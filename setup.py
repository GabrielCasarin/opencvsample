from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy as np
import subprocess
 
proc_libs = subprocess.check_output("pkg-config --libs opencv4".split())
proc_incs = subprocess.check_output("pkg-config --cflags opencv4".split())

libs = [lib for lib in proc_libs.decode().split()]
incs = [inc for inc in proc_incs.decode().split()]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize(Extension("opencvsample",
        sources = ["opencvsample.pyx"],
        language = "c++",
        include_dirs=[np.get_include()] + incs,
        extra_link_args=libs,
        extra_compile_args=["-std=c++17"])
    )
)