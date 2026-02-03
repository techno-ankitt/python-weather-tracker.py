# python-weather-tracker.py

A secure and lightweight Python-based Command Line Interface (CLI) tool that fetches real-time weather data using the OpenWeatherMap API. This project is designed with a focus on secure coding practices by utilizing environment variables to handle sensitive API credentials.

-------Features--------
1.Real-time Weather: Fetches current temperature, "feels like" temperature, humidity, and wind speed.
2.Security Focused: Uses python-dotenv to isolate API keys from the source code, preventing accidental leaks.
3.Error Handling: Comprehensive checks for invalid city names and missing configuration files.

--------Installation & Setup----------
Clone or Download the Project: Download the source code files to your local machine.

Install Dependencies: Open your terminal/command prompt and run: pip install requests python-dotenv

Configure API Key:-----------
1.Obtain a free API key from OpenWeatherMap.
2.Create a file named .env in the root directory.
3.Add your key in the following format:
OPENWEATHER_API_KEY=your_actual_api_key_here

--------Usage---------
Run the script using Python:

Bash--------------
python python-weather-tracker.py

-------Security Note----------
The .env file is explicitly excluded via .gitignore to ensure private keys are never uploaded to public repositories. A template file .env.example is provided for reference.
