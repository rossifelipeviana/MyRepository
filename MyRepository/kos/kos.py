###################################################################################
# Codes to manipulate your OS.
###################################################################################
import os
import shutil
import filecmp


def copier(sources, destinations, reverse=False):
    """Copy a list of files to your destiny.

    Args:
        sources (iterable): Path of source destinations (str): Path of destination
        reverse (iterable): Change source by destination and destination
        by source. Defaults to False.
    """
    print('')
    print('')
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
            # if os.path.samefile(src, dst):
            #     continue
            if filecmp.cmp(src, dst):
                print(f'{os.path.basename(src)} já estava atualizado.')
                continue
            else:
                while True:
                    continuar = input(
                        f'Já existe um arquivo "{os.path.basename(src)}" na pasta de destino diferente do original, deseja realizar a substituição? '
                    )
                    if continuar in ('y', 'yes', 's', 'sim', 'n', 'nao', 'não', 'no'):
                        break
            if continuar == 'n':
                continue
        except FileNotFoundError:
            raise
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


def split_path(path: str, position: int = None, wantfinal: str = True) -> str:
    """
    Split a directory by the positional slash that you want, take beginning or the end of directory

    Args:
        dir (str): Path on the filesystem to split
        position (int, optional): What slash that have been splitted. Defaults to None.
        wantfinal (str, optional): Do you want the final?. Defaults to True.

    Returns:
        str: The part of the path that you wanted splitted.
    """

    # Definitions
    path = path.split("\\")
    n = len(path)

    # Split the path and take what u want.
    path = path[n - position :] if wantfinal else path[: n - position]
    path = "\\".join(path)
    path = "\\" + path if wantfinal else path + "\\"

    return path
