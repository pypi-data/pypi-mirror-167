import PySimpleGUI as sg

from synck import get_pref, application_name


def preferences_dialog():

    pref = get_pref()
    parent_directory_key = "parent_directory"

    layout = [[sg.Text(f"{application_name} parent directory:")], [sg.Input(key="parent_directory")], [sg.Text(f"node: {pref.node_id}")], [sg.Button("Cancel"), sg.Button("Save")]]
    window = sg.Window(f"{application_name} preferences", layout, modal=True, finalize=True)
    window[parent_directory_key].update(pref.parent_directory)

    while True:
        event, values = window.read()
        if event == "Save":
            pref.parent_directory = window[parent_directory_key]
        elif event == "Cancel" or event == sg.WIN_CLOSED:
            break

    window.close()
