import tkinter as tk

root = tk.Tk()
root.title("Bouncing Burger")
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()


layer_colors = ["#F4C28D", "#FF4C5B", "#E0CFCF", "#A87C5F", "#F4C28D"]
layer_labels = ["", "", "MICHELANGELO TESTIGO", "", ""]
layer_height = 20
layer_width = 100


x, y = 250, 150
burger_tag = "burger"


for i, (color, label) in enumerate(zip(layer_colors, layer_labels)):
    rect = canvas.create_rectangle(
        x, y + i * layer_height,
        x + layer_width, y + (i + 1) * layer_height,
        fill=color, outline="", tags=burger_tag
    )
    if label:
        canvas.create_text(
            x + layer_width / 2, y + i * layer_height + 10,
            text=label, font=("Helvetica", 10, "bold"),
            tags=burger_tag
        )


dx, dy = 2, 2
running = True

def move_burger():
    global dx, dy
    if running:
        canvas.move(burger_tag, dx, dy)
        x1, y1, x2, y2 = canvas.bbox(burger_tag)

        
        if x1 <= 0 or x2 >= 600:
            dx *= -1
        if y1 <= 0 or y2 >= 400:
            dy *= -1

        root.after(20, move_burger)

def stop(event):
    global running
    running = False

root.bind("<Key>", stop)
move_burger()
root.mainloop()
