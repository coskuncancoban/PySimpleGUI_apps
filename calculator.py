import PySimpleGUI as sg

def create_window(theme="TanBlue"):
    sg.theme(theme)
    sg.set_options(font="Arial 16")
    button_size = (6,2)
    layout = [
        #[sg.Push(), sg.Text("output", font = "Arial 24")],
        [sg.Text(
            "", 
            font = "Arial 24", 
            justification="right", 
            expand_x=True, 
            pad = (10, 20), # padding = (horizontal, vertical)
            right_click_menu=theme_menu,
            key = "-TEXT-"
            )], 
        [sg.Button("CLEAR", expand_x = True), sg.Button("ENTER", expand_x = True)],
        [sg.Button("7", size = button_size), sg.Button("8", size = button_size), sg.Button("9", size = button_size), sg.Button("*", size = button_size)],
        [sg.Button("4", size = button_size), sg.Button("5", size = button_size), sg.Button("6", size = button_size), sg.Button("/", size = button_size)],
        [sg.Button("1", size = button_size), sg.Button("2", size = button_size), sg.Button("3", size = button_size), sg.Button("-", size = button_size)],
        [sg.Button("0", expand_x = True, size = button_size), sg.Button(".", size = button_size), sg.Button("+", size = button_size)]
    ]

    return sg.Window("Calculator", layout)

theme_menu = ["menu", ["Black", "BluePurple", "DarkRed", "DarkTeal", "TanBlue", "Topanga", "random"]]
window = create_window()

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        current_num.append(event)
        num_string = "".join(current_num)
        window["-TEXT-"].update(num_string)

    if event in ["+", "-", "*", "/"]:
        full_operation.append("".join(current_num))
        current_num = []
        full_operation.append(event)
        window["-TEXT-"].update("")

    if event == "ENTER":
        full_operation.append("".join(current_num))
        result = eval("".join(full_operation))
        window["-TEXT-"].update(result)
        full_operation = []

    if event == "CLEAR":
        current_num = []
        full_operation = []
        window["-TEXT-"].update("")        

window.close()




