import tkinter as tk
import functions as f

# ---------- window ----------
window = tk.Tk()
window.title("Tkinter Calculator")
window.configure(bg="#222222")
window.resizable(False, False)

# ---------- display ----------
display = tk.Entry(
    window,
    font=("Arial", 20),
    bd=5,
    relief=tk.RIDGE,
    width=17,
    justify="right",
)
display.grid(row=0, column=0, columnspan=4, pady=10)

# ---------- button layout & callbacks ----------
#      text, row, col,     colspan (optional)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("√", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("⌫", 5, 1), ("=", 5, 2, 2),  # "⌫" is new here
]

# basic colour palette
COLORS = {
    "digit":  "#4e4e4e",
    "op":     "#8a2be2",
    "equal":  "#32cd32",
    "clear":  "#d32f2f",
    "active": "#555555",
}

for spec in buttons:
    text, r, c, *rest = spec
    colspan = rest[0] if rest else 1

    # decide colour & command
    if text.isdigit() or text == ".":
        bg = COLORS["digit"]
        cmd = lambda t=text: f.press(t, display)
    elif text == "C":
        bg = COLORS["clear"]
        cmd = lambda: f.clear(display)
    elif text == "⌫":
        bg = COLORS["clear"]
        cmd = lambda: f.backspace(display)
    elif text == "=":
        bg = COLORS["equal"]
        cmd = lambda: f.equal(display)
    elif text == "√":
        bg = COLORS["op"]
        cmd = lambda: f.sqrt(display)
    else:  # + - * /
        bg = COLORS["op"]
        cmd = lambda t=text: f.press(t, display)

    btn = tk.Button(
        window, text=text, command=cmd,
        bg=bg, fg="white", activebackground=COLORS["active"],
        bd=0, font=("Arial", 16), width=5, height=2,
    )
    btn.grid(row=r, column=c, columnspan=colspan, sticky="nsew", padx=2, pady=2)

# give every row/column equal weight so the grid expands nicely
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# ---------- start ----------
window.mainloop()

