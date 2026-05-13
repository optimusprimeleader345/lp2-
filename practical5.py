from tkinter import *

def send():
    msg = e.get().lower()
    chat.insert(END, "You: " + msg + "\n")

    if msg in ["hi", "hello"]:
        reply = "Hello! How can I help you?"
    elif "name" in msg:
        reply = "My name is CustomerBot."
    elif "product" in msg:
        reply = "We provide many products online."
    elif "price" in msg:
        reply = "Please check our website for prices."
    elif "order" in msg:
        reply = "Your order will arrive in 3-5 days."
    elif "bye" in msg:
        reply = "Thank you! Visit again."
    else:
        reply = "Sorry, I didn't understand."

    chat.insert(END, "Bot: " + reply + "\n\n")
    e.delete(0, END)

root = Tk()
root.title("Chatbot")
root.geometry("500x500")

chat = Text(root, font=("Arial", 12))
chat.pack(fill=BOTH, expand=True)

e = Entry(root, font=("Arial", 12))
e.pack(fill=X)

Button(root, text="Send", command=send).pack()

root.mainloop()