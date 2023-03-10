import pystray
import PIL.Image
import main
import threading
# system tray icon management
image = PIL.Image.open("neural-network.png")


def multiThread():
    # MultiThreading didnt work !!
    thread = threading.Thread(target=main.startMavis())
    thread.start()


def on_click(icon, item):
    if str(item) == "Start Mavis":
        multiThread()
    # if str(item) == "Stop Mavis":

    if str(item) == "Exit":
        systray.stop()


systray = pystray.Icon("Mavis", image, menu=pystray.Menu(
    pystray.MenuItem("Start Mavis", on_click),
    pystray.MenuItem("Stop Mavis", on_click),
    pystray.MenuItem("Exit", on_click),
    pystray.MenuItem("exit2", on_click, visible=False)
))

systray.run()
