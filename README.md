![pypi](https://img.shields.io/pypi/v/enforce-git-message.svg)
![python](https://img.shields.io/pypi/pyversions/enforce-git-message.svg)
![license](https://img.shields.io/github/license/prahladyeri/enforce-git-message.svg)
![last-commit](https://img.shields.io/github/last-commit/prahladyeri/enforce-git-message.svg)
![docs](https://readthedocs.org/projects/enforce-git-message/badge/?version=latest)
[![donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JM8FUXNFUK6EU)
[![follow](https://img.shields.io/twitter/follow/prahladyeri.svg?style=social)](https://twitter.com/prahladyeri)

# enforce-git-message

![project logo](https://raw.githubusercontent.com/prahladyeri/enforce-git-message/master/logo.png)

Enforces [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for all new git repositories you create by running `git init`. For existing repositories, you can go to your source directory and simply run:

	enforce-git-message

Examples of valid commit messages:

```diff
+ 61c8ca9 fix: navbar not responsive on mobile
+ 479c48b test: prepared test cases for user authentication
+ a992020 chore: moved to semantic versioning
+ b818120 fix: button click even handler firing twice
+ c6e9a97 fix: login page css
+ dfdc715 feat(auth): added social login using twitter
```

Examples of invalid commit messages resulting in an error message:

```diff
- 61c8ca9 fix for navbar not responsive on mobile
- 479c48b prepared test cases for user authentication
- a992020 moved to semantic versioning
- b818120 fixed button click even handler firing twice
- c6e9a97 login page css fix
- dfdc715 added social login auth feature using twitter
```

# Installation

	pip install enforce-git-message
	
# Documentation

Detailed docs are available at <https://enforce-git-message.readthedocs.io/en/latest/>.

# Attribution

<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 		    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>