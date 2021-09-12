# ASCII TRAIN PRINTER

## Introduction

ASCII Train is a python library that given a string representation of a train, prints an ASCII-art representation of this train.

## Installation

Clone the project and cd on the root folder.

Run on PowerShell

```bash
./setup.ps1
```

## Uninstall

```bash
pip uninstall ascii-train
```

## Usage

```python
from ascii_train import Train

# prints '<HHHH::|____|::|____|::|____|'
tr = Train("HCCC")
tr.print()

# prints '|____|::|____|::|____|'
tr.detach_head()
tr.print()

# prints '|____|::|____|'
tr.detach_end()
tr.print()

# prints '<HHHH::|^^^^|::|^^^^|::|____|'
tr = Train("HCCC")
tr.fill()
tr.fill()
tr.print()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)