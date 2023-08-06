from glob import glob
from os.path import basename, dirname, splitext, join
from setuptools import setup, find_packages

setup(
    name="pafdc_pycts",
    version="0.3.1",
    description="Textile capacitive touch sensor tools and utilities.",
    author="rjvallett",
    author_email="rjvallett@drexel.edu",
    url="https://github.com/pafdc/pycts",
    license="None",
    install_requires=['numpy', 'pyserial'],
    packages=find_packages("src"),
    package_dir={"" : "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')]
)
