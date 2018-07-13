Giterator
=========
Lightweight decorator to do version control on individual functions.

Usage:

```
@giterator
def my_function(x, y, z):
	return x+y+z
```

Doing this creates a hidden folder `giterator` (needs to be renamed) which will contain a version history of the function and for each version the inputs and outputs of everytime it was called.
