from setuptools import setup, find_packages

classifiers = [
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Education',
	'Operating System :: Microsoft :: Windows :: Windows 10',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3'
]

setup(
	name='mdinstasaver',
	version='0.0.1',
	description='An instagram downloader',
	Long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
	url='',
	author='Seyed Mohammad Mahdi Mirjalili',
	author_email='usa.smmm7.2007@gmail.com',
	License='MIT',
	classifiers=classifiers,
	keywords='instagram',
	packages=find_packages(),
	install_requires=['']
)