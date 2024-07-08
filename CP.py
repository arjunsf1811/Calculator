import tkinter as tk
from tkinter import colorchooser
import colorsys

class ColorPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker")
        self.root.geometry("300x400")
        self.color = (255, 255, 255)

        self.setup_sliders()
        self.setup_buttons()
        self.setup_display()
        self.update_color_display()

    def setup_sliders(self):
        slider_frame = tk.Frame(self.root, padx=10, pady=10)
        slider_frame.pack()

        self.red_slider = tk.Scale(slider_frame, from_=0, to=255, orient=tk.HORIZONTAL, label="Red", command=self.update_color, length=250, fg="red", font=("Helvetica", 12))
        self.red_slider.pack(pady=5)
        self.green_slider = tk.Scale(slider_frame, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=self.update_color, length=250, fg="green", font=("Helvetica", 12))
        self.green_slider.pack(pady=5)
        self.blue_slider = tk.Scale(slider_frame, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=self.update_color, length=250, fg="blue", font=("Helvetica", 12))
        self.blue_slider.pack(pady=5)

    def setup_buttons(self):
        button_frame = tk.Frame(self.root, padx=10, pady=10)
        button_frame.pack()

        self.color_button = tk.Button(button_frame, text="Choose Color", command=self.choose_color, font=("Helvetica", 12), bg="#ddd", width=15)
        self.color_button.pack(pady=5)

    def setup_display(self):
        display_frame = tk.Frame(self.root, padx=10, pady=10)
        display_frame.pack()

        self.color_display = tk.Label(display_frame, text="", bg="#ffffff", width=20, height=2, relief="solid")
        self.color_display.pack(pady=10)

        self.h_label = tk.Label(display_frame, text="Hue: 0", font=("Helvetica", 12))
        self.h_label.pack(pady=2)
        self.s_label = tk.Label(display_frame, text="Saturation: 0", font=("Helvetica", 12))
        self.s_label.pack(pady=2)
        self.v_label = tk.Label(display_frame, text="Value: 0", font=("Helvetica", 12))
        self.v_label.pack(pady=2)

    def update_color(self, event=None):
        r = self.red_slider.get()
        g = self.green_slider.get()
        b = self.blue_slider.get()
        self.color = (r, g, b)
        self.update_color_display()

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Color")[0]
        if color_code:
            r, g, b = map(int, color_code)
            self.red_slider.set(r)
            self.green_slider.set(g)
            self.blue_slider.set(b)
            self.update_color()

    def update_color_display(self):
        r, g, b = self.color
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        self.color_display.config(bg=color_hex)

        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
        h_deg, s_pct, v_pct = int(h * 360), int(s * 100), int(v * 100)

        self.h_label.config(text=f"Hue: {h_deg}")
        self.s_label.config(text=f"Saturation: {s_pct}%")
        self.v_label.config(text=f"Value: {v_pct}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPicker(root)
    root.mainloop()
