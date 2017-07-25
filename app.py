import tkinter


class Converter:
    """A temperature converter GUI."""
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame(self.master, borderwidth=10)
        self.frame.pack()

        self.header1 = tkinter.StringVar()
        self.header1.set('Temperature in ')
        tkinter.Label(self.frame, textvar=self.header1).pack()
        self.header2 = tkinter.StringVar()
        self.header2.set('Temperature in ')

        # Input
        self.temp1 = tkinter.StringVar()
        tkinter.Entry(self.frame, width=30, textvar=self.temp1).pack()

        tkinter.Label(self.frame, textvar=self.header2).pack()
        # Output
        self.temp2 = tkinter.StringVar()
        tkinter.Label(self.frame, textvar=self.temp2).pack()

        tkinter.Button(self.frame, text='Convert', width=10,
                       command=self.convert).pack()
        tkinter.Button(self.frame, text='Quit', width=10,
                       command=self.quit).pack()

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

    def quit(self):
        """Clear and hide the parent frame."""
        for widget in self.master.winfo_children():
            widget.destroy()
        self.master.pack_forget()

class CelsiusToFahrenheit(Converter):
    """A Converter from Celsius to Fahrenheit."""
    def __init__(self,  master):
        super().__init__(master)
        self.header1.set(self.header1.get() + 'Celsius:')
        self.header2.set(self.header2.get() + 'Fahrenheit:')

    def converter(self):
        self.temp2.set(float(self.temp1.get()) * 9/5 + 32)


class CelsiusToKelvin(Converter):
    """A converter from Celsius to Kelvin."""
    def __init__(self, master):
        super().__init__(master)
        self.header1.set(self.header1.get() + 'Celsius:')
        self.header2.set(self.header2.get() + 'Kelvin:')

    def converter(self):
        self.temp2.set(float(self.temp1.get()) + 273.15)


class FahrenheitToCelsius(Converter):
    """A Converter from Fahrenheit to Celsius."""
    def __init__(self, master):
        super().__init__(master)
        self.header1.set(self.header1.get() + 'Fahrenheit:')
        self.header2.set(self.header2.get() + 'Celsius:')

    def converter(self):
        self.temp2.set((float(self.temp1.get()) - 32) * 5/9)


class FahrenheitToKelvin(Converter):
    """A Converter from Fahrenheit to Kelvin."""
    def __init__(self, master):
        super().__init__(master)
        self.header1.set(self.header1.get() + 'Fahrenheit:')
        self.header2.set(self.header2.get() + 'Kelvin:')

    def converter(self):
        self.temp2.set((float(self.temp1.get()) + 459.67) * 5/9)


class KelvinToCelsius(Converter):
    """A converter from Kelvin to Celsius."""
    def __init__(self, master):
        super().__init__(master)
        self.header1.set(self.header1.get() + 'Kelvin:')
        self.header2.set(self.header2.get() + 'Celsius:')

    def converter(self):
        self.temp2.set(float(self.temp1.get()) - 273.15)

class KelvinToFahrenheit(Converter):
    """A converter from Kelvin to Fahrenheit."""
    def __init__(self, master):
        super().__init__(master)
        self.header1.set(self.header1.get() + 'Kelvin:')
        self.header2.set(self.header2.get() + 'Fahrenheit:')

    def converter(self):
        self.temp2.set(float(self.temp1.get()) * 9/5 - 459.67)


class AppFrame:
    """The main application frame."""
    def __init__(self, master):
        self.master = master
        self.frame1 = tkinter.Frame(self.master, borderwidth=10)
        self.frame1.pack()
        self.frame2 = tkinter.Frame(self.master)

        self.converters = {
            'Celsius To Fahrenheit': CelsiusToFahrenheit,
            'Celsius To Kelvin': CelsiusToKelvin,
            'Fahrenheit To Celsius': FahrenheitToCelsius,
            'Fahrenheit To Kelvin': FahrenheitToKelvin,
            'Kelvin To Celsius': KelvinToCelsius,
            'Kelvin To Fahrenheit': KelvinToFahrenheit,
        }
        # Arrange buttons in alphabetical order
        sorted_names = sorted(self.converters.keys())
        for i in range(len(sorted_names)):
            tkinter.Button(
                self.frame1, text=sorted_names[i], width=20,
                command=lambda c=self.converters[sorted_names[i]]:
                    self.run(c)).grid(row=i//2, column=i%2)

    def run(self, converter):
        # If user has switched converters without closing the frame, clear it
        for widget in self.frame2.winfo_children():
            widget.destroy()

        if not self.frame2.winfo_ismapped():  # the frame isn't packed
            self.frame2.pack()
        converter(self.frame2)


if __name__ == '__main__':
    window = tkinter.Tk()
    app = AppFrame(window)
    window.mainloop()
