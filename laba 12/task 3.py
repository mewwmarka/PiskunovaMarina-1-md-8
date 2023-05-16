from tkinter import*
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []



Cafe1 = IceCreamStand('Ice', 'IceCream')
Cafe1.flavors.append("Ванильное")
Cafe1.flavors.append("Шоколадное")
Cafe1.flavors.append("Мятное")
root=Tk()
root['bg'] = 'light blue'
root.title('Кафе-мороженое')
root.geometry('500x500')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=500, width=500)
canvas.pack()
frame = Frame(root, bg='light yellow')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
title = Label(frame, text='Мороженое', bg="light yellow", font="Courier 40 bold")
title.pack()
def btn_click():
    print(f"Виды мороженого: {', '.join(Cafe1.flavors)}" )

btn = Button(frame, text='Покажи сорта мороженного!', bg = "light green" , font="Courier 15 bold", command=btn_click)

btn.pack()

root.mainloop()