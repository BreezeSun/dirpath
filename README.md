# dirpath
A library for managing directory paths in the python environment
## Installation
```console
pip install dirpath
```

## Usage
### Insert absolute path
```python
import dirpath
dirpath.insert(r'D:\MyProject\pack')
from pack import func1
```

### Insert relative path
```python
import dirpath
dirpath.insert('pack')
from pack import func2
```
### Multiple relative path
The relative path must be in the current file path
```python
import dirpath
dirpath.insert('pack',dir_index=0)
from pack import func3
```

### Change the environment priority
```python
import dirpath
dirpath.insert('pack',env_index=2)
from pack import func4
```
