all: dist/wiipcrt /usr/local/bin/wiipcrt

installdeps:
	pip install pyinstaller

installdeps3:
	pip3 install pyinstaller

dist/wiipcrt: wiipcrt.py
	pyinstaller --onefile wiipcrt.py

/usr/local/bin/wiipcrt: dist/wiipcrt
	install -o 0 -g 0 -m 0755 dist/wiipcrt /usr/local/bin/wiipcrt
