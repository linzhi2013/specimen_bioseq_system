#####################################################
# Copyright (c) 2020-2021 Guanliang Meng. All rights reserved.
#
# This file is part of the Specimen Bioseq System.
#
# The Specimen Bioseq System is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# The Specimen Bioseq System is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# the Specimen Bioseq System. If not, see <http://www.gnu.org/licenses/>.
#
#####################################################


import setuptools

import sysconfig
from setuptools.command.build_py import build_py as _build_py
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

# noinspection PyPep8Naming
class build_py(_build_py):

    def find_package_modules(self, package, package_dir):
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for (pkg, mod, filepath) in modules:
            if os.path.exists(filepath.replace('.py', '.pye')):
                continue
            filtered_modules.append((pkg, mod, filepath, ))
        return filtered_modules


setuptools.setup(
    name="specimen_bioseq_system",
    version="2.0",
    author='Guanliang Meng',
    author_email='linzhi2012@gmail.com',
    description="Specimen Bioseq Information Managment System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    packages=setuptools.find_packages(),
    url='https://www.ororca.cn/',
    include_package_data=True,

    install_requires=[
        'biopython>=1.54',
        'django==3.1.2',
        'django-import-export==2.4.0',
        'django-grappelli==2.14.2',
        'djangorestframework==3.12.1',
        'psycopg2',
        'pyconcrete'
    ],

    entry_points={
        'console_scripts': [
            'sbs_manager=specimen_bioseq_system.manage:main',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    cmdclass={
        'build_py': build_py
    }
)
