import pystray
import PIL.Image
import main

# system tray icon management
image = PIL.Image.open("neural-network.png")


def on_click(icon, item):
    if str(item) == "Start Mavis":
        main.startMavis()
    if str(item) == "Exit":
        systray.stop()


systray = pystray.Icon("Mavis", image, menu=pystray.Menu(
    pystray.MenuItem("Start Mavis", on_click),
    pystray.MenuItem("Exit", on_click)
))

systray.run()
