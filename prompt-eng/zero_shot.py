#!/usr/bin/env python
# coding: utf-8

# 
# 
# 

# # Zero-Shot Prompting
# 
# Zero-shot prompting refers to a technique in prompt engineering where you provide a model with a task without any prior examples. The model is expected to understand and generate a response or complete the task purely based on the given instruction.
# 
# In other words, the model is given "zero" prior training examples or demonstrations in the prompt and relies on its pre-trained knowledge to infer what is needed.
# 
# ## References:
# * [Wei et al. (2022)](https://arxiv.org/pdf/2109.01652.pdf): demonstrate how instruction tuning improves zero-shot learning 

# ## Running this code on MyBind.org
# 
# Note: remember that you will need to **adjust CONFIG** with **proper URL and API_KEY**!
# 
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GenILab-FAU/prompt-eng/HEAD?urlpath=%2Fdoc%2Ftree%2Fprompt-eng%2Fzero_shot.ipynb)
# 
# 

# In[ ]:


##
## ZERO SHOT PROMPTING
##

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "What is 984 * log(2)"

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT = MESSAGE 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')


# ---
# 
# ## How to improve it?
# 
# * **Use Clear and Concise Instructions**: Be specific about the task and desired format.
#     * Bad Prompt: “Summarize this.”
#     * Good Prompt: “Summarize this paragraph in one sentence.”
# * **Add Context**: Providing background can help the model interpret ambiguous prompts better.
# * **Specify Output Format**: If a particular structure is needed, describe it in the instruction.
