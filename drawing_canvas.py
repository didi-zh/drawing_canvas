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

def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y,
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event_x, event_y, fill= current_color, width=line_width, )