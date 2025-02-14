import json
from _pipeline import execute_prompt

# Few-shot examples with user story, functional, and non-functional requirements
few_shot_examples = """
Example 1:
User Story: "As a user, I want to reset my password if I forget it."
Functional Requirements:
- The system must provide a 'Forgot Password' link.
- A verification email should be sent with a reset link.
- The reset link should expire in 24 hours.
Non-Functional Requirements:
- The reset process should not take more than 10 seconds.
- The system must comply with security best practices for password storage.
- The reset link must be encrypted and secure.

Example 2:
User Story: "As an admin, I want to manage user roles and permissions."
Functional Requirements:
- Admins can assign and revoke roles.
- Users with specific roles should have limited access to features.
- Changes to roles should be logged.
Non-Functional Requirements:
- Role updates should take effect immediately.
- The system should log role changes with timestamps and admin details.
- The UI should be intuitive and accessible for role management.

Now analyze the following user story:
User Story: "As a project manager, I want a dashboard to track real-time project progress so that I can ensure timely completion."

Functional Requirements:
"""

# Get the response from the AI model
time_taken, response = execute_prompt(few_shot_examples)

# Ensure that response is a string
if isinstance(response, str):
    # Split the response to separate functional and non-functional requirements
    parts = response.strip().split("Non-Functional Requirements:")
    functional_requirements = parts[0].strip().split("\n") if len(parts) > 0 else []
    non_functional_requirements = parts[1].strip().split("\n") if len(parts) > 1 else []
    
    # Store the response in a structured dictionary
    requirements = {
        "user_story": "As a project manager, I want a dashboard to track real-time project progress so that I can ensure timely completion.",
        "functional_requirements": functional_requirements,
        "non_functional_requirements": non_functional_requirements
    }

    # Save the results to a JSON file
    with open("requirements_few_shots.json", "w") as f:
        json.dump(requirements, f, indent=4)

    print("Requirements have been generated and saved to requirements.json!")
else:
    print(f"Error: The response is not a string, but a {type(response)}.")
