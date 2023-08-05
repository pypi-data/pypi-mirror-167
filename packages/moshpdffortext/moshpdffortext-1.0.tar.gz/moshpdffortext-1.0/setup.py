import setuptools
from pathlib import Path

ReadMe = Path("README.md").read_text

setuptools.setup(
    name="moshpdffortext",
    version=1.0,
    long_description=Path('README.md').read_text(),
    packages=setuptools.find_packages(exclude=['tests', 'data'])
)
