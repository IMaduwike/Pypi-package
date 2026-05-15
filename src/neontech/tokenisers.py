"""Tokeniser helpers for NeonTech.

Usage:
    from neontech import tokenisers
    tok = tokenisers.default_tokeniser()
"""

from __future__ import annotations

from importlib.resources import as_file, files
from pathlib import Path

from tokenizers import Tokenizer


def _bundled_tokenizer_path() -> Path:
    resource = files("neontech").joinpath("rena1/tokenizer.json")
    with as_file(resource) as path:
        return Path(path)


def default_tokeniser() -> Tokenizer:
    """Load the default bundled `rena1` tokeniser."""
    return Tokenizer.from_file(str(_bundled_tokenizer_path()))


def load_tokeniser(path: str | Path) -> Tokenizer:
    """Load a tokeniser from a tokenizer.json file path."""
    return Tokenizer.from_file(str(path))
