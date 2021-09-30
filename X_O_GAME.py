from tkinter import *
from tkinter import ttk, Button
from tkinter import messagebox

played = True
x_points = 0
o_points = 0


def destroy_result_labels():
    label_for_result["text"] = ""


def disable_buttons():
    cube_1["state"] = DISABLED
    cube_2["state"] = DISABLED
    cube_3["state"] = DISABLED
    cube_4["state"] = DISABLED
    cube_5["state"] = DISABLED
    cube_6["state"] = DISABLED
    cube_7["state"] = DISABLED
    cube_8["state"] = DISABLED
    cube_9["state"] = DISABLED


def enable_buttons():
    cube_1["state"] = NORMAL
    cube_2["state"] = NORMAL
    cube_3["state"] = NORMAL
    cube_4["state"] = NORMAL
    cube_5["state"] = NORMAL
    cube_6["state"] = NORMAL
    cube_7["state"] = NORMAL
    cube_8["state"] = NORMAL
    cube_9["state"] = NORMAL


def start_over():
    cube_1["text"] = " "
    cube_1.config(bg="black")
    cube_2["text"] = " "
    cube_2.config(bg="black")
    cube_3["text"] = " "
    cube_3.config(bg="black")
    cube_4["text"] = " "
    cube_4.config(bg="black")
    cube_5["text"] = " "
    cube_5.config(bg="black")
    cube_6["text"] = " "
    cube_6.config(bg="black")
    cube_7["text"] = " "
    cube_7.config(bg="black")
    cube_8["text"] = " "
    cube_8.config(bg="black")
    cube_9["text"] = " "
    cube_9.config(bg="black")
    label_for_result["text"] = ""
    enable_buttons()


def reset_score():
    global x_points, o_points, played
    x_points = 0
    o_points = 0
    played = True
    players_scores["text"] = str(x_points) + " - " + str(o_points)
    start_over()


def winner_check():
    global x_points, o_points, played
    winner = False
    winner_player = None
    game_in_progress = True
    if (
        cube_1["text"] != " "
        and cube_2["text"] != " "
        and cube_3["text"] != " "
        and cube_4["text"] != " "
        and cube_5["text"] != " "
        and cube_6["text"] != " "
        and cube_7["text"] != " "
        and cube_8["text"] != " "
        and cube_9["text"] != " "
    ):
        game_in_progress = False
        start_over()
        played = True
    elif (
        cube_1["text"] == " "
        and cube_2["text"] == " "
        and cube_3["text"] == " "
        and cube_4["text"] == " "
        and cube_5["text"] == " "
        and cube_6["text"] == " "
        and cube_7["text"] == " "
        and cube_8["text"] == " "
        and cube_9["text"] == " "
    ):
        game_in_progress = True
        start_over()
        played = True

    if cube_1["text"] == "X" and cube_2["text"] == "X" and cube_3["text"] == "X":
        cube_1.config(bg="red")
        cube_2.config(bg="red")
        cube_3.config(bg="red")
        label_for_result["text"] = "Player 1 wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_1["text"] == "X" and cube_5["text"] == "X" and cube_9["text"] == "X":
        cube_1.config(bg="red")
        cube_5.config(bg="red")
        cube_9.config(bg="red")
        label_for_result["text"] = "Player 1 wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_1["text"] == "X" and cube_4["text"] == "X" and cube_7["text"] == "X":
        cube_1.config(bg="red")
        cube_4.config(bg="red")
        cube_7.config(bg="red")
        label_for_result["text"] = "Player 1 wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_2["text"] == "X" and cube_5["text"] == "X" and cube_8["text"] == "X":
        cube_2.config(bg="red")
        cube_5.config(bg="red")
        cube_8.config(bg="red")
        label_for_result["text"] = "Player 1 wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_3["text"] == "X" and cube_6["text"] == "X" and cube_9["text"] == "X":
        cube_3.config(bg="red")
        cube_6.config(bg="red")
        cube_9.config(bg="red")
        label_for_result["text"] = "Player 1 wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_4["text"] == "X" and cube_5["text"] == "X" and cube_6["text"] == "X":
        cube_4.config(bg="red")
        cube_5.config(bg="red")
        cube_6.config(bg="red")
        label_for_result["text"] = "Player 1 wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_7["text"] == "X" and cube_8["text"] == "X" and cube_9["text"] == "X":
        cube_7.config(bg="red")
        cube_8.config(bg="red")
        cube_9.config(bg="red")
        label_for_result["text"] = "Player 1 wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_3["text"] == "X" and cube_5["text"] == "X" and cube_7["text"] == "X":
        cube_3.config(bg="red")
        cube_5.config(bg="red")
        cube_7.config(bg="red")
        label_for_result["text"] = "Player 1 Wins !"
        winner = True
        winner_player = "X"
        x_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_1["text"] == "O" and cube_2["text"] == "O" and cube_3["text"] == "O":
        cube_1.config(bg="red")
        cube_2.config(bg="red")
        cube_3.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_1["text"] == "O" and cube_5["text"] == "O" and cube_9["text"] == "O":
        cube_1.config(bg="red")
        cube_5.config(bg="red")
        cube_9.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_1["text"] == "O" and cube_4["text"] == "O" and cube_7["text"] == "O":
        cube_1.config(bg="red")
        cube_4.config(bg="red")
        cube_7.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_2["text"] == "O" and cube_5["text"] == "O" and cube_8["text"] == "O":
        cube_2.config(bg="red")
        cube_5.config(bg="red")
        cube_8.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_3["text"] == "O" and cube_6["text"] == "O" and cube_9["text"] == "O":
        cube_3.config(bg="red")
        cube_6.config(bg="red")
        cube_9.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_4["text"] == "O" and cube_5["text"] == "O" and cube_6["text"] == "O":
        cube_4.config(bg="red")
        cube_5.config(bg="red")
        cube_6.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_7["text"] == "O" and cube_8["text"] == "O" and cube_9["text"] == "O":
        cube_7.config(bg="red")
        cube_8.config(bg="red")
        cube_9.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif cube_3["text"] == "O" and cube_5["text"] == "O" and cube_7["text"] == "O":
        cube_3.config(bg="red")
        cube_5.config(bg="red")
        cube_7.config(bg="red")
        label_for_result["text"] = "Player 2 Wins !"
        winner = True
        winner_player = "O"
        o_points += 1
        disable_buttons()
        root.after(5000, destroy_result_labels)
    elif game_in_progress == False:
        label_for_result["text"] = "Draw !"
        root.after(5000, destroy_result_labels)

    if winner == True:
        players_scores["text"] = str(x_points) + " - " + str(o_points)
        if winner_player == "X":
            played = True
        elif winner_player == "O":
            played = False


