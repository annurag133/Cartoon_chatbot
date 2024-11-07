import tkinter as tk
from tkinter import simpledialog

class CartoonChatbot:
    def __init__(self):
        self.responses = {
            "doraemon": "Doraemon is a Japanese anime character known for his futuristic gadgets and friendship with Nobita.",
            "shizuka": "Shizuka is a character in the anime Doraemon. She is Nobita's best friend and a gentle, kind-hearted girl.",
            "gian": "Gian is a character in the anime Doraemon. He is very powerful and skilled in baseball.",
            "sunio": "Sunio is a character in the anime Doraemon. Gian and Sunio are best friends.",
            "dekisuki": "Dekisuki is a character in the anime Doraemon. He is very intelligent and excels in his studies.",
            "nobita": "Nobita is a clumsy, lazy character in Doraemon who often gets into trouble and relies on Doraemon for help.",
            "sinchan": "Shin-chan is a Japanese manga series that made its first appearance in 1990. His father's name is Harry."
        }
        
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        character = self._extract_character(user_input)
        return self.responses.get(character, "I'm sorry i didn't get your point,i am in training Period can you please imporve your prompt and ask me again.")
    
    def _extract_character(self, user_input):
        for character in self.responses.keys():
            if character in user_input:
                return character
        return None

class ChatbotGUI:
    def __init__(self, root, chatbot):
        self.chatbot = chatbot
        
        # Prompt the user for their name at the start
        self.user_name = simpledialog.askstring("Welcome", "Enter your name:", initialvalue="User_name")
        if not self.user_name:
            self.user_name = "User"
        
        root.title("Cartoon information ")
        
        # Set up the chat display
        self.chat_display = tk.Text(root, height=15, width=50, state='disabled', wrap='word')
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Set up the input field
        self.user_input = tk.Entry(root, width=40)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)
        
        # Set up the colorful send button with an arrow
        self.send_button = tk.Button(root, text="➤", font=("Arial", 12, "bold"), fg="white", bg="#00A3E0", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Bind Enter key to send message
        root.bind('<Return>', lambda event: self.send_message())
    
    def send_message(self):
        user_text = self.user_input.get()
        
        if user_text:
            # Display user input with the user's name
            self._display_text(f"{self.user_name}: {user_text}")
            
            # Get chatbot response
            bot_response = self.chatbot.get_response(user_text)
            
            # Display bot response
            self._display_text(f"Drake: {bot_response}")
            
            # Clear the input field
            self.user_input.delete(0, tk.END)
    
    def _display_text(self, text):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, text + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

def main():
    root = tk.Tk()
    chatbot = CartoonChatbot()
    gui = ChatbotGUI(root, chatbot)
    root.mainloop()

if __name__ == "__main__":
    main()
    
