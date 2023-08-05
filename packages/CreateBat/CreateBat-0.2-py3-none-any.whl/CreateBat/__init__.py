import os
import sys
import tkinter as tk
from tkinter import filedialog
import pathlib
import re
from typing import Union


def right_path_format(path):
    ossep = re.escape(os.sep)
    return re.sub(fr"[\\/]+", ossep, path)


def ask_for_file(
    title: str = "Select a file", filetypes: tuple = (("Excel files", ".xlsx .xls"),)
) -> str:
    filetypes = list(filetypes)
    root = tk.Tk()
    filename = filedialog.askopenfilename(
        parent=root, title=title, filetypes=filetypes, initialdir=os.getcwd()
    )
    root.withdraw()
    return filename


def create_batch_file_on_desktop(envname: Union[None, str] = None) -> str:
    """

    :param envname: Is only required if you don't use Anaconda
    :return: str (path of bat file)
    """

    if envname is None:
        envname = os.environ.get("CONDA_DEFAULT_ENV")

    pythonexe = sys.executable
    filepath = ask_for_file(
        title="Select a Python script", filetypes=(("Python files", ".py"),)
    )
    filepath_for_batch_file = filepath
    if not "\\" in filepath_for_batch_file or not "/" in filepath_for_batch_file:
        filepath_for_batch_file = os.path.join(envname, filepath)
    filepath_for_batch_file = right_path_format(filepath_for_batch_file)
    executeindict = str(os.sep).join(filepath_for_batch_file.split(os.sep)[:-1])
    purefilename = filepath_for_batch_file.split(os.sep)[-1]
    purebatfilename = "_" + purefilename.split(".")[0] + ".bat"
    desktop = f"{pathlib.Path.home()}{os.sep}Desktop"
    batpath = right_path_format(os.path.join(desktop, purebatfilename))
    addarguments = input("\nDo you want to add parameters? (e.g: --path=C:\\Users )")
    keepconsoleopen = input(
        '\nIf you want to keep the console open after executing the script, press: "y" ?'
    )
    keepconsoleopenstring = " "
    harddisk = pathlib.Path(filepath).parts[0].rstrip(os.sep)
    if keepconsoleopen.lower().strip().strip("'\"") == "y":
        keepconsoleopenstring = " -i "
    batchfile = f"""
    @echo off
    {harddisk}
    cd "{executeindict}"
    echo Activating {envname}
    CALL activate {envname}
    echo Starting Python {filepath_for_batch_file}
    CALL "{pythonexe}"{keepconsoleopenstring}"{filepath_for_batch_file}" {addarguments.strip()}

    """

    with open(batpath, mode="w", encoding="utf-8") as f:
        f.write(batchfile)

    print("Batchfile written to:")
    print(batpath)
    print(f"_____________________\n{batchfile}")
    return batpath
