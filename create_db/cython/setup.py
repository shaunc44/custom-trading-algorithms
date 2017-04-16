from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
	name = "Hello World",
	ext_modules = cythonize("cy_files/add_avg_gain.pyx")
)