thing = 'something'

###############################################################################
# Method 1
###############################################################################

# Check if the object have __len__
if hasattr(thing, "__len__"):
	pass
	
###############################################################################
# Method 2
###############################################################################
from collections.abc import Iterable

# Check if object is iterable
if isinstance(thing, Iterable):
	pass

