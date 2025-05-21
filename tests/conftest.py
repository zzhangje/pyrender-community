import os
from pyvirtualdisplay import Display

# Start virtual display only in CI
if os.getenv("CI"):
    display = Display(visible=0, size=(1024, 768))
    display.start()