import tkinter as tk
from atom import AtomList
from meny_window import MenyFrame
import question_window as q_w


class MainFrame(tk.Tk):
    def __init__(self):
        """Initializes window
        """
        super().__init__()

        self.a_list = AtomList()
        self.title("Eriks atomspel")

        meny_buttons = MenyFrame(self, self.a_list)
        meny_buttons.grid(row=0, column=0, padx=30, pady=30)

        self.current_frame = tk.Label(
            self, text="Periodiska System Spelet \n Atomer är supercoola!", font=("Futura Heavy BQ", 90))
        self.current_frame.grid(row=0, column=1, padx=0, pady=0)

        self.mainloop()

    def display_frame(self, frame):
        """Displays frame, destroys previous

        Args:
            frame (tk.Frame): frame to be displayed
        """
        self.current_frame.destroy()
        self.current_frame = frame
        self.current_frame.grid(row=0, column=1, padx=0, pady=0)


if __name__ == '__main__':
    MainFrame()
