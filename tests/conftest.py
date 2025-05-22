import os

# Start virtual display only in CI
if os.getenv("CI"):
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1024, 768))
    display.start()