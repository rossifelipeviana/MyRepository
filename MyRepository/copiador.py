###################################################################################
# Pull files in a directory of my PC to that I upload that to GitHub/MyRepository.
###################################################################################

from kos.kos import *

my_pc = [
    r'E:\Programas\Python\Quimiometria\RDC166\kdecorator\kdecorator.py',
    r'E:\Programas\Python\Quimiometria\RDC166\kdocx\kstyle.py',
    r'E:\Programas\Python\Quimiometria\RDC166\kmatplotlib\kstyle.mplstyle',
    r'E:\Programas\Python\Quimiometria\RDC166\kstats\kstats.py',
]
my_pc = [dir.replace('\\', '/') for dir in my_pc]

my_git = [
    r'E:\Programas\Python\MyRepository\MyRepository\kdecorator\kdecorator.py',
    r'E:\Programas\Python\MyRepository\MyRepository\kdocx\kstyle.py',
    r'E:\Programas\Python\MyRepository\MyRepository\kmatplotlib\kstyle.mplstyle',
    r'E:\Programas\Python\MyRepository\MyRepository\kstats\kstats.py',
]
my_git = [dir.replace('\\', '/') for dir in my_git]

copier(my_pc, my_git, reverse=False)
print('Well done')
