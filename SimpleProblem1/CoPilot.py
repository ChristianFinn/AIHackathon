import json

json_data = '{ "tools": ["copilot", "cody", "whisper", "copilot"], "email": "thecookiemonster@cookiejar.com" }'
data = json.loads(json_data)

# Accessing the values
tools = data["tools"]
email = data["email"]

# Printing the values
print("Tools:", tools)
print("Email:", email)