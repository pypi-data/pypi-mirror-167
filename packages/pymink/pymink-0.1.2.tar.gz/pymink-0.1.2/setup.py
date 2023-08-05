from pathlib import Path
from setuptools import setup, find_packages
from version import __version__, __rootdir__


setup(
    author="Fábio Lucas Pereira Carneiro",
    author_email="fabiolucas.carneiro@gmail.com",
    license="GNU General Public License v3.0",
    url="https://github.com/fabiocfabini/pymink",
    name=__rootdir__,
    version=__version__,
    description='A Python library to perform N Gram based text analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=list(map(lambda x: str(x).split('/')[-1].split('.')[0], Path(__rootdir__).rglob('*.py'))),
    package_dir={'': __rootdir__},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'nltk',
        'pandas',
        'matplotlib',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
)