To create a binary distribution (single file with bundled python), use pyinstaller: https://www.pyinstaller.org/

pip install pyinstaller
pyinstaller --onefile reset_tool.py

Note: Whether you'll get 32-bit or 64-bit executables depends on whether you used 32-bit or 64-bit Python!
