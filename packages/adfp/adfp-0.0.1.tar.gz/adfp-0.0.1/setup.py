from setuptools import setup, find_packages
from codecs import open
from os import path


from adfp import __version__


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering :: Mathematics',
]

setup(name='adfp',
      version=__version__,
      license='MIT License',
      install_requires=['numpy'],
      author='Takumi Enomoto',
      author_email='eno.sleepy.zzz.zz.z@gmail.com',
      url='https://github.com/enoTak/adfp',
      packages=find_packages(exclude=['tests', 'sample_notebook']),
      description='auto differential framework',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords='auto differential',
      )