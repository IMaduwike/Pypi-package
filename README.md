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
