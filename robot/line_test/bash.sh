echo "Run Xvfb"
Xvfb :99 -screen 0 640x480x8 -nolisten tcp &
echo "Run line test"
python3 line_test.py