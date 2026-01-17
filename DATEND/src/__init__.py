#imports packages needed for DATEND
import subprocess
try:
    import PySide6
except:
    try:
        subprocess.check_call(["pip", "install", 'PySide6'])
    except:
        subprocess.check_call(["pip3", "install", 'PySide6'])
    import PySide6

try:
    import docx
except:
    try:
        subprocess.check_call(["pip", "install", 'python-docx'])
    except:
        subprocess.check_call(["pip3", "install", 'python-docx'])
    import docx