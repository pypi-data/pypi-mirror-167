from codecs import open
from os import path

from setuptools import find_packages, setup

__version__ = '0.1.4'

here = path.abspath(path.dirname(__file__))


def read_list(filename):
    if path.exists(path.join(path.dirname(__file__), filename)):
        with open(path.join(path.dirname(__file__), filename)) as f:
            return f.read().splitlines()
    else:
        return []


required = read_list('requirements.txt')
required_dev = read_list('requirements-dev.txt')

setup(
    name='apimate',
    version=__version__,
    description='API mate',
    long_description='Collection utils for create clean architecture REST API application with FastAPI',
    long_description_content_type='text/plain',
    url="https://github.com/antipooh/apimate.git",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    author='Oleg Komkov',
    install_requires=required,
    extras_require={
        'dev': required_dev,
        'mongodb': ['pymongo', 'motor'],
        'redis': ['aioredis']
    },
    author_email='okomkov@gmail.com',
)
