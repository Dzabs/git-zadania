import tkinter as tk



gui = tk.Tk()
gui.geometry("800x500")
gui.title("Baza adresowa")

label = tk.Label(gui, text="Wprowadź dane adresowe poniżej.").place(x=5, y=5)

# name_frame = tk.Frame(gui)
name_label = tk.Label(gui, text= "Wprowadź imie i nazwisko: ")
name_entry = tk.Entry(gui)
name_label.place(x=5, y=35)
name_entry.place(x=230, y=35)
# name_frame.pack()

# ulica_frame = tk.Frame(gui)
ulica_label = tk.Label(gui, text= "Wprowadź ulicę i adres domowy : ")
ulica_entry = tk.Entry(gui)
ulica_label.place(x=5, y=65)
ulica_entry.place(x=230, y=65)
# ulica_frame.pack()

# kod_frame = tk.Frame(gui)
kod_label = tk.Label(gui, text= "Wprowadź kod pocztowy i miasto : ")
kod_entry = tk.Entry(gui)
kod_label.place(x=5, y=95)
kod_entry.place(x=230, y=95)
# kod_frame.pack()




def add_dane():
    name=name_entry.get()
    ulica=ulica_entry.get()
    kod=kod_entry.get()
    if name and ulica and kod:
        with open("my_file.txt", "a") as f:
            f.write("\n" + "1: " + name + ", " + "2: " + ulica + ", " + "3: " + kod)
    else:
        labelerror = tk.Label(gui, text="Wprowadź wszystkie dane.").place(x=5, y=150)


button = tk.Button(gui, text="Zapisz", command = add_dane)
button.place(x=230, y=125)

print("Mati to ziomal")


print("Rafal to ziomal")



