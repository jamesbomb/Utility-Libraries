# tk_PromptPassword.py
# Python 2.7.6

"""
Reusable library which pops tkinter window to prompt password
"""

import Tkinter as tk
import tkMessageBox as tkm  # To show warning/ error messages
import logging

__author__ = "Vinoth Subramanian"
__doc__ = "Reusable library which pops tkinter window to prompt password"


""" Basic logging config
Since this is a library, logging propoerties are not configured
http://docs.python-guide.org/en/latest/writing/logging/#logging-in-a-library

A null handler ignores all logging by default, unless logged in client
"""
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class prompt_password:
    """
    Use tkinter to get password
    """

    def __init__(self, title="TK Password Prompt", text="Password"):
        """
        Class initialization.
        Window title can be customized while instantiating the class.
        If title not provided, a default title is shown
        If the prompt text is not provided, a default text is shown
        """
        self.root = tk.Tk()
        self.root.title(title)  # The title of tkinter window is configurable
        self.root.minsize(width=400, height=100)

        # Define the frame to contain label and entry widget
        self.messageFrame = tk.Frame(master=self.root)
        self.messageFrame.grid(padx=2, pady=2)

        # Define the frame for submit button
        self.buttonFrame = tk.Frame(master=self.root)
        self.buttonFrame.grid(padx=10, pady=2)

        self.text = text
        self.password = None

    def submit_click(self, event=None):
        """
        Submit button click event handler
        event - parameter to bind with '<Return>'
        When the button is clicked instead of Enter, then event wont be passed
        Set default to None to cover this case
        """
        pwd = self.password_entry.get()

        if (pwd):
            self.password = pwd
            # Close window once processing complete
            self.root.destroy()
        else:
            tkm.showerror(
                title="Error", message="Mandatory fields cannot be empty")

    def get_password(self):
        """
        Tkinter UI to prompt user for password
        """
        password_lbl = tk.Label(self.messageFrame,
                                text=self.text,
                                padx=5, pady=10)
        self.password_entry = tk.Entry(self.messageFrame,
                                       show="*")
        submit_button = tk.Button(self.buttonFrame,
                                  text="Submit",
                                  padx=10, pady=5,
                                  width=50,
                                  command=self.submit_click)

        password_lbl.grid(row=0, column=0)
        self.password_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=0, columnspan=2)

        # Bind enter key with button
        self.root.bind('<Return>', self.submit_click)

        # Have the focus set on password textbox
        self.password_entry.focus()

        self.root.mainloop()

        return self.password


if __name__ == "__main__":
    """ To invoke the library directly"""
    ui = prompt_password()
    ui.get_password()
