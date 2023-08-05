# wchk

A command line tool to check the status web pages.

## Installation

```console
pip install wchk
```

or

```console
pipx install wchk
```

## Usage

Check a web page:

    wchk https://example.com

Show help:

    wchk -h

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    pipx install hatch
    git clone git@github.com:yaph/wchk.git
    cd wchk
    hatch shell

To run the tests:

    pytest

## License

`wchk` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
