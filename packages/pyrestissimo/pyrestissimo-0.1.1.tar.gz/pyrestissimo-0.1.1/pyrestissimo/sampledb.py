import h5py
import numpy
import hdf5plugin
from .utils import ENV_TABLE, INV_ENV_TABLE, db_to_amp, mstoFrameLength


class SampleDB():
    def __init__(self, dbFilename: str, mode: str = 'r'):
        self._mode = mode
        self._file = h5py.File(dbFilename, mode)

    def add_instrument(self, name: str, instID: str = None, brief: str = None):
        if(instID == None):
            instrumentID = '1' if (list(self._file.keys()) == []) else str(int(max(list(self._file.keys()))) + 1)
        else:
            instrumentID = instID
        instrumentSet = self._file.create_group(instrumentID)
        instrumentSet.attrs['name'] = name
        instrumentSet.attrs['brief'] = brief
        return instrumentID

    def add_sample(self,
                    instrumentID: int,
                    pitch: int,
                    sample: numpy.ndarray,
                    samplerate: int = 48000,
                    sustain_db: int = 0,
                    attack_time: int = 0,
                    decay_time: int = 0,
                    release_time: int = 0,
                    loop_start: int = 0,
                    loop_end: int = 0):
        if(not self._mode == 'w' or self._mode == 'r+'):
            raise IOError('Not a writable sampleDB.')

        attackFrame = mstoFrameLength(samplerate, attack_time)
        decayFrame = mstoFrameLength(samplerate, decay_time)
        aPharse = sample[[0, 1], 0:attackFrame]
        aPharse = numpy.interp((numpy.arange(aPharse.shape[1]) * INV_ENV_TABLE.shape[0] / aPharse.shape[1]),
                                numpy.arange(INV_ENV_TABLE.shape[0]),
                                INV_ENV_TABLE) * aPharse
        dPharse = sample[[0, 1], attackFrame:attackFrame + decayFrame]
        dPharse = (numpy.interp((numpy.arange(dPharse.shape[1]) * ENV_TABLE.shape[0] / dPharse.shape[1]),
                                        numpy.arange(ENV_TABLE.shape[0]),
                                        ENV_TABLE * (1 - db_to_amp(sustain_db)))) + db_to_amp(sustain_db) * dPharse
        sPharse = sample[[0, 1], attackFrame + decayFrame:(loop_end if not loop_end == 0 else sample.shape[1])] * db_to_amp(sustain_db)

        thisSample = self._file.create_dataset('{}/{}'.format(instrumentID, pitch),
                                                data=numpy.concatenate((aPharse, dPharse, sPharse), axis=1),
                                                **hdf5plugin.Bitshuffle())
        thisSample.attrs['release_time'] = release_time
        thisSample.attrs['loop_start'] = loop_start
        thisSample.attrs['loop_end'] = loop_end

    def get_instrument_list(self):
        instrumentList = list(self._file.keys())
        return [(i, self._file[i].attrs['name'], self._file[i].attrs['brief'],) for i in instrumentList]

    def get_valid_pitch_list(self, instrumentID):
        return list(self._file['{}'.format(instrumentID)])

    def get_sample(self, instrumentID: int, pitch: int):
        try:
            sample = self._file['{}/{}'.format(instrumentID, pitch)]
        except:
            raise KeyError('Pitch {} or instrumentID {} not found.'.format(pitch, instrumentID))
        return (sample,
                sample.attrs['release_time'],
                sample.attrs['loop_start'],
                sample.attrs['loop_end'])

    def exists(self, instrumentID: int, pitch: int):
        return ('{}/{}'.format(instrumentID, pitch) in self._file)

    def close(self):
        self._file.close()
