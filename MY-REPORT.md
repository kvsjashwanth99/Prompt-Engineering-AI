## Exploring Prompt Engineering with Ollama for Automated Requirement Analysis

Investigating the effectiveness of prompt engineering techniques in GenAI-driven SDLC automation.

Authors: Venkata Sai Jaswanth Kommu

Academic Supervisor: Dr. Fernando Koch

## Research Question

How can prompt engineering techniques be leveraged to enhance automated requirement analysis in software development lifecycles using Ollama?

## Arguments

What is already known about this topic:

Prompt engineering is crucial for optimizing AI-generated responses.

NLP models like Ollama can be fine-tuned to improve requirement analysis automation.

The challenge lies in designing effective prompts for accurate and context-aware outputs.

 ## What this research is exploring:

We employ structured and iterative prompt refinement techniques.

We are building a simulated GenAI pipeline to evaluate prompt effectiveness.

We explore parameter tuning, such as temperature and response context size, in Ollama.

## Implications for practice

It will be easier to automate requirement analysis in SDLC.

It will optimize the interaction between AI models and software engineers.

We will better understand how prompt variations impact AI-generated responses.

## Research Method

We developed a structured pipeline to experiment with prompt engineering in Ollama:

## Pipeline Implementation:

Created _pipeline.py to handle model requests.

Implemented execute_prompt() to automate prompt execution.

## Experiment Execution:

Defined sample prompts (e.g., "Explain the significance of Newton's laws in physics").

Executed zero_shot.py to test the pipeline.

Evaluated response quality and processing time.

## Parameter Adjustments:

Experimented with different models and inference parameters.

Adjusted response length, temperature, and contextual window size.

## Results

The results of the zero-shot and few-shot experiments provide valuable insights into the effectiveness of the automated requirement analysis pipeline.

## Zero-Shot Results

For the zero-shot experiment, the model was asked to generate functional and non-functional requirements for a fitness tracker app. The generated content includes the following:

## User Stories:

The model generated five user stories describing various user needs and fitness tracking functionalities, from tracking daily steps and calories burned to monitoring heart rate and providing personalized recommendations.

## Functional Requirements:

The model generated five functional requirements such as Activity Tracking, Goal Setting and Progress Monitoring, Sleep Tracking, Social Sharing, and Personalized Recommendations. Each requirement addressed specific features necessary for fulfilling the app's user stories.

## Non-Functional Requirements:

The model generated five non-functional requirements, focusing on the quality aspects such as Usability (ease of data entry), Security (data encryption), Performance (real-time tracking), Availability (cloud storage), and Maintainability (regular software updates).

The output demonstrates that Ollama effectively identifies essential requirements and categorizes them into functional and non-functional types.

## Few-Shot Results

For the few-shot experiment, the model was given several examples of user stories and their corresponding functional and non-functional requirements. The model generated the following for a new user story:

## User Story:

"As a project manager, I want a dashboard to track real-time project progress so that I can ensure timely completion."

 ## Functional Requirements:

A real-time progress tracking dashboard for project managers.

The ability to view project milestones, timelines, and task status.

Alerts or notifications when tasks are nearing deadlines or have been completed.

## Non-Functional Requirements:

The dashboard should update within 5 seconds.

Project data should be stored securely and be backed up regularly.

The system must handle a large volume of concurrent users and requests without significant performance degradation.

## Security Considerations:

Data encryption at rest and in transit.

Authentication and authorization mechanisms to prevent unauthorized access.

Monitoring for suspicious activity or data breaches.

## Scalability and Performance:

Implement load balancing and distributed architecture.

Optimize database queries and indexing for faster performance.

Use caching strategies to reduce the load on the database.

## User Experience:

Ensure the dashboard is visually appealing and easy to navigate.

Provide intuitive filtering, sorting, and search capabilities.

Include real-time analytics and insights to help project managers make data-driven decisions.

Code Implementation Example:

# Importing required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import secrets
import string
import smtplib
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
mail = Mail(app)

# Database to store user credentials
users_db = {}

def generate_reset_token():
    return secrets.token_urlsafe(16)

def send_email(user, token):
    msg = Message('Reset Password', sender='your-email@gmail.com',
                  recipients=[user['email']])
    msg.body = f'Your password reset link is: {url_for("reset_password", token=token)}'
    mail.send(msg)

def verify_reset_token(token):
    return bool(secrets.compare_digest(generate_reset_token(), token))

@app.route('/forgot-password', methods=['GET'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        if email in users_db:
            user = users_db[email]
            token = generate_reset_token()
            send_email(user, token)
            return redirect(url_for('reset_password', token=token))
        else:
            return render_template('forgot_password.html', error='Email not found.')
    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET'])
def reset_password(token):
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']
        if new_password == confirm_new_password:
            users_db[request.form['email']] = {
                'password': new_password,
                'last_login': time.time()
            }
            return redirect(url_for('login'))
    return render_template('reset_password.html', token=token)

if __name__ == '__main__':
    app.run(debug=True)

## Key Findings from Both Approaches:

Zero-Shot: The model successfully generated basic requirements based on prompts, even without prior examples. The response was accurate but generalized.

Few-Shot: By providing examples of user stories and requirements, the model produced more specific and nuanced outputs, showcasing a deeper understanding of user needs.

## Further Research

Explore multi-turn dialogue prompts for better requirement elicitation.

Integrate additional GenAI models for comparison.

Automate prompt generation and refinement using meta-prompting techniques.

Extend the study to assess prompt effectiveness in different SDLC stages.