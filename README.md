# 🚀 Python Emoji Renderer

A simple Python command-line tool that prints an emoji alias (like `:sparkles:`) alongside an optional message. Great for learning about command-line argument parsing, timing performance, and testing with `pytest`.

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv testenv
source testenv/bin/activate
pip install -r requirements.txt
```

## Run

Example usage:

```bash
python make_emoji.py --name ":sparkles:" --msg "Hello"
```

Output:

```bash
:sparkles: Hello
```

## Time it

We can measure how fast emoji conversion runs using Python’s built-in timeit module.

Command:

```bash
python3 -m timeit -n 1000 -s "from emoji import emojize" "emojize(':rocket:')"


# Example Result:
1000 loops, best of 5: 10.3 usec per loop
```

## Test

To verify your script works as expected, run the test suite:

```bash
pytest -q


# Example Output:
1 passed in 0.12s   [100%]
```

## Project Structure

```bash
python_emoji/
│
├── make_emoji.py          # Main script
├── requirements.txt       # Dependencies
├── tests/
│   └── test_smoke.py      # Basic smoke test
└── README.md              # Documentation
```

## Notes

Built with:

- emoji
  - converts alias names to emojis.
- rich
  - for nice terminal printing.
- Tested on macOS with Python 3.10+.
- Educational exercise focusing on argparse, testing, and timing.
