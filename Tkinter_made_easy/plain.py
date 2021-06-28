import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32': base = 'Win32GUI'
opts = {'include_files': ['lottery.png'], 'includes': ['re']}

setup(name='Lotto',
      version=1.0,
      description='Lottery number picker',
      options={'build_exe': opts},
      executables=[Executable('Lottery game.py', base=base)])
