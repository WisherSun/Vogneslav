import customtkinter
import gpt
from PIL import Image
def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("400x150")
button_image= customtkinter.CTkImage(Image.open("a.png"), size=(26,26))
button = customtkinter.CTkButton(app, text="my button", command=button_callback, image= button_image)
button.pack(padx=20, pady=20)
textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0", "")
textbox.pack(padx=20, pady=20)
app.mainloop()