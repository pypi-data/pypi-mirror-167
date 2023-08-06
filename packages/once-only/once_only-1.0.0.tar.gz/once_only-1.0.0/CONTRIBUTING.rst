.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/mikapfl/once_only/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

`once_only` could always use more and better documentation!

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/pflueger/once_only/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that contributions are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `once_only` for local development.

1. Fork the `once_only` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/once_only.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper
   installed, this is how you set up your fork for local development::

    $ cd once_only/
    $ make virtual-environment
    $ make install-pre-commit

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass our tests and
   automatically format everything according to our rules::

     $ make lint

   Often, the linters can fix errors themselves, so if you get failures, run
   ``make lint`` again to see if any errors need human intervention.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring and check the generated
   API documentation.
3. The pull request will be tested on python 3.7, 3.8, 3.9, and 3.10.

Deploying
---------

.. highlight:: shell

A reminder for the maintainers on how to deploy.

1.  Commit all your changes.
2.  Run ``tbump X.Y.Z``.
3.  Wait a bit that the release on github is created.
4.  Upload the release to pyPI: ``make release``
