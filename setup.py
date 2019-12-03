from beSMArt import __version__, __doc__
from setuptools import setup, find_packages


def readme():
    with open("README.md") as fp:
        return fp.read()


setup(
    name="beSMArt",
    version=__version__,
    author="Patryk Niedzwiedzinski",
    author_email="pniedzwiedzinski19@gmail.com",
    description=__doc__,
    long_description=readme(),
    license="MIT",
    packages=find_packages(),
    install_requires=['requests']
)
