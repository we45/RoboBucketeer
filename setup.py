from setuptools import setup
from codecs import open
from os import path

current_path = path.abspath(path.dirname(__file__))

with open(path.join(current_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RoboBucketeer',
    version='1.0',
    packages=[''],
    package_dir={'': 'robobucketeer'},
    url='https://github.com/we45/RoboBucketeer',
    license='MIT',
    author='we45',
    author_email='info@we45.com',
    description='Robot Framework Library for RoboBuckteer - S3 Buckets & Subdomain Enumeration',
    install_requires = [''],
    long_description = long_description,
    long_description_content_type='text/markdown'
)