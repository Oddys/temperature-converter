import tkinter


class Converter:
    """A temperature converter GUI."""
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame(self.master, borderwidth=10)
        self.frame.pack()

        self.header = tkinter.StringVar()
        self.header.set('Temperature in ')
        tkinter.Label(self.frame, textvar=self.header).pack()

        # Input
        self.temp1 = tkinter.StringVar()
        tkinter.Entry(self.frame, width=30, textvar=self.temp1).pack()

        # Output
        self.temp2 = tkinter.StringVar()
        tkinter.Label(self.frame, textvar=self.temp2).pack()

        tkinter.Button(self.frame, text='Convert', command=self.convert).pack()
        tkinter.Button(self.frame, text='Quit',
                       command=self.master.destroy).pack()

    def converter(self):
        """Convert temperature from one scale (stored in self.temp1) to
        the other and store the result in self.temp2.
        """
        pass

    def convert(self):
        """Handle the case when the user gave no input."""
        try:
            self.converter()
        except ValueError:
            self.temp2.set('ENTER YOUR TEMPERATURE')


class FahrenheitToCelsius(Converter):
    """A Converter from Fahrenheit to Celsius."""
    def __init__(self, master):
        super().__init__(master)
        self.header.set(self.header.get() + 'Fahrenheit')

    def converter(self):
        self.temp2.set((float(self.temp1.get()) - 32) * 5 / 9)


class CelsiusToFahrenheit(Converter):
    """A Converter from Celsius to Fahrenheit."""
    def __init__(self,  master):
        super().__init__(master)
        self.header.set(self.header.get() + 'Celsius')

    def converter(self):
        self.temp2.set(float(self.temp1.get()) * 9 / 5 + 32)
