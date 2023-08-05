import numpy
from distutils.core import setup
from Cython.Build import cythonize

setup(
    include_dirs=[numpy.get_include()],
    ext_modules=cythonize(["agg_mem.pyx", "comp_mem.pyx", "inverse_tc.pyx"])
)