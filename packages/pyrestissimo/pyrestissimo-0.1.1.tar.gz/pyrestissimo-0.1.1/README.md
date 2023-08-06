# Dependenicy
python:
	pip install numpy pedalboard h5py hdf5plugin

# Usage
## Synthesize audio from midi
Refer to test/test_render_piano.ipynb

## Import new sample
Refer to script/import_sample.ipynb

## Get instrument list and range from a sample database
```
import random

from fastsynth import SampleDB
db = SampleDB('../assets/classical_minor.hdf5', 'w') # Path of sample database

print(db.get_instrument_list())
instrumentID = random.choice(db.get_instrument_list())[0]
print(db.get_valid_pitch_list(instrumentID))
```
