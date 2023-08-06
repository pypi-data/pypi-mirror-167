import numpy

class Note:
    def __init__(self, instrumentID: int, pitchNum: int, startTime: float, duration: float, dynamic: float):
        if(not (0 <= pitchNum <= 128)):
            raise ValueError('pitchNum %d out of range.'.format(pitchNum))
        if(not (0. <= dynamic <= 1.)):
            raise ValueError('dynamic %d out of range.'.format(dynamic))
        self._pitchNum = pitchNum
        self._startTime = startTime
        self._duration = duration
        self._instrumentID = instrumentID
        self._dynamic = dynamic

    @property
    def pitchNum(self):
        return self._pitchNum
    
    @property
    def startTime(self):
        return self._startTime
    
    @property
    def duration(self):
        return self._duration
    
    @property
    def instrumentID(self):
        return self._instrumentID

    @property
    def dynamic(self):
        return self._dynamic

