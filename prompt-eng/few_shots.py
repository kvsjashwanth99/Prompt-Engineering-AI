import json
import time
import matplotlib.pyplot as plt
from _pipeline import execute_prompt

# Define multiple prompt techniques
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
"""

zero_shot_prompt = """
Analyze the following user story and generate functional and non-functional requirements.
User Story: "As a project manager, I want a dashboard to track real-time project progress so that I can ensure timely completion."
Functional Requirements:
"""

chain_of_thought_prompt = """
Let's break this down step by step:
1. What is the primary functionality needed for a project tracking dashboard?
2. What system features are essential for tracking real-time progress?
3. What additional non-functional requirements are needed for security and performance?
Now generate a list of functional and non-functional requirements:
User Story: "As a project manager, I want a dashboard to track real-time project progress so that I can ensure timely completion."
Functional Requirements:
"""

# Experiment with multiple techniques
experiments = {
    "Few-Shot": few_shot_examples,
    "Zero-Shot": zero_shot_prompt,
    "Chain of Thought": chain_of_thought_prompt
}

results = {}

for technique, prompt in experiments.items():
    start_time = time.time()
    execution_time, response = execute_prompt(prompt)  # Unpack the tuple correctly
    
    print(f"\n🔍 Debugging {technique} Response:")
    print("Type:", type(response))
    print("Raw Response:", response)

    if isinstance(response, str):
        parts = response.strip().split("Non-Functional Requirements:")
        functional_requirements = parts[0].strip().split("\n") if len(parts) > 0 else []
        non_functional_requirements = parts[1].strip().split("\n") if len(parts) > 1 else []

        results[technique] = {
            "user_story": "As a project manager, I want a dashboard to track real-time project progress so that I can ensure timely completion.",
            "functional_requirements": functional_requirements,
            "non_functional_requirements": non_functional_requirements,
            "execution_time": execution_time
        }
        print(f"{technique} completed in {execution_time:.2f} seconds.")
    else:
        print(f"❌ Error: Response from {technique} is not a string. Instead, got: {type(response)}")

# Save results to a JSON file
with open("experiment_results.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

print("✅ Results saved to experiment_results.json")

# Generate a visualization of execution times
plt.figure(figsize=(8, 5))
techniques = list(results.keys())
times = [results[tech]["execution_time"] for tech in techniques]

plt.barh(techniques, times, color=["blue", "green", "red"])
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Prompt Engineering Techniques")
plt.title("Comparison of Prompt Engineering Techniques Execution Time")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.savefig("experiment_results.png")
plt.show()
