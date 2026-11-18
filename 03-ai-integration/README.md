# AI Integration:
## Install tiktoken:
The `tiktoken` library used to converting ordinary text into numerical token ID. This is developed by OpenAI.
```js
import { get_encoding } from "tiktoken";
const encoding = get_encoding("cl100k_base");
// encode() converts text into numerical token IDs.
const tokens = encoding.encode("Dhanush");
console.log(tokens);
// decode() converts token IDs into UTF-8 bytes.
const decodedBytes = encoding.decode(tokens);
// TextDecoder converts UTF-8 bytes into a readable string.
const text = new TextDecoder().decode(decodedBytes);
console.log(text);
```
Here,
get_encoding() loads a specific tokenizer encoding. These arguments are encoding names, NOT AI model names.
"cl100k_base" -> Used by GPT-3.5 Turbo and GPT-4
"o200k_base"  -> Used by GPT-4o
"p50k_base"   -> Used by older Codex models
"r50k_base"   -> Used by older GPT-3 models
Each encoding has its own vocabulary and tokenization rules. Different encodings may split the same text differently
and assign different numerical token IDs.

## Choosing right model:
Choosing a right model depends on our application and its requirements. Focus on some criteria that matter when choosing a model.
- Reasoning
- Speed
- Modalities
- Cost
- Context Window
- Privacy

### Reasoning:
If we want to solve complex problem then choose a stronger reasoning model. But if we need some extract, classify or summarize text then don't need a top tier model

### Speed:
It determine the models response speed bigger model often very slower but the smaller models are faster.

### Modalities:
What kinds of input and output are we are going to send to and receive from a model. Text is most common, 
but newer models can also process images, audio, video or even a combination of those. These are called LMMs (Large Multi-modal Models)

### Cost:
This is based on number of tokens.

### Context window:
How much tokens model can handle for current window. This is include text, input, model response and also chat history.
