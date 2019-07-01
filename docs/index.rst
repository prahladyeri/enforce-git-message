.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
Introduction
============================

.. image:: https://raw.githubusercontent.com/prahladyeri/enforce-git-message/master/logo.png

`enforce-git-message <https://github.com/prahladyeri/enforce-git-message>`_ is a tool for enforcing `conventional git commit messages <https://www.conventionalcommits.org/en/v1.0.0-beta.4/>`_ for all new git repositories you create by running `git init`. For existing repositories, you can go to your source directory and simply run::

	enforce-git-message

Examples of valid commit messages:

.. code-block:: diff

	+ 61c8ca9 fix: navbar not responsive on mobile
	+ 479c48b test: prepared test cases for user authentication
	+ a992020 chore: moved to semantic versioning
	+ b818120 fix: button click even handler firing twice
	+ c6e9a97 fix: login page css
	+ dfdc715 feat(auth): added social login using twitter

Examples of invalid commit messages resulting in an error message:

.. code-block:: diff

	- 61c8ca9 fix for navbar not responsive on mobile
	- 479c48b prepared test cases for user authentication
	- a992020 moved to semantic versioning
	- b818120 fixed button click even handler firing twice
	- c6e9a97 login page css fix
	- dfdc715 added social login auth feature using twitter

Installation
===========================

.. code-block:: bash

	pip install enforce-git-message

Verification
===========================

Go to your source folder and try to commit with a non-conventional message like this and it should fail:

.. code-block:: bash

		> git commit -m "added a new feature for xyz"
		
		COMMIT FAILED!

		Please enter commit message in the conventional format and try to commit again. Examples:

		+ 61c8ca9 fix: navbar not responsive on mobile
		+ 479c48b test: prepared test cases for user authentication
		+ a992020 chore: moved to semantic versioning
		+ b818120 fix: button click even handler firing twice
		+ c6e9a97 fix: login page css
		+ dfdc715 feat(auth): added social login using twitter
		
After that, try doing the commit with a valid message and it should work:

.. code-block:: bash

		> git commit -m "feat(test): added xyz"
		[master (root-commit) 8797aa0] feat(test): added xyz
		 6 files changed, 1 insertion(+)
		 create mode 100644 test.java
		 create mode 100644 foo.txt
		 create mode 100644 bar.txt

Notes
======

`Read this article <https://prahladyeri.com/blog/2019/06/how-to-enforce-conventional-commit-messages-using-git-hooks.html>`_ to fully understand how the enforcement actually works by using git hooks.


Attribution
=============

.. raw:: html

	<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 		    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>


Indices and tables
===========================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
