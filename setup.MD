1) Check which Python versions TD ships

ls "/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/"

If you see 3.11, use the three lines below exactly:

2) Install/upgrade pip in TD’s Python

"/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/3.11/bin/python3.11" -m ensurepip --upgrade

3) Upgrade build tools

"/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/3.11/bin/python3.11" -m pip install --upgrade pip setuptools wheel

4) Install matplotlib (plus numpy, pillow)

"/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/3.11/bin/python3.11" -m pip install matplotlib numpy pillow