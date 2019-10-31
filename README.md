# RDFScript

A scripting language for creating RDF graphs.

* Define, extend, and expand parameterisable templates for common patterns of RDF triples.
* Share your RDFScript templates with collaborators, or import their templates for use in your own script.
* Serialise as [turtle](https://www.w3.org/TR/turtle/), [n3](https://www.w3.org/TeamSubmission/n3/), [rdf/xml](https://www.w3.org/TR/rdf-syntax-grammar/), or easily extend RDFScript with a custom serialiser.
* Perform complex manipulations of the graph by hooking into Python code defined as extensions.

## Get Started

### Dependencies

RDFScript requires Python 3.x.

Python package dependencies are listed in `setup.py`.

### Install

1. Download or clone repository. `git clone https://github.com/intbio-ncl/shortbol.git`
2. Navigate to RDFScript directory. `cd rdfscript`

(This method requires setuptools, which can be installed from your package manager on most \*nix systems, and is probably called python3-setuptools or similar)
3a. As a non-root user. `python setup.py install --user`

(This method requires pip)
3b.`python -m pip install rdflib lxml requests ply pathlib pysbolgraph`

## Example usage

Running the example in `examples/templates.rdfsh`

`python run.py -s rdfxml examples/templates.rdfsh -o <output-file>`

Run the REPL

`python run.py -s rdfxml -o <output-file>`

Display command line options, including available serialisations.

`python run.py -h`

The example files in `examples/` are commented with some explaination of the language.

### SBOL example

1. Shortbol libaries are now linked by default.
2. In the rdfscript directory `python run.py -s sbolxml templates/simple_example.rdfsh -o <output-file>` 
(Multiple examples are in the directory explaining different functionality.)
3. `output-file` is an SBOL file.

### Extensions

Extensions provide a way to execute Python code to do additional, more complex processing of the RDF triples generated by expanding templates.

Extensions intended as built-ins should be added to the `extensions` package. 'Third party' extensions can also be added at the command line, as long as they are in the Python PATH.


### Testing

A test suite using the Python3 `unittest` package is under the `test/` directory.

Run the tests from the project root using `python -m unittest`
