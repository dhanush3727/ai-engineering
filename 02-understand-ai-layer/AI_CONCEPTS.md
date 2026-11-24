# AI Concepts:
## Embeddings:
An embedding in LLM is a list of numbers that represents the meaning of text such as a token, word, sentence, or document so a model can process it mathematically.

## Temperature:
Temperature in LLM controls the randomness of generated text by scaling token probabilities before the model picks the next word.

## Inference:
LLM inference is a process of running trained LLM on new data to generate a output such as text, summaries, or answers without updating its learned weight.

## Prompt Engineering:
### Role & System Prompting:
Separating the hidden developer instructions (`system` role) from the end-user input (`user` role) to define the AI's persona, output rules, and hard boundaries.

### Zero-shot prompting (Direct instruction):
Giving the model a clear task directly without providing any input/output examples.

### Few-shot prompting (Teaching by example):
Including 2 to 5 concrete input -> output examples right inside your prompt, so the model mirrors the exact output.

### Chain of thought (Step by step reasoning):
Instructing the model to think through a problem step by step before committing to a final answer or calling a tool.