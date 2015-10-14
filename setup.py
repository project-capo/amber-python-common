# coding=utf-8
# !/usr/bin/env python
import sys

try:
    from setuptools import setup
except ImportError:
    sys.stderr.write('using distutils\n')
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='amber-python-common',
    packages=['ambercommon', 'ambercommon.common'],
    package_dir={'ambercommon': 'src/ambercommon',
                 'ambercommon.common': 'src/ambercommon/common'},
    package_data={'': [
        'src/ambercommon/common/runtime.ini'
    ]},
    data_files=[
        ('', [
            'src/ambercommon/common/runtime.ini'
        ]),
    ],
    include_package_data=True,
    install_requires=required,
    version='0.4',
    description='Amber clients in python',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='http://project-capo.github.io/',
    download_url='http://github.com/project-capo/amber-python-common/',
    keywords=['amber', 'common'],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    long_description='''\
'''
)
