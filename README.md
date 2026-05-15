# NeonTech

`NeonTech` packages your tokenizer so you can use it directly in Python.

## Usage

```python
from neontech import tokenisers

# Load bundled tokenizer by name (what you asked for)
tokeniser = tokenisers.load_tokeniser("rena1")

encoded = tokeniser.encode("Hello from NeonTech")
print(encoded.ids)
```

You can also load a custom local tokenizer file:

```python
tokeniser = tokenisers.load_tokeniser("/path/to/tokenizer.json")
```

See available bundled tokenizers:

```python
print(tokenisers.available_tokenisers())
```

## Build and publish to PyPI (real package upload)

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

If you want to test first on TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

## GitHub Actions release workflow

This repo now includes workflows:

- `.github/workflows/ci.yml`: builds package and runs `twine check` on pushes/PRs.
- `.github/workflows/publish-pypi.yml`: publishes to PyPI when you push a version tag like `v0.1.0`.

### One-time PyPI setup for GitHub publishing

1. On PyPI, create a **Trusted Publisher** for this GitHub repository.
2. In GitHub, keep the `pypi` environment (used by the workflow).
3. Bump `version` in `pyproject.toml`, commit, tag, and push:

```bash
git tag v0.1.0
git push origin v0.1.0
```
