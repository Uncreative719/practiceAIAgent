# Calculator

A simple command-line calculator that evaluates arithmetic expressions with support for addition, subtraction, multiplication, and division, respecting standard operator precedence.

## Features

- Supports `+`, `-`, `*`, `/` operators
- Respects operator precedence (`*` and `/` before `+` and `-`)
- JSON-formatted output
- Handles nested and complex expressions

## Project Structure

```
calculator/
├── main.py          # CLI entry point
├── tests.py         # Unit tests
└── pkg/
    ├── calculator.py # Core Calculator class
    └── render.py     # JSON output formatter
```

## Usage

```bash
python main.py "<expression>"
```

Expressions must be space-separated tokens:

```bash
python main.py "3 + 5"
# {"expression": "3 + 5", "result": 8}

python main.py "2 * 3 - 8 / 2 + 5"
# {"expression": "2 * 3 - 8 / 2 + 5", "result": 7}
```

## Running Tests

```bash
python tests.py
```

## How It Works

1. `Calculator.evaluate()` tokenizes the input expression by splitting on spaces
2. `_evaluate_infix()` processes tokens using two stacks (values and operators), applying the shunting-yard algorithm respecting precedence
3. Results are formatted as JSON by `format_json_output()` in `render.py`
