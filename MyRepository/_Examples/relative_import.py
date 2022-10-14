'''
If you need import a file in up a directory.
'''
import sys
import os

# Two up folder.
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

# One up folder.
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))