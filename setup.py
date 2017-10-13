from numpy.distutils.core import setup, Extension
#from numpy.distutils.misc_util import Configuration

#from setuptools import setup, Extension
import numpy
#include_dirs_numpy = [numpy.get_include()]

shape = Extension('symeess.shape.shp',
                  # extra_compile_args=['-std=c99'],
                  #include_dirs=include_dirs_numpy,
                  sources=['fortran/shp.pyf', 'fortran/shp.f90'])

setup(name='symeess',
      version='0.1',
      description='Programa de simetria',
      author='Abel Carreras',
      author_email='abelcarreras83@gmail.com',
      packages=['symeess',
                'symeess.shape',
                'symeess.molecule'],
      # scripts=['scripts/dynaphopy'],
      ext_modules=[shape])

