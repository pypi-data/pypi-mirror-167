import numpy
import os

ENV_TABLE = numpy.load(os.path.join(os.path.dirname(__file__), './envTable.npy'))
INV_ENV_TABLE = numpy.flipud(ENV_TABLE)
DB_TABLE = numpy.load(os.path.join(os.path.dirname(__file__), './dbTable.npy'))

def db_to_amp(db: float):
	if(not -120 <= db <= 0):
		raise ValueError('db value must between -120 to 0.')
	return DB_TABLE[int(-db * 10)]

def mstoFrameLength(samplerate: int, ms: int):
    return int(samplerate * ms / 1000.)

