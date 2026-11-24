# Understanding AI Layers
## AI(Artificial Intelligence):
Artificial Intelligence (AI) is a technology that enables machines and computers to perform tasks that typically require human intelligence. It allows systems to learn from data, recognise patterns and make decisions to solve complex problems.

## Machine Learning:
Machine Learning is where we train machines on data so that they can make predictions without explicit programming.
- Classification: Classification is the process of identifying something and assigning it to a predefined category or class based on its characteristics.
- Regression: Regression is the process of predicting a continuous numerical value based on patterns learned from training data. 

## Deep Learning:
Deep Learning is a machine learning technique that uses neural networks to learn from large amounts of data, mimiking the human brain's ability to recognize patterns and make decisions.

## Models:
A model is a computer program trained on data to recognize patterns, make predictions, or generate new content without being explicitly hardcoded for every task.
### How an AI Model works:
- Training data: The model is fed large datasets such as text, images, audio, or numbers relevant to the goal.
- Learning Patterns: Algorithms analyze the data, adjust internal parameters and map out statistical relationships.
- Inference: Once trained, you give the model new input data, and it uses what it learned to generate a prediction, classification, or piece of content.

## Gen AI:
Generative AI is a type of artificial intelligence that can create brand new content such as text, image, audio, video, and computer code in response to user prompts.
### How it works:
- Learning Patterns: Gen AI is trained on massive datasets using deep learning and neural networks.
- Prompt based generation: When you give it a prompt, the model predicts the most likely next piece of data based on the patterns it learned.
- Core architecture: It is powered by technologies like Large Language Models (LLM), Transformers, Diffusion Models, and Generative Adversarial Networks.

## LLM:
A Large Language Model is an artificial intelligence program trained on massive amounts of text to recognize language patterns, understand context, and generate human-like responses. LLM just think and give the output based on the input this is the work of LLM.

### How LLMs Work:
- Training Data: They are fed billions or trillions of words from books, articles, websites, and code.
- Pattern Recognition: Instead of thinking like a human, they use deep learning specifically a neural network architecture called transformer to look at how words telate to one another.
- Next-Word prediction: When you give it a prompt, the model calculates probabilities and predicts the most logical next word or token, step by step, to build a coherent response.

### Tokenization:
Tokenization is the foundational process of breaking raw text into smaller units called tokens and converting those units into unique numerical IDs that a LLM can process. EVery instruction you give an LLM is converted into tokens. Every model has its own tokenization method example:
For the word `unbelivable`,
- Model A will use 1 token and
- Model B will use 2 tokens (`un` - `belivalbe`)
So word is not equal to token.

There are 3 types of tokens
- Input tokens
- Output tokens
- Cached input tokens

### Parameters:
Parameters are the internal numerical values(numbers) that an AI model learns during training to process text and predict next token. They help the model recognize patterns and generate responses.
If parameter size is increase then the LLM accuracy also directly increase but local usage run is low.
If we choose high parameter LLM then we want the high level system requirements.

### Context Window:
Context window in LLM is the maximum amount of text measured in tokens that the model can process, hold, and reference during a single interaction.
In simple how many tokens the model can handle in its current context.
Ex:

### LLM Limitations:
- Hallucinations
- Incorrect answers
- Outdated information
- Bias
- Lack of guaranteed fact
- Context limitations
- Overconfidence

### Hallucination:
An LLM hallucination happens when a LLM generates a response that sounds fluent, coherent, and confident but is factually false, completely fabricated, or disconnected from reality.

## Use AI model:
```py
from huggingface_hub import snapshot_download
from transformers import pipeline

model_name = "google/flan-t5-small"
model_folder = "model/" + model_name.replace("/", "_")

print("Downloading", model_name)
snapshot_download(repo_id=model_name, local_dir=model_folder)
print("Model saved in", model_folder)

ai = pipeline("text2text-generation", model=model_folder)

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    result = ai(question, max_new_tokens=100)
    print("AI: ", result[0]["generated_text"])
```
In this code,
### Importing libraries:
```py
from huggingface_hub import snapshot_download
from transformers import pipeline
```
Here,
- `huggingface_hub` is the library and `snapshot_download` is a function inside that library.
- Its responsibility is to download all files from a particular Hugging Face repository.
- `snapshot_download()` downloads the repository files.
- For the second import same as for first import `transformers` is the library and `pipeline` is a function inside that library.
- Its responsibility is to provide a convenient interface for using pretained AI models.
- `snapshot_download()`: Downloads model files.
- `pipeline()`: Loads and uses the model for a task.

