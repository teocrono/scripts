#import sys
from cx_Freeze import setup, Executable

base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },

}


setup(
    name = "TC WR SPED",
    options = options,
    version = "1.0",
    description = 'arruma sped',
    executables = executables
)