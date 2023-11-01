import tkinter as tk
from tkinter import filedialog

class MorseConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Kodu Dönüştürücü")

        self.label = tk.Label(root, text="Metin veya Morse kodu girin:", font=("Arial", 14))
        self.label.pack()

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.button_to_morse = tk.Button(self.button_frame, text="Metni Morse Koda Dönüştür", font=("Arial", 12), command=self.convert_to_morse)
        self.button_to_morse.pack(side="left", padx=10)

        self.button_to_text = tk.Button(self.button_frame, text="Morse Kodunu Metne Dönüştür", font=("Arial", 12), command=self.convert_to_text)
        self.button_to_text.pack(side="left", padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="center")
        self.result_label.pack()

        self.place_label = tk.Label(root, text="Sonuç:", font=("Arial", 12))
        self.place_label.pack()

        self.copy_button = tk.Button(root, text="Sonucu Kopyala", font=("Arial", 12), command=self.copy_result)
        self.copy_button.pack()

        self.save_button = tk.Button(root, text="Sonucu Kaydet", font=("Arial", 12), command=self.save_result)
        self.save_button.pack()

        self.select_file_button = tk.Button(root, text="Dosya Seç", font=("Arial", 12), command=self.select_file)
        self.select_file_button.pack()

        self.symbols_to_morse = {
            "a": ".-", "b": "-...", "c": "-.-.", "ç": "-.-..", "d": "-..", "e": ".",
            "f": "..-.", "g": "--.", "ğ": "--.", "h": "....", "ı": "..", "i": "..",
            "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
            "ö": "---.", "p": ".--.", "r": ".-.", "s": "...", "ş": "----", "t": "-",
            "u": "..-", "ü": "..--", "v": "...-", "y": "-.--", "z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
            "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        }

    def convert_to_morse(self):
        user_input = self.entry.get().lower()
        result = self.text_to_morse_converter(user_input)
        self.result_label.config(text=result)

    def convert_to_text(self):
        user_input = self.entry.get()
        result = self.morse_to_text_converter(user_input)
        self.result_label.config(text=result)

    def text_to_morse_converter(self, text):
        morse_code = []
        for char in text:
            if char == ' ':
                morse_code.append(' ')
            elif char in self.symbols_to_morse:
                morse_code.append(self.symbols_to_morse[char])
        return ' '.join(morse_code)

    def morse_to_text_converter(self, morse_code):
        morse_to_text = {v: k for k, v in self.symbols_to_morse.items()}
        words = morse_code.split("  ")
        text = ""
        for word in words:
            letters = word.split(" ")
            for letter in letters:
                if letter in morse_to_text:
                    text += morse_to_text[letter]
            text += " "
        return text.strip()

    def copy_result(self):
        result = self.result_label.cget("text")
        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        self.root.update()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.entry.delete(0, tk.END)
                self.entry.insert(0, content)


    def save_result(self):
        result = self.result_label.cget("text")
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(result)


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseConverterApp(root)
    # root.geometry("600x500")
    root.mainloop()
