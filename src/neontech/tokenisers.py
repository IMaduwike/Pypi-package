"""Tokeniser helpers for NeonTech.

Usage:
    from neontech import tokenisers
    tok = tokenisers.load_tokeniser("rena1")
    tok = tokenisers.default_tokeniser()
"""

from __future__ import annotations

from importlib.resources import as_file, files
from pathlib import Path

from tokenizers import Tokenizer

_BUNDLED = {
    "rena1": "rena1/tokenizer.json",
}


def available_tokenisers() -> list[str]:
    """Return the names of bundled tokenisers."""
    return sorted(_BUNDLED.keys())


def _bundled_tokenizer_path(name: str) -> Path:
    key = name.lower()
    if key not in _BUNDLED:
        supported = ", ".join(available_tokenisers())
        raise ValueError(f"Unknown bundled tokeniser '{name}'. Available: {supported}")

    resource = files("neontech").joinpath(_BUNDLED[key])

def _bundled_tokenizer_path() -> Path:
    resource = files("neontech").joinpath("rena1/tokenizer.json")
    with as_file(resource) as path:
        return Path(path)


def load_tokeniser(name_or_path: str | Path = "rena1") -> Tokenizer:
    """Load a tokeniser by bundled name (e.g. "rena1") or tokenizer.json file path."""
    if isinstance(name_or_path, Path):
        return Tokenizer.from_file(str(name_or_path))

    lowered = name_or_path.lower()
    if lowered in _BUNDLED:
        return Tokenizer.from_file(str(_bundled_tokenizer_path(lowered)))

    return Tokenizer.from_file(name_or_path)
def default_tokeniser() -> Tokenizer:
    """Load the default bundled `rena1` tokeniser."""
    return Tokenizer.from_file(str(_bundled_tokenizer_path()))


def load_tokeniser(path: str | Path) -> Tokenizer:
    """Load a tokeniser from a tokenizer.json file path."""
    return Tokenizer.from_file(str(path))
