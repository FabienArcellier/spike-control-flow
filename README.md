## spike control flow

[![ci](https://github.com/FabienArcellier/spike-control-flow/actions/workflows/main.yml/badge.svg)](https://github.com/FabienArcellier/spike-control-flow/actions/workflows/main.yml)

experimentation with the control flow library to structure calls for LLMs. The goal is to reproduce documentation experimentation
of https://controlflow.ai.

## Usage

```bash
python src/app/spike1.py
python src/app/spike2.py
python src/app/spike3.py
python src/app/spike4.py
python src/app/spike5.py
python src/app/spike6.py
python src/app/spike7.py
python src/app/spike8.py
python src/app/spike9.py
python src/app/spike10.py
```

### Run in gitpod

[gitpod](https://www.gitpod.io/) can be used as an IDE. You can load the code inside to try the code.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/FabienArcellier/spike-control-flow)

## Developper guideline

### Add a dependency

``bash
poetry add requests
``
### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
poetry install
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version

```bash
poetry update
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
poetry shell
```

### Run the continuous integration process

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
$ poetry run alfred ci
```

### Rebuild the blueprint from scratch

I have to regularly rebuild it to update dependencies.

* [maintain this blueprint](./maintain%20this%20blueprint.md)

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018-2025 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
