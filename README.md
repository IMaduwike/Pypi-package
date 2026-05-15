# NeonTech

`NeonTech` is a Python package that ships your `rena1` tokeniser for easy usage:

```python
from neontech import tokenisers

# Load the bundled tokenizer
tokeniser = tokenisers.default_tokeniser()

encoded = tokeniser.encode("Hello from NeonTech")
print(encoded.ids)
```

It also supports loading custom tokenizer JSON files:

```python
custom = tokenisers.load_tokeniser("/path/to/tokenizer.json")
```
