from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "re", "sys", "contextlib", "io", "pathlib", "platform", "os"],
    "include_files": [
        "data_engine.cpython-312-x86_64-linux-gnu.so",  
    ]
}

setup(
    name="DataEngineGUI",
    version="1.0",
    description="C++ Data Engine GUI",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py")]
)