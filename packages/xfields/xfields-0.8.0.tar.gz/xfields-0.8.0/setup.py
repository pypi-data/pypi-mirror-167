# copyright ################################# #
# This file is part of the Xfields Package.   #
# Copyright (c) CERN, 2021.                   #
# ########################################### #

from setuptools import setup, find_packages, Extension

#######################################
# Prepare list of compiled extensions #
#######################################

extensions = []


#########
# Setup #
#########

setup(
    name='xfields',
    version='0.8.0',
    description='Field Maps and Particle In Cell',
    long_description=("Python package for the computation of fields generated "
                      "by particle ensembles in accelerators.\n\n"
                      "This package is part of the Xsuite collection."),
    url='https://xsuite.readthedocs.io/',
    packages=find_packages(),
    ext_modules = extensions,
    include_package_data=True,
    install_requires=[
        'numpy>=1.0',
        'scipy',
        'pandas',
        'xobjects>=0.0.4',
        'xtrack>=0.0.1',
        ],
    author='G. Iadarola et al.',
    license='Apache 2.0',
    download_url="https://pypi.python.org/pypi/xfields",
    project_urls={
            "Bug Tracker": "https://github.com/xsuite/xsuite/issues",
            "Documentation": 'https://xsuite.readthedocs.io/',
            "Source Code": "https://github.com/xsuite/xfields",
        },
    )
