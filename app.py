import tkinter


class Converter:
    def __init__(self, from_, into, formula):
        """
        (Converter, str, str, function) -> NoneType
        Create converter from scale from_ into scale into using formula formula.
        """
        self.from_ = from_
        self.into = into
        self.formula = formula

    def convert(self, temperature):
        """
        (Converter, float) -> float
        Convert temperature degrees.
        """
        return self.formula(temperature)


class ConverterGUI:
    """GUI for Converter."""
    def __init__(self, master, converter):
        self.master = master
        self.converter = converter

        self.frame = tkinter.Frame(master, borderwidth=10)
        self.frame.pack()

        self.header1 = f'Temperature in {self.converter.from_}:'
        tkinter.Label(self.frame, text=self.header1).pack()

        # Input
        self.temp1 = tkinter.StringVar()
        tkinter.Entry(self.frame, width=30, textvar=self.temp1).pack()

        self.header2 = f'Temperature in {self.converter.into}:'
        tkinter.Label(self.frame, text=self.header2).pack()

        # Output
        self.temp2 = tkinter.StringVar()
        tkinter.Label(self.frame, textvar=self.temp2).pack()

        tkinter.Button(self.frame, text='Convert', width=10,
                       command=self.convert).pack()
        tkinter.Button(self.frame, text='Quit', width=10,
                       command=self.quit).pack()

    def convert(self):
        """Display the result of conversion."""
        try:
            self.temp2.set(self.converter.formula(float(self.temp1.get())))
        except ValueError:  # the user has given no or incorrect input
            self.temp2.set('ENTER CORRECT TEMPERATURE')

    def quit(self):
        """Clear and hide or destroy the master"""
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.master.pack_forget()
        except AttributeError:  # the master has no attribute pack_forget
            self.master.destroy()


class AppFrame:
    """The main frame for the converting application"""
    def __init__(self, master):
        self.master = master
        self.frame1 = tkinter.Frame(master, borderwidth=10)
        self.frame1.pack()
        self.frame2 = tkinter.Frame(master, borderwidth=10)

        self.converters_data = {
            ('Celsius', 'Fahrenheit'): lambda t: t*9/5 + 32,
            ('Celsius', 'Kelvin'): lambda t: t + 273.15,
            ('Fahrenheit', 'Celsius'): lambda t: (t-32) * 5/9,
            ('Fahrenheit', 'Kelvin'): lambda t: (t+459.67) * 5/9,
            ('Kelvin', 'Celsius'): lambda t: t - 273.15,
            ('Kelvin', 'Fahrenheit'): lambda t: t*9/5 - 459.67,
        }
        sorted_names = sorted(self.converters_data.keys())
        for i in range(len(sorted_names)):
            names_pair = sorted_names[i]
            converter = Converter(*names_pair, self.converters_data[names_pair])
            tkinter.Button(self.frame1, width=20,
                           text=converter.from_ + ' to ' + converter.into,
                           command=lambda c=converter:
                                self.run(c)).grid(row=i//2, column=i%2)

    def run(self, converter):
        # If no converter has been run yet or the user quit a previous converter
        if not self.frame2.winfo_ismapped():
            self.frame2.pack()
        # If the user switched converters without quitting
        else:
            for widget in self.frame2.winfo_children():
                widget.destroy()
        ConverterGUI(self.frame2, converter)


if __name__ == '__main__':
    window = tkinter.Tk()
    app = AppFrame(window)
    window.mainloop()
