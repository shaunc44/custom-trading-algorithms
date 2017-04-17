from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
	name = "Add Avg Gain",
	ext_modules = cythonize("cy_files/add_avg_gain.pyx")
)