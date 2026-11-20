import tkinter as tk

current_color = "black"
line_width = 5
last_x = None
last_y = None

canvas = tk.Canvas(root, bg="white", cursor="pencil")

def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event_x, event_y, fill= current_color, width=line_width, )

def stop_drawing(event):
    global last_x, last_y
    last_x, last_y = None, None

def set_color(new_color):
    global current_color
    current_color = new_color

def set_width(new_width):
    global line_width
    line_width = new_width

def clear_canvas():
    canvas. delete("all")



root = tk.Tk()
root.title("My Python Paint")
root.geometry("800x600")


colors = ["blue", "green", "red", "yellow", "purple", "orange", "white"]        