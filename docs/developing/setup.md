
## Get Started!

Ready to contribute? Here's how to set up `electricpie` for local development.

1. Fork the `electricpie` repo on GitHub.
2. Clone your fork locally::

    `git clone git@github.com:your_name_here/electricpie.git`

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    `mkvirtualenv electricpie`
    `cd electricpie/`
    `python setup.py develop`

4. Create a branch for local development::

    `git checkout -b name-of-your-bugfix-or-feature`

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    `flake8 electricpie tests`
    `python setup.py test or pytest`
    `tox`

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    `git add .`
    `git commit -m "Your detailed description of your changes."`
    `git push origin name-of-your-bugfix-or-feature`

7. Submit a pull request through the GitHub website.