def button_click(cube):
    global played
    if cube["text"] == " " and played == True:
        cube["text"] = "X"
        played = False
        winner_check()
    elif cube["text"] == " " and played == False:
        cube["text"] = "O"
        played = True
        winner_check()

    else:
        messagebox.showerror(title="Error", message="This box is already filled !")


def Close_app():
    root.quit()


root = Tk()
root.overrideredirect(False)
root.minsize(width=1080, height=672)
root.update()
# root.eval("tk::PlaceWindow . center")

frame_for_buttons = Frame(root)
frame_for_buttons.grid(row=0, column=0, padx=170)
frame_for_options = Frame(root)
frame_for_options.grid(row=1, column=0, pady=25)

cube_1 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_1),
)
cube_2 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_2),
)
cube_3 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_3),
)
cube_4 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_4),
)
cube_5 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_5),
)
cube_6 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_6),
)
cube_7 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_7),
)
cube_8 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_8),
)
cube_9 = Button(
    frame_for_buttons,
    text=" ",
    width=50,
    bg="black",
    fg="white",
    height=10,
    command=lambda: button_click(cube_9),
)

cube_1.grid(row=0, column=0)
cube_2.grid(row=0, column=1)
cube_3.grid(row=0, column=2)
cube_4.grid(row=1, column=0)
cube_5.grid(row=1, column=1)
cube_6.grid(row=1, column=2)
cube_7.grid(row=2, column=0)
cube_8.grid(row=2, column=1)
cube_9.grid(row=2, column=2)

label_for_result = Label(frame_for_options, font=("arial", 20))
label_for_result.grid(row=3, column=1)

label_for_score = Label(frame_for_options, text="Score", font=("arial", 20))
label_for_score.grid(row=4, column=1)

players_scores = Label(frame_for_options, text="0 - 0", font=("arial", 20))
players_scores.grid(row=5, column=1)

restart_button = ttk.Button(
    frame_for_options, text="Start Again", width=10, command=start_over
)
restart_button.grid(row=6, column=1)

reset_score_button = ttk.Button(
    frame_for_options, text="Reset Score", width=10, command=reset_score
)
reset_score_button.grid(row=7, column=1)

close_button = ttk.Button(frame_for_options, text="Quit", width=10, command=Close_app)
close_button.grid(row=8, column=1)

root.mainloop()
