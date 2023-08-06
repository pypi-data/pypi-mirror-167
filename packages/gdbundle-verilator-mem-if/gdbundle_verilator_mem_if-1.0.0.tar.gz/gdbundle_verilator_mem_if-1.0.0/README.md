# gdbundle-verilator-mem-if

This package implements the `gdb_loader` method required by `gdbundle` for loading Python custom commands into GDB.

Your `.gdbinit` file should be updated with the following:

```python
python
import subprocess, sys
from pathlib import Path

# Execute Python using the user's shell and pull out the sys.path (for site-packages)
paths = subprocess.check_output('python -c "import os,sys;print(os.linesep.join(sys.path).strip())"',shell=True).decode("utf-8").split()

# Extend GDB's Python search path
sys.path.extend(paths)

# Init and load plugins
import gdbundle
gdbundle.init()
end
```

See the following links for background on `gdbundle`.

https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api  
https://interrupt.memfault.com/blog/advanced-gdb  
https://interrupt.memfault.com/blog/gdbundle-plugin-manager  
