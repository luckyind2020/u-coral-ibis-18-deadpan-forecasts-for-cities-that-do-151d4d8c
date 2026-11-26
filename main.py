"""Entry point for the make.fun Deadpan Forecasts bounty.

Reads the single forecast line from entry.txt next to this file,
prints it to stdout, and writes it to /output/entry.txt when the
grader's output directory exists.
"""

from pathlib import Path


def normalize_line(raw: str) -> str:
    """Collapse any stray whitespace runs to single spaces."""
    return " ".join(raw.split())


def load_entry() -> str:
    """Read the forecast line from entry.txt beside this script."""
    entry_path = Path(__file__).with_name("entry.txt")
    raw = entry_path.read_text(encoding="utf-8")
    line = normalize_line(raw)
    validate_entry(line)
    return line


def validate_entry(line: str) -> None:
    """Enforce the bounty rules: one non-empty line, at most 160 chars."""
    if not line:
        raise ValueError("entry.txt must contain a non-empty line")
    if "\n" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > 160:
        raise ValueError(f"entry is {len(line)} chars, over the 160 limit")


def write_output(line: str) -> None:
    """Write the line to /output/entry.txt when /output exists."""
    output_dir = Path("/output")
    if output_dir.is_dir():
        (output_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")


def main() -> None:
    line = load_entry()
    print(line)
    write_output(line)


if __name__ == "__main__":
    main()
