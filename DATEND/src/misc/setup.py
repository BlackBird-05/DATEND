from setuptools import setup

APP = ["DATEND.py"]
DATA_FILES = [("resources", ["Icon.icns"])]
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "Icon.icns",
    "packages": ["docx", "PySide6", "tkinter"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)




