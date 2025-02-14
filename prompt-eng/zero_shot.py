import requests
import json

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Define a function to generate requirements using Ollama
def generate_requirements(prompt_template, model="llama3"):
    payload = {
        "model": model,
        "prompt": prompt_template,
        "stream": False  # Set to True if you want streaming responses
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# Define Prompt Templates
user_story_template = """
Generate 5 user stories for a fitness tracker app. Each story should follow the format:
"As a [type of user], I want [some goal] so that [some reason]."
"""

functional_req_template = """
Generate 5 functional requirements for a fitness tracker app. Each requirement should describe a feature or functionality.
"""

non_functional_req_template = """
Generate 5 non-functional requirements for a fitness tracker app. Each requirement should describe a quality attribute, such as performance, security, or usability.
"""

# Generate Requirements
user_stories = generate_requirements(user_story_template)
functional_reqs = generate_requirements(functional_req_template)
non_functional_reqs = generate_requirements(non_functional_req_template)

# Save Results to a JSON File
requirements = {
    "user_stories": user_stories.split("\n"),
    "functional_requirements": functional_reqs.split("\n"),
    "non_functional_requirements": non_functional_reqs.split("\n"),
}

with open("requirements.json", "w") as f:
    json.dump(requirements, f, indent=4)

print("Requirements generated and saved to requirements.json!")