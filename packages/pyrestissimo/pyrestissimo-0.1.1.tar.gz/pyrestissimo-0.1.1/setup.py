from setuptools import setup, find_packages

setup(
	name='pyrestissimo',
	version='0.1.1',
	keywords=('audio-processing', 'sampler'),
	description='An extremly fast sampler and symbolized music score renderer(standard midi file and msf supported for now).',
	license='MIT Licence',

	author='Luo Zhongqi',
	author_email='luozhongqi@mail.com',

	packages=['pyrestissimo'],
	include_package_data=True,
	platforms='any',
	install_requires=['numpy>=1.21', 'h5py>=3.0', 'hdf5plugin>=3.0', 'protobuf>=4.21'],
	package_data={
		'': ['*.npy']
	}
)

