import tkinter as tk

class TooltipManager:
    def __init__(self, canvas: tk.Canvas):
        """
        Object manages tooltips and wraps widgets with tooltips using make_tooltip.

        Args:
            canvas: Main canvas that holds the widget and will show the tooltip.
        """
        self.widget_texts = {} # Dictionary holding {widget: assigned text}
        self.text_id = 0 # ID of current text being shown.
        self.canvas = canvas # Display canvas.
        self.showing = "" # ID of current action.

    def _enter(self, widget:tk.Widget) -> None:
        """
        Helper function. When mouse enters, calls _show after a second.

        Args:
            widget (tk.Widget): Widget that mouse has entered.
        """
        self.showing = self.canvas.after(1000, self._show, widget)

    def _show(self, widget:tk.Widget) -> None:
        """
        Helper function. Shows the tooltip.

        Args:
            widget (tk.Widget): Widget that's tooltip is being shown.
        """
        self.text_id = self.canvas.create_text(widget.winfo_x()+widget.winfo_width()+5,
                                                        widget.winfo_y()-8,
                                                        text=self.widget_texts[widget])

    def _leave(self):
        """
        Helper function. Cancels the show if mouse leaves, or deletes the text if already shown.
        """
        if self.text_id:
            self.canvas.delete(self.text_id)
            self.text_id = 0
        else:
            self.canvas.after_cancel(self.showing)


    def make_tooltip(self, widget: tk.Widget, text:str) -> None:
        """
        Gives a widget a tooltip.

        Args:
            widget (tk.Widget): TK widget being assigned the tooltip.
            text (str): Text tooltip that is shown.
        """
        self.widget_texts[widget] = text
        widget.bind("<Enter>", lambda _: self._enter(widget))
        widget.bind("<Leave>", lambda _: self._leave())