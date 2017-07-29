import tkinter


class Converter:
    """Temperature converter with GUI: converts temperature given by user
    from scale from_ to scale to using formula.
    """
    def __init__(self, master, from_, to, formula):
        """
        :param master: parent tkinter widget
        :param from_: str
        :param to: str
        :param formula: function
        """
        self.master = master
        self.from_ = from_
        self.to = to
        self.formula = formula
        # Variables for storing input and output
        self.temperature1 = tkinter.StringVar()
        self.temperature2 = tkinter.StringVar()

    def __str__(self):
        """Create string representation of conversion scales."""
        return self.from_ + ' to ' + self.to

    def run(self):
        """Run Converter GUI."""
        frame = tkinter.Frame(self.master, borderwidth=10)
        frame.pack()

        # Header
        tkinter.Label(frame, text=str(self)).pack()

        # Input view
        tkinter.Label(frame, text=f'Temperature in {self.from_}:').pack()
        tkinter.Entry(frame, width=30, textvar=self.temperature1).pack()

        # Output view
        tkinter.Label(frame, text=f'Temperature in {self.to}:').pack()
        tkinter.Label(frame, textvar=self.temperature2).pack()

        # Controller button
        tkinter.Button(frame, text='Convert', width=10,
                       command=self.get_result).pack()

    def get_result(self):
        """Store result of conversion."""
        try:
            degrees_to_convert = float(self.temperature1.get())
            self.temperature2.set(self.formula(degrees_to_convert))
        except ValueError:  # User hasn't passed any valid input
            self.temperature2.set('ENTER VALID TEMPERATURE')

    def reset(self):
        """Reset values of input and output variables."""
        self.temperature1.set('')
        self.temperature2.set('')


class Application:
    """Application with GUI offering multiple converters."""
    def __init__(self, master):
        """Create Application with parent tkinter widget master."""
        self.master = master
        self.converters_data = [
            ('Celsius', 'Fahrenheit', lambda t: t * 9 / 5 + 32),
            ('Celsius', 'Kelvin', lambda t: t + 273.15),
            ('Fahrenheit', 'Celsius', lambda t: (t - 32) * 5 / 9),
            ('Fahrenheit', 'Kelvin', lambda t: (t + 459.67) * 5 / 9),
            ('Kelvin', 'Celsius', lambda t: t - 273.15),
            ('Kelvin', 'Fahrenheit', lambda t: t * 9 / 5 - 459.67),
        ]
        # Frame for displaying converter chosen by user
        self.converter_frame = tkinter.Frame(self.master, borderwidth=10)

    def run_app(self):
        """Run application GUI."""
        frame = tkinter.Frame(self.master, borderwidth=10)
        frame.pack()

        # Header
        tkinter.Label(frame, text='Converters').grid(columnspan=2)

        # Converter choice buttons
        for i in range(len(self.converters_data)):
            from_, to, formula = self.converters_data[i]
            converter = Converter(self.converter_frame, from_, to, formula)
            tkinter.Button(frame, text=str(converter), width=20,
                           command=lambda c=converter:
                           self.run_converter(c)).grid(row=i//2 + 1, column=i%2)

    def run_converter(self, converter):
        """Run chosen converter in appropriate frame."""
        # If frame isn't packed or has been hidden, display it
        if not self.converter_frame.winfo_ismapped():
            self.converter_frame.pack()
        # If user switched converters without quitting, clear the frame.
        else:
            for widget in self.converter_frame.winfo_children():
                widget.destroy()
        # Run converter GUI.
        converter.run()
        # Create button for quitting the converter
        tkinter.Button(self.converter_frame, text='Quit', width=10,
                       command=lambda: self.quit_converter(converter)).pack()

    def quit_converter(self, converter):
        """Quit converter GUI."""
        # Clear converter data
        converter.reset()
        # Clear and hide the frame
        for widget in self.converter_frame.winfo_children():
            widget.destroy()  # Clear
        self.converter_frame.pack_forget()  # Hide

if __name__ == '__main__':
    window = tkinter.Tk()
    app = Application(window)
    app.run_app()
    window.mainloop()
