import argparse
from os import replace
from emoji import emojize
from rich import print

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a message with an emoji.")
    # replace None with a helpful description of the f(x)
    parser.add_argument("--name", default=":sparkles:", help="The emoji name to use.")
    # default like ":rocket:" and a clear help string
    parser.add_argument("--msg", default="", help="The message to display with the emoji.")
    # default empty string and clear help
    return parser

def render_emoji(name: str, msg: str) -> str:
    """Return the combined emoji + message string."""
    symbol = emojize(name, language="alias") # DO NOT Change this
    # line the first None is needed
    output = f"{symbol} {msg}".strip() # TODO: build f-string combining symbol + msg
    # (strip trailing spaces)
    return output

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    # TODO: ensure args.name and args.msg become strings
    name = str(args.name) # e.g., str(args.name)
    msg = str(args.msg) # e.g., str(args.msg)
    result = render_emoji(name, msg)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())