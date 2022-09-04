###################################################################################
# Codes to manipulate your OS.
###################################################################################
import os
import shutil


def copier(sources, destinations, reverse=False):
    """Copy a list of files to your destiny

    Args:
        sources (iterable): Path of source destinations (str): Path of destination
        reverse (iterable): Change source by destination and destination
        by source. Defaults to False.
    """
    if reverse == True:
        _ = sources
        sources = destinations
        destinations = _

    for src, dst in zip(sources, destinations):

        # Verify if that source folder exists.
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        # Fix the slashes
        src.replace("\\", "/")
        src.replace("\\", "/")

        # Verify that be same files.
        try:
            if os.path.samefile(src, dst):
                continue
        except FileNotFoundError:
            pass

        # Remove if this exist.
        try:
            os.remove(dst)
        except FileNotFoundError:
            pass

        # Try to move the folder, if it doesn't print the error message.
        try:
            shutil.copy(src, dst)
        except:
            raise


def split_by_end_of_path(
    dir: str, position: int = None, wantfinal: str = True
) -> str:
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
