# Adversarial Resilience Learning --- Design of Experiments


## Introduction

(Coming soon ...)

## Installation

ArsenAI is written in Python. It provides a `setup.py` that installs
the minimal set of packages to run arsenai. Use, preferable in a
virtual environment:

    $ ./setup.py install

or, for development::

    $ pip install -e .

## Usage

ArsenAI comes with an example experiment file. You find it in the folder 
tests/fixtures/. 
To use arsenAI, simply type

```
$ arsenai generate tests/fixtures/example_experiment.yml
```

An output folder will be created 
(default: (current working directory)/_outputs)) and in that directory, 
palaestrAI run files, which can be executed with 
```
$ palaestrai experiment-start _outputs/Dummy\ Experiment_run-0.yml
```

You can copy the example file and modify it to your needs.

## Documentation

(Coming soon ...)

## Development

(Coming soon ...)
