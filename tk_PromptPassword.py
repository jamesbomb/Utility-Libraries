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
__name__ = "tk_PromptPassword"


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

    def __init__(self, title="TK Password Prompt"):
        """
        Class initialization.
        Window title can be customized while instantiating the class.
        If title not provided, a default title is shown
        """
        self.root = tk.Tk()
        self.root.title(title)  # The title of tkinter window is configurable
        self.root.minsize(width=300, height=125)
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
        password_lbl = tk.Label(self.root, text="Password", padx=2, pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        submit_button = tk.Button(self.root,
                                  text="Submit",
                                  command=self.submit_click, width=20, pady=5)

        password_lbl.grid(row=0, column=0, sticky="E")
        self.password_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=0, columnspan=2)

        # Bind enter key with button
        self.root.bind('<Return>', self.submit_click)

        # Have the focus set on password textbox
        self.password_entry.focus()

        self.root.mainloop()

        return self.password
