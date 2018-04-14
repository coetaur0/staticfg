# StatiCFG
Python3 control flow graph generator

StatiCFG is a module that allows you to produce control flow graphs (CFGs) for Python 3 programs. The CFGs it generates
can be easily visualised with graphviz and used for control flow analysis. They cannot, however, be used for symbolical 
execution (hence the name **StatiC**FG: the CFGs produced by the module are purely "static").

## Installation

To install StatiCFG, simply clone this repository and run the command `pip3 install --upgrade .` from inside it.

## Usage

To use StatiCFG, simply import the module in your Python interpreter or program, and use the `staticfg.CFGBuilder` class to 
build CFGs. For example, to build the CFG of a program defined in a file with the path *./example.py*, the following code can 
be used:

```
from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('example.py', './example.py')
```

This returns the CFG for the code in *./example.py* in the `cfg` variable. The first parameter of `build_from_file` is the 
desired name for the CFG, and the second one is the path to the file containing the source code. The produced CFG can then be 
visualised with:

```
cfg.build_visual('exampleCFG', 'pdf')
```

The first paramter of `build_visual` is the desired name for the DOT file produced by the method, and the second one is the
format to use for the visualisation.
