# Weather API Function Calling

## Project Overview

Weather API Function Calling is a Python-based weather application that uses an LLM with function calling to retrieve current weather information for a selected city.

The application uses Groq for function calling and the OpenWeather API to obtain real-time weather data. The LLM identifies when the weather function should be used, calls the `get_weather()` function, and the weather data is then returned to the LLM to generate the final response.

## Features

* Accepts a city name from the user
* Uses Groq LLM for function calling
* Uses the OpenWeather API for weather data
* Retrieves temperature, humidity, weather condition, and wind speed
* Demonstrates tool/function calling
* Uses environment variables to protect API keys
* Generates a final natural-language weather response

## Technologies Used

* Python
* Groq API
* OpenWeather API
* OpenAI Python SDK
* Requests
* Python-dotenv

## Project Workflow

```text
User Input
    |
    v
Groq LLM
    |
    v
Function Call: get_weather()
    |
    v
OpenWeather API
    |
    v
Weather Data
    |
    v
Groq LLM
    |
    v
Final Weather Response
```

## Project Structure

```text
Weather-API-Function-Calling/
│
├── weather_app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── venv/
```

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd Weather-API-Function-Calling
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## API Key Configuration

Create a `.env` file in the project folder.

Add the following:

```text
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Replace the placeholder values with your own API keys.

Do not upload the `.env` file to GitHub.

## Running the Application

Run the following command:

```powershell
python weather_app.py
```

Enter a city name when prompted:

```text
Enter city name: chennai
```

The application calls the weather function and displays the final weather response.

## Example

```text
Enter city name: chennai

Function Called: get_weather

Final Answer:
The current weather in Chennai is ...
```

## Function Calling

The application defines a `get_weather()` function as a tool for the LLM.

The function accepts a city name and retrieves weather information from the OpenWeather API.

The main function-calling process is:

1. The user enters a city name.
2. The request is sent to the Groq LLM.
3. The LLM selects the `get_weather()` function.
4. The application executes the function.
5. The function requests weather data from OpenWeather.
6. The weather result is returned to the LLM.
7. The LLM generates the final response.

## Environment Variables

The following environment variables are required:

```text
GROQ_API_KEY
OPENWEATHER_API_KEY
```

These keys are loaded using the `python-dotenv` package.

## Security

API keys should not be hard-coded in the Python source code.

The `.env` file is excluded from GitHub using `.gitignore`.

Example `.gitignore`:

```text
.env
venv/
__pycache__/
```

## Conclusion

This project demonstrates how function calling can connect an LLM with an external API. The Groq LLM determines when to call the weather function, while the OpenWeather API provides the actual weather information.

## Author 
HUMAIRUL JASHIRA M
