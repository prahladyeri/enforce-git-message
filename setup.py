#!/usr/bin/env python3
import os, sys
import enforce_git_message
from enforce_git_message import __version__, __description__, __author__, __email__, __license__, __title__
from setuptools import setup, find_packages
from setuptools.command.install import install
#from subprocess import check_call
#from pkg_resources import Requirement, resource_filename
import site
from distutils.dir_util import copy_tree
#import shutil

app_name = "enforce-git-message"
pkg_name = "enforce_git_message"

class PostInstallCommand(install):
	"""Post-installation for installation mode."""
	def run(self):
		os.system("echo CUSTOM_PRE_MESSAGE")
		install.run(self)
		os.system("echo CUSTOM_POST_MESSAGE")
		#conf_path_temp = resource_filename(Requirement.parse(app_name), "git-templates")
		#the_path = site.getusersitepackages() # => Useless and misleading
		fpath = os.path.join(self.install_lib, pkg_name)
		fpath = os.path.join(fpath, "git-templates")
		tpath = os.path.join(os.path.expanduser("~"), ".git-templates")
		os.system("git config --global init.templatedir ~/.git-templates")
		copy_tree(fpath, tpath)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

s = setup(
	name=app_name,
	version=__version__,
	license=__license__,
	description=__description__,
	long_description=read("README.md"),
	long_description_content_type='text/markdown',
	keywords="security,scanner",
	url='https://github.com/prahladyeri/%s' % app_name,
	packages=find_packages(),
	include_package_data=True,
	entry_points={
		"console_scripts": [
			"enforce-git-message = enforce_git_message.main:main",
		],
	},
	install_requires=[],
	python_requires = ">= 3.4",
	author=__author__,
	author_email=__email__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	cmdclass={
		'install': PostInstallCommand,
	},
	)

