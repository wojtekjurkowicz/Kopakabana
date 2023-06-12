from tkinter import Tk, Button, Label


clicks = 0
def click_action(button):
    global clicks
    clicks += 1
    if clicks == 10:
        button.destroy()
        label = Label(root, text="Jesteś gejem", font=50)
        label.pack()
    button.config(text=f"Ostrzegam po raz {clicks}")

root = Tk()
root.geometry("200x200")

click_button = Button(root, text="NIE WCISKAJ TEGO !!!!", width=20) # kolejny argument command=click_action
click_button.pack()

click_button.config(command=lambda: click_action(click_button)) # config do modyfikacji w czasie dzialania aplikacji

root.mainloop()