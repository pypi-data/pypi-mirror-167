# ctime

ctime is a python library for how long does the function takes for execute completally

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ctime.

```bash
pip install ctime
```

## Usage

```python
import ctime

@ctime.ctime() # Optional args: simplified, printable
def function():
    ... # Your code
    
function()
```

```
Function "function_name" took X seconds.
```

## License
[MIT](https://choosealicense.com/licenses/mit/)