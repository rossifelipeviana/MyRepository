import shutil

# Pull of a file in a directory of my PC to that I upload that to GitHub/MyRepository.
def positional_split(dir: str, last_path:int):
    dir = r"E:\Programas\Python\Quimiometria\graph\kstyle.mplstyle"
    dir = dir.split("\\")
    dir = dir[len(dir)-last_path:]
    dir = '\\'.join(dir)
    dir = '\\'+dir
    return dir



src = {
    r"E:\Programas\Python\Quimiometria\graph\kstyle.mplstyle",
    r"E:\Programas\Python\Quimiometria\doc\kstyle.py",
    r"E:\Programas\Python\Polícia Civil\PCNET_Navegator\knavegator.py",
}



print(x)
