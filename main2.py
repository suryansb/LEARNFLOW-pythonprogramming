import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Create variables for user input
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()

        # Set default values
        self.amount_var.set(1.0)
        self.from_currency_var.set("USD")
        self.to_currency_var.set("EUR")

        # Create labels
        tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(root, text="Converted Amount:").grid(row=4, column=0, padx=10, pady=10)

        # Create entry widgets
        self.amount_entry = tk.Entry(root, textvariable=self.amount_var)
        self.from_currency_dropdown = tk.OptionMenu(root, self.from_currency_var, "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "INR", "CNY", "NZD", "SGD", "KRW", "THB", "IDR", "PHP")
        self.to_currency_dropdown = tk.OptionMenu(root, self.to_currency_var, "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "INR", "CNY", "NZD", "SGD", "KRW", "THB", "IDR", "PHP")
        self.converted_amount_label = tk.Label(root, text="")

        # Create button for conversion
        convert_button = tk.Button(root, text="Convert", command=self.convert_currency)

        # Grid layout
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)
        self.from_currency_dropdown.grid(row=1, column=1, padx=10, pady=10)
        self.to_currency_dropdown.grid(row=2, column=1, padx=10, pady=10)
        convert_button.grid(row=3, column=1, padx=10, pady=10)
        self.converted_amount_label.grid(row=4, column=1, padx=10, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get().upper()
            to_currency = self.to_currency_var.get().upper()

            # Use forex_python library to get real-time exchange rates
            c = CurrencyRates()
            exchange_rate = c.get_rate(from_currency, to_currency)
            converted_amount = round(amount * exchange_rate, 2)

            result_text = f"{amount} {from_currency} = {converted_amount} {to_currency}"
            self.converted_amount_label.config(text=result_text)

        except ValueError:
            self.converted_amount_label.config(text="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
