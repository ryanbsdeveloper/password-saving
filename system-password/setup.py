import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable('main.py', base=base, icon='img/senha.ico')
]

includeFile = ['img/','imports/', 'windows/']

setup(
    name="Save Password",
    version="0.1",
    description="Salvamento de senhas, e gerador de senhas criptografadas.",
    options={"build_exe":{'include_files':includeFile}},
    executables=executables
)