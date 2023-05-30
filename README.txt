Telegram Image Bot
This is a simple Telegram bot that sends random images from selected folders to users. Users can choose a folder and receive a random image from that folder.

Prerequisites
Make sure you have the following requirements installed:

Python 3
telebot library (install using pip install pytelegrambotapi)
Getting Started
Clone or download the repository to your local machine.

Create a Telegram bot and obtain an API token. You can create a new bot and get the token by following the instructions in the BotFather documentation.

Create a token.txt file in the project directory and paste your bot token into the file.

Organize your images into folders and specify the path to the image folder in the IMAGE_FOLDER variable in the code.

Run the script by executing the following command in your terminal:


python your_script_name.py
Start a conversation with your bot in Telegram and send the /start command to begin.
Usage
Upon starting the conversation with the bot, you will be prompted to choose a folder.

Select one of the available folders by tapping the corresponding button.

The bot will send a random image from the selected folder to you.

If there are no images in the chosen folder, the bot will inform you.

You can choose a different folder and receive another random image by repeating the process.

Customization
You can modify the IMAGE_FOLDER variable in the code to specify the path to your image folder.

If you want to change the behavior of the bot or add more functionality, you can modify the existing functions or add new ones as needed.

That's it! You now have a Telegram bot that can send random images from selected folders. Feel free to customize and extend the code to suit your needs.
