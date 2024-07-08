import tkinter as tk
from tkinter import colorchooser
import colorsys

class ColorPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker")
        
        # Initial color
        self.color = (255, 255, 255)
        
        # Create sliders for RGB values
        self.red_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Red", command=self.update_color)
        self.red_slider.pack()
        self.green_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=self.update_color)
        self.green_slider.pack()
        self.blue_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=self.update_color)
        self.blue_slider.pack()
        
        # Button to open color chooser
        self.color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()
        
        # Display area for selected color
        self.color_display = tk.Label(root, text="", bg="#ffffff", width=20, height=10)
        self.color_display.pack()
        
        # HSV display labels
        self.h_label = tk.Label(root, text="Hue: 0")
        self.h_label.pack()
        self.s_label = tk.Label(root, text="Saturation: 0")
        self.s_label.pack()
        self.v_label = tk.Label(root, text="Value: 0")
        self.v_label.pack()
        
        # Update the color display initially
        self.update_color_display()
    
    def update_color(self, event=None):
        # Get RGB values from sliders
        r = self.red_slider.get()
        g = self.green_slider.get()
        b = self.blue_slider.get()
        
        # Update the color
        self.color = (r, g, b)
        
        # Update the display area
        self.update_color_display()
    
    def choose_color(self):
        # Open color chooser dialog
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
        
        # Update the color display area
        self.color_display.config(bg=color_hex)
        
        # Convert RGB to HSV
        r_norm = r / 255.0
        g_norm = g / 255.0
        b_norm = b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
        
        # Convert HSV to percentage values
        h_deg = int(h * 360)
        s_pct = int(s * 100)
        v_pct = int(v * 100)
        
        # Update HSV labels
        self.h_label.config(text=f"Hue: {h_deg}")
        self.s_label.config(text=f"Saturation: {s_pct}%")
        self.v_label.config(text=f"Value: {v_pct}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPicker(root)
    root.mainloop()
