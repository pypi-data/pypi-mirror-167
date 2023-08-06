#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Yarik1gou
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Yarik1gou
"""

version = '0.1'
'''
with open('README.md', encoding='utf-8') as f:
	long_description = f.read()
'''

long_description = '''Protect your python file with a password(This version is still raw)!'''

setup(
	name='PyProtect',
	version=version,

	author='Yarik1gou',
	author_email='erundopel@internet.ru',

	description=(
		u'Protecting python files'
		u'Yarik1gou'
	),
	long_description=long_description,
	#long_description_content_type='text/markdown',

	url='https://github.com/yar-exe/PyProtect',
	download_url='https://github.com/yar-exe/PyProtect/archive/v{}.zip'.format(
		version
	),

	license='Apache License, Version 2.0, see LICENSE file',

	packages=['PyProtect'],
	install_requires=[],

	classifiers=[
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
	]
)