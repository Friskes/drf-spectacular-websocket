# Contribution Guide

> First off, thanks for taking the time to contribute!

Contributions include but are not restricted to:
- Reporting bugs
- Contributing to code
- Writing tests
- Writing documentation

## A recommended flow of contributing to an Open Source project

1. First, [fork](https://github.com/Friskes/drf-spectacular-websocket/fork) this [project](https://github.com/Friskes/drf-spectacular-websocket) to your own namespace using the fork button at the top right of the repository page.

2. Clone the upstream repository to local:
    ```bash
    git clone https://github.com/Friskes/drf-spectacular-websocket.git
    ```

3. Add the fork as a new remote:
    > where fork is the remote name of the fork repository.
    ```bash
    git remote add fork https://github.com/YOURNAME/drf-spectacular-websocket.git
    git fetch fork
    ```

## ProTips:

1. Don't modify code on the main branch, the main branch should always keep track of origin/main.
    > To update main branch to date:
    ```bash
    git pull origin main
    # In rare cases that your local main branch diverges from the remote main:
    git fetch origin && git reset --hard main
    ```

2. Create a new branch based on the up-to-date main branch for new patches.

3. Create a Pull Request from that patch branch.

## Local development

> We recommend working in a [virtual environment](https://docs.python.org/3/tutorial/venv.html). Feel free to create a virtual environment with either the venv module or the virtualenv tool. For example:

1. Create virtual environment
    ```bash
    python -m venv .venv
    . .venv/bin/activate  # linux
    .venv/Scripts/activate  # windows
    ```

2. Install dependencies
    ```bash
    python -m pip install -e .[dev]
    ```

3. Install [pre-commit](https://pre-commit.com/)
    ```bash
    pre-commit install
    ```

> Run `pre-commit run --all-files` to run linters and formatters. This step is optional and will be executed automatically by git before you make a commit, but you may want to run it manually in order to apply fixes

#### Now, all dependencies are installed into the Python environment you chose, which will be used for development after this point.

### Run tests
```bash
pytest
```

> The test suite is still simple and needs expansion! Please help write more test cases.

## Making changes to the project

1. Make your changes

2. Commit your changes to git. We follow [conventional commits](https://www.conventionalcommits.org/) which are enforced using a pre-commit hook.

3. Push the changes to your fork

4. Open a [pull request](https://docs.github.com/en/pull-requests). Give the pull request a descriptive title indicating what it changes. The style of the PR title should also follow [conventional commits](https://www.conventionalcommits.org/), and this is enforced using a GitHub action.

5. Add yourself as a contributor using the [all-contributors bot](https://allcontributors.org/docs/en/bot/usage)

### Guidelines for writing code

- Code should be [Pythonic and zen](https://peps.python.org/pep-0020/)

- All functions, methods, classes, and attributes should be documented with a docstring. We use the [Google docstring style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
    > If you come across a function or method that doesn't conform to this standard, please update it as you go

- Writing and running tests
    - Tests are contained within the `tests` directory, and follow the same directory structure as the `drf_spectacular_websocket` module. If you are adding a test case, it should be located within the correct submodule of `tests`. E.g., tests for `drf_spectacular_websocket/schemas/schema.py` reside in `tests/schemas/test_schema.py`.

### Creating a New Release

1. Checkout the main branch:
    ```bash
    git checkout main
    ```

2. Run the release preparation script:
    ```bash
    gh release create <version number tag> --target <branch name> --notes ""
    ```

3. Replace <version number tag> with the desired version number following the [versioning scheme](https://semver.org/) and [PEP 440](https://peps.python.org/pep-0440/).

4. Commit the changes to main:
    > Replace vX.Y.Z with the actual version number.
    ```bash
    git commit -am "chore(release): prepare release vX.Y.Z"
    ```

5. Create a new branch for the release:
    ```bash
    git checkout -b vX.Y.Z
    ```

6. Push the changes to a vX.Y.Z branch:
    ```bash
    git push origin vX.Y.Z
    ```

7. Open a pull request from the vX.Y.Z branch to main.

    > Once the pull request is approved, go to the draft release on GitHub (the release preparation script will provide a link).

8. Review the release notes in the draft release to ensure they look correct.

9. If everything looks good, click "Publish release" to make the release official.

10. Go to the [Release Action](https://github.com/Friskes/drf-spectacular-websocket/actions/workflows/publish-to-pypi.yml) and approve the release workflow if necessary.

    > Check that the release workflow runs successfully.
