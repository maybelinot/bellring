#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-04 14:04:46
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-12-17 17:21:42


# python-2.7 setup.py build


from setuptools import setup

VERSION_FILE = "bellring/_version.py"
VERSION_EXEC = ''.join(open(VERSION_FILE).readlines())
__version__ = ''
exec(str(VERSION_EXEC))  # update __version__
if not __version__:
    raise RuntimeError("Unable to find version string in %s." % VERSION_FILE)

# acceptable version schema: major.minor[.patch][-sub[ab]]
__pkg__ = 'bellring'
__pkgdir__ = {'bellring': 'bellring'}
__pkgs__ = ['bellring']
__desc__ = 'Export tables to Google Spreadsheets.'
__scripts__ = ['bin/bellring']
__irequires__ = [
    # CORE DEPENDENCIES
    'functioncache==0.92',
    'argparse==1.3.0',
    'pyyaml==3.11',
]
__xrequires__ = {
    'tests': [
        'pytest==2.7.2',
        # 'instructions',
        # 'pytest-pep8==1.0.6',  # run with `py.test --pep8 ...`
    ],
    # 'docs': ['sphinx==1.3.1', ],
    # 'github': ['PyGithub==1.25.2', ],
    # 'invoke': ['invoke==0.10.1', ],
}

pip_src = 'https://pypi.python.org/packages/src'
__deplinks__ = []

# README is in the parent directory
readme_pth = 'README.rst'
with open(readme_pth) as _file:
    readme = _file.read()


default_setup = dict(
    license='GPLv3',
    author='Eduard Trott',
    author_email='etrott@redhat.com',
    maintainer='Chris Ward',
    maintainer_email='cward@redhat.com',
    long_description=readme,
    data_files=[],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        'Topic :: Utilities',
    ],
    keywords=['information'],
    dependency_links=__deplinks__,
    description=__desc__,
    install_requires=__irequires__,
    extras_require=__xrequires__,
    name=__pkg__,
    package_dir=__pkgdir__,
    packages=__pkgs__,
    scripts=__scripts__,
    version=__version__,
    zip_safe=False,
)

setup(**default_setup)
