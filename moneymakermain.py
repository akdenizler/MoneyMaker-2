import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("MONEYMAKER 2")
#scoreboard
score = 0

#gif stuff
gif_path = "making-money.gif"  
animated_frames = []

gif = Image.open(gif_path)
try:
    while True:
        animated_frames.append(ImageTk.PhotoImage(gif.copy()))
        gif.seek(gif.tell() + 1)  # Move to the next frame
except EOFError:
    pass  #End of GIF frames

# CYCLING RAINBOW TEXT
rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00","#00FFFF", "#0000FF", "#4B0082", "#8B00FF", "#FF00FF"]
color_index = 0  

# SCOREBOARD COLOR CYCLE
def cycle_colors():
    global color_index
    # UPDATE COLOR
    score_label.config(fg=rainbow_colors[color_index])
    # NEXT COLOR
    color_index = (color_index + 1) % len(rainbow_colors)
    # COLOR CHANGE TIMING
    root.after(100, cycle_colors)

# MONEY BUTTON
def handle_click():
    global score
    score += 1
    score_label.config(text=f"MONEYS MADE: {score}")

    # GREEN-UPON-CLICK
    button.itemconfig(button_oval, fill="#32CD32") 
    root.after(200, lambda: button.itemconfig(button_oval, fill="#FFD700"))

    play_gif()

# Function to play the GIF and pause on the last frame
def play_gif():
    gif_label.grid(row=2, column=0)  
    frame_index = 0

    def update_frame():
        nonlocal frame_index
        if frame_index < len(animated_frames):
            gif_label.config(image=animated_frames[frame_index])  # Update the frame
            frame_index += 1
            root.after(100, update_frame)  # Adjust timing based on GIF frame rate

    update_frame()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root, bg="white")
frame.grid(row=0, column=0, sticky="nsew")  
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

#SCOREBOARD
score_label = tk.Label(frame, text=f"MONEYS MADE: {score}", font=("Arial", 40), bg="white", fg=rainbow_colors[0])
score_label.grid(row=0, column=0, pady=20)

# ROUND MONEYBUTTON
button = tk.Canvas(frame, width=100, height=100, bg="white", highlightthickness=0)
button_oval = button.create_oval(5, 5, 95, 95, fill="#FFD700", outline="#FFA500", width=2)  # Gold round button
button.create_text(50, 50, text="$", font=("Arial", 24, "bold"), fill="white")

#BIND THE MONEYBUTTON
button.bind("<Button-1>", lambda event: handle_click())
button.grid(row=1, column=0, pady=20)

#gif handling
gif_label = tk.Label(frame, bg="white")
gif_label.grid(row=2, column=0, pady=20)

gif_label.config(image=animated_frames[0])

# RAINBOW SCOREBOARD CYCLE
cycle_colors()


root.mainloop()
