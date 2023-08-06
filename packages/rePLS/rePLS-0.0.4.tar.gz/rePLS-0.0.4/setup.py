from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Residual Partial Least Squares Learning '
LONG_DESCRIPTION = '...'

# Setting up
setup(
    name="rePLS",
    version=VERSION,
    author="thanhvd",
    author_email="duythanhvu.uet@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'scikit-learn'],
    keywords=['PLS', 'rePLS','PCR', 'LR'],
)