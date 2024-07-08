from flask import Flask, render_template, jsonify, request
import tkinter as tk
from tkinter import colorchooser
import colorsys

app = Flask(__name__)

class ColorPicker:
    def __init__(self):
        self.color = (255, 255, 255)

    def choose_color(self, r, g, b):
        self.color = (r, g, b)
        return self.get_hsv()

    def get_hsv(self):
        r, g, b = self.color
        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
        h_deg, s_pct, v_pct = int(h * 360), int(s * 100), int(v * 100)
        return h_deg, s_pct, v_pct

color_picker = ColorPicker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choose_color', methods=['POST'])
def choose_color():
    r = int(request.form['red'])
    g = int(request.form['green'])
    b = int(request.form['blue'])
    h_deg, s_pct, v_pct = color_picker.choose_color(r, g, b)
    return jsonify({
        'hue': h_deg,
        'saturation': s_pct,
        'value': v_pct
    })

if __name__ == '__main__':
    app.run(debug=True)
