import numpy
from multiprocessing import Process, Queue
import hdf5plugin
from .MSF_pb2 import Sequence
from .note import Note
from .sampledb import SampleDB
from .utils import ENV_TABLE, mstoFrameLength


class Prestissimo:
    def __init__(self, bpm: int, samplerate: int, samplefile: str):
        if(not (20 <= bpm <= 300)):
            raise ValueError('bpm %d out of range.'.format(bpm))
        if(not (samplerate == 44100)):
            raise ValueError('invalid samplerate %d, only 44100 is supported now.'.format(samplerate))

        self._bpm = bpm
        self._samplerate = samplerate
        self._quarterLength = int(samplerate / (bpm / 60))
        self._sampleDB = SampleDB(samplefile, 'r')
        self._dbName = samplefile
        self._noteList = {}
        self._frameLength = 0

    def append(self, note = Note):
        thisTimbre = (note.instrumentID, note.pitchNum)
        noteFrameLength = Prestissimo.quartertoFrameLength(self._samplerate, self._bpm, note.duration)
        noteFrameStartTime = Prestissimo.quartertoFrameLength(self._samplerate, self._bpm, note.startTime)
        noteFrameEndTime = noteFrameStartTime + noteFrameLength + self._samplerate * 2
        self._frameLength = noteFrameEndTime if noteFrameEndTime > self._frameLength else self._frameLength
        if(thisTimbre in self._noteList):
            if(noteFrameLength in self._noteList[thisTimbre]):
                self._noteList[thisTimbre][noteFrameLength].add((noteFrameStartTime, note.dynamic))
            else:
                self._noteList[thisTimbre][noteFrameLength] = set([(noteFrameStartTime, note.dynamic)])
        else:
            self._noteList[thisTimbre] = {noteFrameLength: set([(noteFrameStartTime, note.dynamic)])}

    @staticmethod
    def construct_note(samplerate: int, sample: tuple, frameLength: int):
        releaseFrameLength = mstoFrameLength(samplerate, sample[1])
        noteTotalFrameLength = frameLength + releaseFrameLength
        adsPharse = sample[0][[0,1], 0:frameLength]
        rPharse = sample[0][[0,1],frameLength:frameLength + releaseFrameLength]
        rPharse = numpy.multiply(numpy.interp((numpy.arange(rPharse.shape[1]) * ENV_TABLE.shape[0] / rPharse.shape[1]),
                                            numpy.arange(ENV_TABLE.shape[0]),
                                            ENV_TABLE), rPharse)

        return numpy.concatenate((adsPharse, rPharse), axis=1)

    @staticmethod
    def synth_work(samplerate: int, sampleDB: str, notes: Queue, frameLength: int, output: Queue):
        res = numpy.zeros((2, frameLength), dtype='float32')
        db = SampleDB(sampleDB, 'r')
        while(not notes.empty()):
            try:
                noteset = notes.get(timeout=.1)
            except:
                output.put(res)
                db.close
                break
            sample = db.get_sample(noteset[0][0], noteset[0][1])
            for timeInfo in noteset[1]:
                thisNote = Prestissimo.construct_note(samplerate, sample, timeInfo[0])
                for startFrame, dynamic in list(timeInfo[1]):
                    endFrame = startFrame+thisNote.shape[1]
                    res[[0, 1], startFrame:endFrame] = numpy.add(numpy.multiply(thisNote, [dynamic]), res[[0, 1], startFrame:endFrame])
        output.put(res)
        db.close()

    @staticmethod
    def _standardization(data):
        return numpy.multiply(data, [(1 / numpy.amax(data.ravel()))])

    def render(self, processNum: int, standardization=True):
        notes = Queue()
        worker_res = Queue()
        res = numpy.zeros((2, self._frameLength), dtype='float32')
        for timbre, timeInfo in self.noteList.items():
            timeInfos = []
            for lg, st in timeInfo.items():
                timeInfos.append((lg, st))
            notes.put(((timbre), timeInfos))
        processes = []
        for i in range(processNum):
            p = Process(target=Prestissimo.synth_work,
                        args=(self._samplerate,
                            self._dbName,
                            notes,
                            self._frameLength,
                            worker_res))
            p.start()
            processes.append(p)

        for i in range(processNum):
            res += worker_res.get()

        for p in processes:
            p.join()

        return Prestissimo._standardization(res) if standardization else res

    def from_msf(self, path: str, track: int):
        with open(path, 'rb') as f:
            seq = Sequence.FromString(f.read())
            for n in (Note(seq.track[track].instrumentID, note.pitch, note.start / seq.quantization, note.duration / seq.quantization, note.attribute[0].value / 256) for note in seq.track[track].note):
                self.append(n)

    @staticmethod
    def quartertoFrameLength(samplerate: int, bpm:int, quarter: float):
        return int(quarter * int(samplerate / (bpm / 60)))

    @property
    def noteList(self):
        return self._noteList

    @property
    def sampleDB(self):
        return self._sampleDB

