import requests
import json

API_KEY = "tXEYmAxK6EZD"
PROJECT_TOKEN = "tFMA3o46cafo"
RUN_TOKEN = "tZXQLyYhnOZb"

response = requests.get(
    f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(response.text)

print(data)
