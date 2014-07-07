#!/usr/bin/env python
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup configuration."""

import platform

from ez_setup import use_setuptools
use_setuptools()
# pylint:disable=C6204
import setuptools

# Configure the required packages and scripts to install, depending on
# Python version and OS.
REQUIRED_PACKAGES = [
    'ez-setup==0.9',
    'google-apputils==0.4.0',
    'httplib2==0.8',
    'mimeparse==0.1.3',
    'mock==1.0.1',
    'oauth2client==1.2',
    'protorpc==0.9.1',
    'python-dateutil==1.5',
    'python-gflags==2.0',
    'pytz==2013.7',
    'wsgiref==0.1.2',
    ]
CONSOLE_SCRIPTS = [
    'gen_client = apitools.gen.gen_client:run_main',
    ]

py_version = platform.python_version()

if py_version < '2.7':
  REQUIRED_PACKAGES.append('unittest2==0.5.1')
  REQUIRED_PACKAGES.append('argparse==1.2.1')

_NAMESPACE = 'apitools'
_APITOOLS_VERSION = '0.2'

setuptools.setup(
    name='apitools',
    version=_APITOOLS_VERSION,
    description='client libraries for humans',
    url='http://github.com/craigcitro/apitools',
    author='Craig Citro',
    author_email='craigcitro@google.com',
    # Contained modules and scripts.
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
        },
    install_requires=REQUIRED_PACKAGES,
    provides=[
        'apitools (%s)' % (_APITOOLS_VERSION,),
        ],
    # PyPI package information.
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    license='Apache 2.0',
    keywords='apitools',
    )
