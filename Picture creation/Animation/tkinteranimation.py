import tkinter as tk

# Create the window
root = tk.Tk()
root.title("Moving Circle Animation")
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Create the circle
circle = canvas.create_oval(50, 50, 100, 100, fill="red")
dx, dy = 2, 2  # Velocity

def move():
    global dx, dy
    canvas.move(circle, dx, dy)
    pos = canvas.coords(circle)

    # Bounce off walls
    if pos[0] <= 0 or pos[2] >= 400:
        dx = -dx
    if pos[1] <= 0 or pos[3] >= 300:
        dy = -dy

    root.after(20, move)

# Start animation
move()
root.mainloop()