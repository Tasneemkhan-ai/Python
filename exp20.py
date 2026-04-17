#Aim:GUI for developing conversion utilities
#Name:Khan Tasneem
#Date:17-04-2026
import tkinter as tk

def btnHandler():
    try:
        value = float(inputValue.get())
        choice = option.get()

        if choice == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            output.config(text="Result: " + str(result) + " °F")

        elif choice == "Rupees to Dollars":
            result = value / 83
            output.config(text="Result: $" + str(round(result, 2)))

        elif choice == "Inches to Feet":
            result = value / 12
            output.config(text="Result: " + str(result) + " ft")

    except:
        output.config(text="Enter valid number!")

# window
root = tk.Tk()
root.title("Unit Converter App")
root.geometry("700x500")

# title
tk.Label(root, text="Enter Value").pack()

# input
tk.Label(root, text="Enter Value").pack()
inputValue = tk.Entry(root)
inputValue.pack(pady=5)

# dropdown menu
option = tk.StringVar()
option.set("Celsius to Fahrenheit")

menu = tk.OptionMenu(root, option,
                     "Celsius to Fahrenheit",
                     "Rupees to Dollars",
                     "Inches to Feet")

menu.pack(pady=10)

# button
tk.Button(root, text="Convert", command=btnHandler).pack(pady=10)

# output
output = tk.Label(root, text="Result will appear here")
output.pack(pady=10)

# run
root.mainloop()
