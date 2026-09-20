import os
import json
import requests
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

    return {
        "error": "Unable to get weather information",
        "status_code": response.status_code
    }


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]


city = input("Enter city name: ")

messages = [
    {
        "role": "user",
        "content": f"What is the current weather in {city}?"
    }
]


response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    tools=tools,
    tool_choice="required"
)

message = response.choices[0].message


if message.tool_calls:

    tool_call = message.tool_calls[0]

    arguments = json.loads(tool_call.function.arguments)

    weather = get_weather(arguments["city"])

    print("\nFunction Called:", tool_call.function.name)

    messages.append(message)

    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(weather)
    })


    final_response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    print("\nFinal Answer:")
    print(final_response.choices[0].message.content)

else:
    print(message.content)
