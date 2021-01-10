#importing the libraries required
import requests
import tkinter as tk
from bs4 import BeautifulSoup

root = tk.Tk()

#This method is used to set the dimensions of the Tkinter window and is used to set the position of the main window on the user’s desktop.
root.geometry("300x300")

# Setting the title for the tkinter window
root.title("Temprature Scrapper")

# Setting the background of the tkinter window
root.config(bg = "wheat")

def check():
    city = y.get()
    search = f"Weather in {city}"


    #URL
    url = f"https://www.google.com/search?&q={search}"

    # Sending HTTP requests
    req = requests.get(url)

    # Pulling HTTP data from internet
    soup = BeautifulSoup(req.text, "html.parser")

    # Finding temperature in Celcius
    temp = soup.find("div", class_ = "BNeawe").text
    g = f"Temperature in {city} is {temp}"
    l2.configure(text = g)


y = tk.StringVar()

l1 = tk.Label(root, text = "Enter city : ")
l1.place(x = 10, y = 5)

e1 = tk.Entry(root, textvariable = y)
e1.place(x = 10, y = 35, height = 35, width = 180)

l2 = tk.Label(root, fg = "black")
l2.place(x = 10, y = 105)

b = tk.Button(root, text = "Check", command = check)
b.place(x = 10, y = 75)

root.mainloop()

