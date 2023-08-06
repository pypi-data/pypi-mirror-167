from setuptools import find_packages, setup

from Cython.Build import cythonize

setup(
    name="testing_cython",
    version="0.1.0",
    packages=find_packages(),
    author="William Rosenbaum",
    description="Testing Cython",
    ext_modules=cythonize(["testing_cython/fib.pyx"]),
    install_requires=[
        'Cython'
    ]
)