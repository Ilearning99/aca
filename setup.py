from distutils.core import setup, Extension
from Cython.Build import cythonize

NAME = "ac"
VERSION = '1.0'
DESCRIPTION = 'Aho-Corasick automaton implementation'
AUTHOR = 'Timo Petmanson @Funderbeam OÜ'
AUTHOR_EMAIL = 'tpetmanson@gmail.com'
LICENSE = "GPLv3"

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Linguistic',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5'
]

REQUIREMENTS = [
    'Cython>=0.24.1,<0.25',
    'pytest']


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,

    ext_modules=cythonize(
        Extension('ac/ac_cpp',
                  sources=['ac/ac_cpp.pyx'],
                  language='c++',
                  extra_compile_args=['-std=c++11', '-mmacosx-version-min=10.9'],
                  extra_link_args=['-std=c++11'])
    )
)
