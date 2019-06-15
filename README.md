![pypi](https://img.shields.io/pypi/v/enforce-git-messages.svg)
![python](https://img.shields.io/pypi/pyversions/enforce-git-messages.svg)
![implementation](https://img.shields.io/pypi/implementation/enforce-git-messages.svg)
<!-- https://img.shields.io/travis/prahladyeri/enforce-git-messages/master.svg -->
<!-- ![docs](https://readthedocs.org/projects/enforce-git-messages/badge/?version=latest) -->
![license](https://img.shields.io/github/license/prahladyeri/enforce-git-messages.svg)
![last-commit](https://img.shields.io/github/last-commit/prahladyeri/enforce-git-messages.svg)
<!--![commit-activity](https://img.shields.io/github/commit-activity/w/prahladyeri/enforce-git-messages.svg)-->
[![follow](https://img.shields.io/twitter/follow/prahladyeri.svg?style=social)](https://twitter.com/prahladyeri)
# enforce-git-messages

Enforces [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for all new git repositories you create by running `git init .`. For existing repositories, you can go to your source directory and simply run:

	enforce-git-messages .

# Installation

	pip install enforce-git-messages
	
	
# Verifying

Go to your source folder and try to commit with a non-conventional message like this and it should fail:

	> git commit -m "added a new feature for xyz"
	Traceback (most recent call last):
	  File "C:/Users/prahlad/Documents/scripts/check_commit.py", line 14, in <module>
		main()
	  File "C:/Users/prahlad/Documents/scripts/check_commit.py", line 11, in main
		if m == None: raise Exception("conventional commit validation failed")
	Exception: conventional commit validation failed
	
After that, try doing the commit with a valid message and it should work:

	> git commit -m "feat(test): added xyz"
	>
	