### Specifying the model name:
```py
model_name = "google/flan-t5-small"
```
- `model_name` is a variable and `google/flan-t5-small` repo ID on hugging face.
- `google`: The organization that published the model.
- `flan-t5-small`: The model name.

### Creating a local folder path:
```py
model_folder = "model/" + model_name.replace("/", "_")
```
- The `replace()` method replaces one character with another. Ex: `google/flan-t5-small` into `google_flan-t5-small`, because we want to use the model name as a folder name without creating unwanted nested directories.

### Downloading the model:
- `print("Downloading", model_name)`: Simply displays a message in the terminal.
- `snapshot_download(repo_id=model_name, local_dir=model_folder)`: This is where the actual download happens. `repo_id` identifies which hugging face repository to download. `local_dir` specifies where to save the downloaded files.
- `Model saved in model/google_flan-t5-small`: This prints the local folder path.

### Loading the AI model:
```py
ai = pipeline("text2text-generation", model=model_folder)
```
- What is `pipeline()`?
`pipeline()` is a high-level API provided by transformers. It simplifies the process of loading a model and using it for a particular task. Normally, you would need to handle things like, loading the tokenizer, loading model weights, preparing input tokens, runnig model inference, converting generated tokens back into text. The pipeline handles most of that for you.

- What does `"text2text-generationg"` mean?
It tells Transformers what task you want to perform. In this case, Input text -> AI model -> Generated text. We're using FLAN-T5, which is an encoder-decoder model designed for text to text tasks.

- What does `model=model_folder` mean?
It tells Transformers where to load the model from. Notice that we're using the local folder, not the hugging face repo ID.

- Load the model stored in this local folder and prepare it for text to text generation. The `ai` variable now holds the pipeline object that you can use to generate responses.

### Creating an infinite loop:
```py
while True:
```
- Use `while` loop and set as `True`, so the loop keeps running until you explicitly stop it.

### Getting user input:
```py
question = input("You: ")
```
- `input()` is a built-in Python function. It displays a message and waits for the user to enter something.

### Checking whether the user wants to exit:
```py
if question.lower() == "exit":
    break
```
- If user enter `exit` then loop will stop.
- `.lower()` used for case sensitive.

### Sending the question to AI model:
```py
result = ai(question, max_new_tokens=5)
```
- `ai(question)`: This is passing the user's question to the pipeline.
- `max_new_tokens=100`: It controls the maximum number of new tokens the model can generate. A token is a small unit of text processed by an AI model. It can be a word, part of a word, or punctuation.
- The model can generate up to 100 new tokens for this request. It doesn't guarantee that the model will generate all 100 tokens. It may stop earlier.
- What is the `result`?
The pipeline returns its output as a list containing dictionaries.
```py
[
    {
        "generated_text": "Artificial intelligence is..."
    }
]
```
Then we can get the `generated_text` from the result `result[0]["generated_text"]`.

## Use another AI Model:
```py
from huggingface_hub import snapshot_download
from transformers import pipeline

model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"
model_folder = "model/" + model_name.replace("/", "_")

print("Downloading", model_name)
snapshot_download(repo_id=model_name, local_dir=model_folder)
print("Model saved in", model_folder)

ai = pipeline("text-generation", model=model_folder)

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    message=[{"role": "user", "content": question}]
    result = ai(message, max_new_tokens=100)
    print("AI: ", result[0]["generated_text"][-1]["content"])
```
All things are same from the above we just only saw,
`message=[{"role": "user", "content": question}]`:
- In this code we use instruction-tuned chat models.
- So we explicitly tell that role is user and the user question go to that content the `result` look like
```py
[
    {
        'generated_text': [
            {
                'role': 'user',
                'content': 'hi'
            },

            {
                'role': 'assistant',
                'content': 'Hello! How can I help you today'
            }
        ]
    }
]
```
- We get this response so we print `print("AI: ", result[0]["generated_text"][-1]["content"])`