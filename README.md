![pypi](https://img.shields.io/pypi/v/enforce-git-message.svg)
![python](https://img.shields.io/pypi/pyversions/enforce-git-message.svg)
![implementation](https://img.shields.io/pypi/implementation/enforce-git-message.svg)
<!-- https://img.shields.io/travis/prahladyeri/enforce-git-message/master.svg -->
<!-- ![docs](https://readthedocs.org/projects/enforce-git-message/badge/?version=latest) -->
![license](https://img.shields.io/github/license/prahladyeri/enforce-git-message.svg)
![last-commit](https://img.shields.io/github/last-commit/prahladyeri/enforce-git-message.svg)
<!--![commit-activity](https://img.shields.io/github/commit-activity/w/prahladyeri/enforce-git-message.svg)-->
[![donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JM8FUXNFUK6EU)
[![follow](https://img.shields.io/twitter/follow/prahladyeri.svg?style=social)](https://twitter.com/prahladyeri)
# enforce-git-message

![project logo](https://repository-images.githubusercontent.com/192069745/136f2780-903c-11e9-8155-7a04e973c798){width=100px}

Enforces [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for all new git repositories you create by running `git init`. For existing repositories, you can go to your source directory and simply run:

	enforce-git-message

# Installation

	pip install enforce-git-message
	
	
# Verifying

Go to your source folder and try to commit with a non-conventional message like this and it should fail:

	> git commit -m "added a new feature for xyz"
	Traceback (most recent call last):
	  File ".git/hooks/commit-msg", line 22, in <module>
		main()
	  File ".git/hooks/commit-msg", line 19, in main
		if m == None: raise Exception("conventional commit validation failed")
	Exception: conventional commit validation failed
	
After that, try doing the commit with a valid message and it should work:

	> git commit -m "feat(test): added xyz"
	>
	
# Notes

[Read this article](https://prahladyeri.com/blog/2019/06/how-to-enforce-conventional-commit-messages-using-git-hooks.html) to fully understand how the enforcement actually works by using git hooks.

# Attribution

- *Tick Icon made by [smashicons](https://www.flaticon.com/authors/smashicons) from www.flaticon.com is licensed by [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/)*