from glob import glob
from distutils.core import setup

setup(name='lc',
      version='0.4',
      py_modules=['langconfluxer'],
      data_files=[('share/lc/', glob('*.txt'))],
      scripts=['lconflux']
      )
