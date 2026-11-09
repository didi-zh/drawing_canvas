import tkinter as tk

current_color = "black"
line_width = 5
last_x = None
last_y = None


root = tk.Tk()
root.title("My Python Paint")
root.geometry("800x600")

colors = ["blue", "green", "red", "yellow", "purple", "orange", "white"]


canvas = tk.Canvas(root, bg="white", cursor="pencil")