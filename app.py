import customtkinter
from tkinter import *
import tkinter as tk
import random
import tkinter.messagebox as msgbox


root = customtkinter.CTk()
root.title("Tic-Tac-Toe")

jugador_x = True
jugador_cpu = True

def disable_buttons():
    for button in button_list:
        button.configure(state="disabled")

def check_winner():
    # Comprobación de filas
    if button_1.cget("text") == button_2.cget("text") == button_3.cget("text") != " ":
        return button_1.cget("text")
    if button_4.cget("text") == button_5.cget("text") == button_6.cget("text") != " ":
        return button_4.cget("text")
    if button_7.cget("text") == button_8.cget("text") == button_9.cget("text") != " ":
        return button_7.cget("text")

    # Comprobación de columnas
    if button_1.cget("text") == button_4.cget("text") == button_7.cget("text") != " ":
        return button_1.cget("text")
    if button_2.cget("text") == button_5.cget("text") == button_8.cget("text") != " ":
        return button_2.cget("text")
    if button_3.cget("text") == button_6.cget("text") == button_9.cget("text") != " ":
        return button_3.cget("text")

    # Comprobación de diagonales
    if button_1.cget("text") == button_5.cget("text") == button_9.cget("text") != " ":
        return button_1.cget("text")
    if button_3.cget("text") == button_5.cget("text") == button_7.cget("text") != " ":
        return button_3.cget("text")
    
    if all(button.cget("text") != "" for button in button_list):
        msgbox.showinfo(f"Information", "Its a Draw \n Game close automatically in few seconds")
        disable_buttons()
        root.after(0, root.quit)

    return None

def on_button(button):
    if button.cget("text") != "":
        return
    else:
        button.configure(text="X")

    winner = check_winner()
    if winner:
        msgbox.showinfo(f"Congratulations", "Player wins! \n Game close automatically in few seconds")
        disable_buttons()
        root.after(0, root.quit)
    else:
        on_button_cpu()

def on_button_cpu():
    cpu = random.choice(button_list)
    while cpu.cget("text") != "":
        cpu = random.choice(button_list)
        button_list.remove(cpu)
    cpu.configure(text="O")

    winner = check_winner()
    if winner:
        msgbox.showinfo(f"Congratulations", " CPU wins! \n Game close automatically in few seconds")
        disable_buttons()
        root.after(0, root.quit)

        



title_frame = customtkinter.CTkFrame(root,fg_color="transparent")
title_frame.pack(pady=10)

customtkinter.CTkLabel(
    title_frame,
    text="PLAYER",
    font=("DefaultFont",16)
).grid()

body_frame = customtkinter.CTkFrame(
    root,
    fg_color="transparent"
)
body_frame.pack()

button_1 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_1)
)
button_2 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_2)
)
button_3 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_3)
)
button_4 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_4)
)
button_5 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_5)
)
button_6 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_6)
)
button_7 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_7)
)
button_8 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_8)
)
button_9 = customtkinter.CTkButton(
    body_frame,
    text="",
    fg_color=("#FCFBF9"),
    text_color="red",
    font=("DefaultFont",40),
    height=100,
    width=100,
    command=lambda: on_button(button_9)
)

button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

button_1.grid(column=0, row=0, padx=10, pady=10)
button_2.grid(column=1, row=0, padx=10, pady=10)
button_3.grid(column=2, row=0, padx=10, pady=10)
button_4.grid(column=0, row=1, padx=10, pady=10)
button_5.grid(column=1, row=1, padx=10, pady=10)
button_6.grid(column=2, row=1, padx=10, pady=10)
button_7.grid(column=0, row=2, padx=10, pady=10)
button_8.grid(column=1, row=2, padx=10, pady=10)
button_9.grid(column=2, row=2, padx=10, pady=10)





root.mainloop()