"""Command-line interface."""

import argparse
from typing import List
from typing import Optional

from leina import __version__


def main(argv: Optional[List[str]] = None) -> None:
    """Saffire."""
    parser = argparse.ArgumentParser(description="Saffire: Self Awareness for FIRE")

    parser.add_argument("--version", action="version", version=f"{__package__} v{__version__}")

    parser.parse_args(argv)


if __name__ == "__main__":
    main()  # pragma: no cover
