from tkinter import *
import requests
root = Tk()

def get_information():
    pokemon = pokemonField.get()

    url = 'https://pokeapi.co/api/v2/pokemon'
    result = requests.get(f"{url}/{pokemon}")
    information = result.json()
    info['text'] = f'Abilities: {", ".join([ab["ability"]["name"] for ab in information["abilities"]])}'

root['bg'] = 'pink1'
root.title('Информация о покемонах')
root.geometry('500x500')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='PaleVioletRed1', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='PaleVioletRed1', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

pokemonField = Entry(frame_top, bg='lavender blush', font='Courier 30 bold')
pokemonField.pack()

btn = Button(frame_top, text=' Information about pokemon ', command=get_information, font='Courier 15 bold', bg='lavender blush')
btn.pack()

info = Label(frame_bottom, bg='lavender blush', font='Courier 12 bold')
info.pack()

root.mainloop()