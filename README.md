# Rain Alert Notifier

![App Screenshot]()

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Author](#author)

## Description
This program checks the weather forecast for rain in a specific location and sends an 
SMS alert using the Twilio service if rain is predicted. It utilizes the OpenWeatherMap 
API to gather weather data and the Twilio API to send SMS messages.

## Requirements
- Python 3.x
- Twilio Account: You need a Twilio account with a valid account_sid and auth_token.
- OpenWeatherMap API Key: You need an API key from OpenWeatherMap to access weather data.
- requests library (`pip install requests`)
- twilio library (`pip install twilio`)

## Features
- The program sends a request to the OpenWeatherMap API to fetch weather data for 
the specified location.
- It checks the weather condition codes to determine if rain is predicted (condition code < 700).
- If rain is predicted, the program uses the Twilio API to send an SMS alert to 
the specified phone number.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/laurianerzb/rain-alert-notifier.git
2. Navigate to the project directory:
   ```bash 
   cd rain-alert-notifier
3. Run the program
   ```bash
   python main.py
4. install the requests and twilio libraries
    ```bash
    pip install requests twilio

## Author
- [laurianerzb](https://github.com/laurianerzb)
