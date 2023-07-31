# Simple Keylogger

A simple keylogger written in Python using the `pynput` library to capture key events and save them in both JSON and text file formats.

## Description

This project is a basic keylogger that records keyboard events such as key presses, holds, and releases. It provides a timestamp for each event and stores the captured data in both JSON and text file formats.

## Features

- Captures key presses, holds, and releases.
- Saves key logs in JSON and text file formats.
- Provides timestamps for each key event.
- Lightweight and easy to use.

## How to Use

### Installation

1. Clone the repository to your local machine:

```bash
$ git clone https://github.com/your_username/your_repo.git
$ cd your_repo
```

## 1.Install the required dependencies:
$ pip install pynput

### Running the Keylogger
To start the keylogger, execute the keylogger.py script:
$ python keylogger.py
The keylogger will begin capturing keyboard events and saving the logs in both logs.json and logs.txt.

### Data Storage
The key logs are saved in two formats:
logs.json: 
          Stores the key logs in JSON format, with details like key, action (Pressed, Held, Released), and timestamp for each event.
logs.txt: 
          Contains the raw key strokes captured by the keylogger.
### Disclaimer
Please note that using keyloggers to capture sensitive information without proper authorization is illegal and unethical. Keyloggers should only be used responsibly for legitimate purposes, such as debugging, personal use, or by system administrators for monitoring authorized users. Always respect privacy and adhere to applicable laws and regulations.


Remember to replace `your_username/your_repo` with your GitHub username and repository name. Customize the content under each section to describe your project thoroughly. Additionally, add any relevant details like project structure, setup, or usage examples to make the README informative and user-friendly.


