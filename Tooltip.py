# Tooltip.py holds a class that adds a wrapper to a widget that enables tooltips.

import tkinter as tk

class TooltipManager:
    def __init__(self, canvas: tk.Canvas):
        self.widget_texts = {}
        self.text_ids = {}
        self.canvas = canvas

    def enter(self, widget:tk.Widget):
        self.text_ids[widget] = self.canvas.create_text(widget.winfo_x()+widget.winfo_width()+5,
                                                        widget.winfo_y()-8,
                                                        text=self.widget_texts[widget])

    def leave(self, widget:tk.Widget):
        self.canvas.delete(self.text_ids[widget])

    def make_tooltip(self, widget: tk.Widget, text:str) -> None:
        self.widget_texts[widget] = text
        widget.bind("<Enter>", lambda _: self.enter(widget))
        widget.bind("<Leave>", lambda _: self.leave(widget))