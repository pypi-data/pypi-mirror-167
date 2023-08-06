import PySimpleGUI as sg
from psgtray import SystemTray

from synck import application_name
from synck.gui import preferences_dialog


def gui_main():

    menu = ["", ["Sync", "---", "Preferences", "Exit"]]

    window = sg.Window(application_name, layout=[[]], finalize=True)  # needed for SystemTray
    window.hide()

    tray = SystemTray(menu, window=window, tooltip=application_name)  # , icon=sg.DEFAULT_BASE64_ICON)

    while True:
        _, values = window.read()
        event = values[0]

        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Preferences":
            preferences_dialog()

    tray.close()  # optional but without a close, the icon may "linger" until moused over
    window.close()
