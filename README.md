# Cartoon_chatbot
1. Description of the Chatbot
The Cartoon information is a Talks Chatbot is designed to answer questions related to a small set of popular cartoon characters such as Doraemon, Shizuka, Nobita,Gian,sunio and Shin-chan. When a user types in a question mentioning one of these characters, the chatbot provides a predefined response about that character.

The project uses the Tkinter library to create a simple graphical user interface (GUI) where users can type questions and receive responses. This chatbot serves as an introduction to building conversational interfaces and is structured to be easily expandable, allowing more characters to be added to the response set.

2. How to Run the Chatbot
   1. Download or Clone the Repository
    git clone https://github.com/annurag133/Cartoon_chatbot.git
    cd cartoon-talks-chatbot

   2. Run the Python Script

    python cartoon_chatbot.py

   3. Using the Chatbot
    Once the application window opens, type a question about one of the supported cartoon characters (e.g., "Who is Doraemon?").
    Click the "Send" button or press "Enter" to get a response from the chatbot.
    The chatbot will respond with character-specific information if the character is recognized. Otherwise, it will prompt you to ask about a different cartoon character.

3. Dependencies
The Cartoon Talks Chatbot requires Python 3.x and the Tkinter library, which is usually included with Python installations. If Tkinter is not available, you can install it as follows: pip install tk

4. Explanation of the Code
The chatbot code consists of two main classes, CartoonChatbot and ChatbotGUI, which work together to process input, generate responses, and display them in a Tkinter-based GUI.

> CartoonChatbot Class
 This class contains a dictionary (self.responses) where each key is a character name, and each value is a string with information about the character.
 
> get_response(): Accepts a user input string, processes it to match character names, and retrieves the associated response if a match is found. If the character is not recognized, it returns a default message.

> _extract_character(): A helper function to identify character names in user input, enabling get_response() to look up responses based on character keywords.

> ChatbotGUI Class
Sets up and manages the graphical interface.
chat_display: Displays conversation history.
user_input: An entry field where users type their questions.
send_button: Sends user questions to the chatbot.
_display_text(): Updates the chat display area with new messages.
send_message(): Retrieves user input, calls get_response() from CartoonChatbot, and displays the chatbot's response.


5. Possible Future Developments
To enhance this project, here are a few potential upgrades:

> Add More Characters and Responses: Extend self.responses to include additional cartoon and anime characters for a wider range of responses.

> Natural Language Processing (NLP) Integration: Integrate NLP techniques (such as text classification or entity recognition) to allow the chatbot to understand a broader range of questions and provide responses accordingly.

> Interactive Elements in GUI: Improve the user interface with more visually appealing elements like images, emojis, or background themes to make the chatbot more engaging.
Speech Recognition and Text-to-Speech: Enable voice input and output for a more interactive experience, using libraries like SpeechRecognition and pyttsx3.

> Learning-Based Chatbot Model: Evolve the chatbot from a rule-based model to a machine learning-based model, allowing it to learn from user interactions and improve its responses over time.
