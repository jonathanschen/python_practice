try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'jonathanschen@gmail.com',
	'version': '.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
	