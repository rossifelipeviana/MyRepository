###################################################################################
# Pull files in a directory of my PC to that I upload that to GitHub/MyRepository.
###################################################################################

from MyRepository.kos.kos import *

srcs = [
    r"E:\Programas\Python\Quimiometria\graph\kstyle.mplstyle",
    r"E:\Programas\Python\Quimiometria\doc\kstyle.py",
    r"E:\Programas\Python\Polícia Civil\PCNET_Navegator\knav\knavegator.py",
]
srcs = [dir for dir in srcs]

dsts = [
    r"E:\Programas\Python\MyRepository\matplotlib\kstyle.mplstyle",
    r"E:\Programas\Python\MyRepository\docx\kstyle.py",
    r"E:\Programas\Python\MyRepository\Quimiometria\selenium\knavegator.py",
]
dsts = [dir.replace("\\", "/") for dir in dsts]

copier(srcs, dsts, reverse=False)
