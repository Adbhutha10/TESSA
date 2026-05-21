# TESSA
**(Tissue Environment Simulation Syntax Architecture)**

A Domain-Specific Language (DSL) and compiler system designed to simplify biological simulation, tumor microenvironments, and cellular automata modeling.

## Overview
TESSA bridges the gap between biology and computer science by allowing researchers to define complex cellular behavior using a clean, human-readable language syntax, and compiling it down into executable simulation code.

### Example Code
```text
cell CancerCell {
    divide every 6h
    migrate toward oxygen
    die if glucose < 10
}

cell ImmuneCell {
    attack CancerCell if distance < 3
}
```

## Architecture
1. **Lexer / Parser:** Built using `lark`
2. **Compiler Pipeline:** AST -> Semantic Analyzer -> Intermediate Representation
3. **Simulation Runtime:** Target Python/NumPy (Phase 2), CUDA (Phase 5)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run the test parser interactively:
```bash
python test_parser.py
```
Or pass a file:
```bash
python test_parser.py examples/sample.bsl
```
