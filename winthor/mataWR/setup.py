#import sys
from cx_Freeze import setup, Executable

base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

executables = [Executable("mataWReColetor.py", base=base)]

packages = ["idna","urllib","requests","urllib3","queue"]
options = {
    'build_exe': {
        'packages':packages,
    },




}


setup(
    name = "TC",
    options = options,
    version = "1.0",
    description = '',
    executables = executables
)
