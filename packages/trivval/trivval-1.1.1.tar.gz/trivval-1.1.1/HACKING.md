# Hacking on the trivval library

This is a very much incomplete attempt at, at the same time,
a style guide and a set of how-to procedures for working on
the `trivval` library's source.

## Code style conventions

Use the `black` tool (`tox -e black-reformat`) for source code
formatting. The maximum line length is 100 characters.

Import modules, not symbols. Not only does that make it a bit more
clear which symbol comes from which library, but it is also easier to
mock them in the test suite if necessary.

Use type annotations everywhere. Add any new files to the `defs.pyfiles`
list in the `tox.ini` file to include them in the static source code
checks.

When adding new files to the project, also add EditorConfig definitions for
them in the `.editorconfig` file.

## Running the various tests

The `tox.ini` file defines several tests to be run on the `trivval`
library's source code: static code checkers (`black`, `flake8`,
`mypy`, `pylint`) and a unit tests suite.

The most straightforward way to run all the tests is by invoking
the Tox tool directly:

    tox -p all

If [the tox-delay tool][tox-delay] is installed, it may be used to
only run the actual unit tests suite if all the static source code
checks pass:

    tox-delay -p all -e unit-tests

The same result - run all the static checkers first, then the unit tests -
may be obtained by pointing [the Nix shell][nix-shell] to the `tox.nix`
expression. The latter can be invoked as-is or passed a "py" parameter to
specify the Python version suffix (e.g. "39", "311", etc.):

    nix-shell --pure tox.nix
    nix-shell --pure --arg py 311 tox.nix

[nix-shell]: https://nixos.wiki/wiki/Development_environment_with_nix-shell "Development environment with nix-shell"
[tox-delay]: https://gitlab.com/ppentchev/tox-delay "Run some Tox tests after others have completed"

## Version control workflow

The author of the `trivval` library prefers a rebase workflow, not
a merge one, when keeping up with changes in remote Git repositories.

## Contact the author

For comments and suggests, contact [Peter Pentchev][roam].

[roam]: mailto:roam@ringlet.net "Peter Pentchev"
