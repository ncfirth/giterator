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

Example:

```
df = joblib.load('.giterator/function_versions.pkl')
print(df)  # ugly as sin
  function_name contained_in function_hash version                   datetime  \
0    dummy_func      test.py   ltYf8b0tgjE       1 2018-07-13 13:36:09.425704   
1    dummy_func      test.py   66jVYMsiY8M       2 2018-07-13 13:38:35.233723   
2    dummy_func      test.py   Ud7Z0_SYyWQ       3 2018-07-13 13:59:19.534313   

                                       function_text  
0  @giterator\ndef dummy_func(x, y, z):\n    """S...  
1  @giterator\ndef dummy_func(x, y, z):\n    """S...  
2  @giterator\ndef dummy_func(x, y, z=5):\n    ""... 
```

and for the memoisation of the latest version:


```
print(open('.giterator/test_dummy_func_3.txt').read())
input;output
<BoundArguments (x=7, y=2, z=3)>;3.432987845683981
<BoundArguments (x=8, y=5, z=3)>;4.854335752179021
<BoundArguments (x=7, y=2, z=3)>;3.432987845683981
<BoundArguments (x=8, y=5, z=3)>;4.854335752179021
```
