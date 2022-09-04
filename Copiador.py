###################################################################################
# Pull files in a directory of my PC to that I upload that to GitHub/MyRepository.
###################################################################################

import shutil
import os


def split_by_end_of_path(dir: str, position: int = None, wantfinal: str = True) -> str:
    """I don't needed this function
    Split a directory by the file, take beginning or the end of directory

    Args:
        dir (str): Path on the filesystem to split
        position (int, optional): What slash that have been splitted. Defaults to None.
        wantfinal (str, optional): Do you want the final?. Defaults to True.

    Returns:
        str: The part of the path that you wanted splitted.
    """

    dir = dir.split("\\")
    n = len(dir)
    dir = dir[n - position :] if wantfinal else dir[: n - position]
    dir = "\\".join(dir)
    dir = "\\" + dir if wantfinal else dir + "\\"

    return dir


def copier(sources, destinations, reverse=False):
    """Copy a source of the file to your destiny

    Args:
        sources (str): Path of source destinations (str): Path of destination
        reverse (bool, optional): Change source by destination and destination
        by source. Defaults to False.
    """

    for src, dst in zip(sources, destinations):

        # Verify that source folder exists
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        # Fix the slashes
        src.replace("\\", "/")
        src.replace("\\", "/")

        # Try to move the folder, if it doesn't print the error message
        try:
            if not (reverse):
                shutil.copy(src, dst)
            elif reverse:
                shutil.copy(dst, src)
        except Exception as e:
            print(e)


if __name__ == "__main__":

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
