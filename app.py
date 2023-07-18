import datetime
import time

from textual import on
from textual.app import App
from textual.widget import Widget
from textual.reactive import reactive
from textual.containers import Horizontal
from textual.widgets import Button, Header, Input, Label, Footer
from textual.screen import ModalScreen


class TodoItem(Widget):
    DEFAULT_CSS = """
    TodoItem {
        height: 1;
    }
    """
    def __init__(self, label):
        super().__init__()
        self.label = label

    def compose(self):
        with Horizontal():
            yield Label(f"Date: dd/mm/YYYY - ")
            yield Label("Dummy description")

        

class TodoModal(ModalScreen):
    DEFAULT_CSS = """
    TodoModal {
        align: center middle;
    }
    """
    def compose(self):
        yield TodoItem("New todo")

        with Horizontal():
            yield Button("Dismiss", id="dismiss")
            yield Button("Edit", id="edit")

    @on(Button.Pressed, "#dismiss")
    def dismiss_modal(self):
        self.dismiss()

    @on(Button.Pressed, "#edit")
    def edit(self):
        pass

    

class TodoApp(App):
    BINDINGS = [
        ("n", "new_item", "New TODO item"),
    ]
    counter = reactive(0)

    def compose(self):
        self.label = Label()
        yield Header(show_clock=True)
        yield self.label
        yield Button("Show Item", id="show-modal")
        yield Footer()

    @on(Button.Pressed, "#show-modal")
    def show_modal(self):
        self.push_screen(TodoModal())


    def watch_counter(self, new_counter_value):
        self.label.update(str(new_counter_value))

    

TodoApp().run()
