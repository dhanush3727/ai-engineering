// import { get_encoding } from "tiktoken";
import OpenAI from "openai";

// get_encoding() loads a specific tokenizer encoding.
// These arguments are encoding names, NOT AI model names.
//
// "cl100k_base" -> Used by GPT-3.5 Turbo and GPT-4
// "o200k_base"  -> Used by GPT-4o
// "p50k_base"   -> Used by older Codex models
// "r50k_base"   -> Used by older GPT-3 models
//
// Each encoding has its own vocabulary and tokenization rules.
// Different encodings may split the same text differently
// and assign different numerical token IDs.

// const encoding = get_encoding("cl100k_base");

// encode() converts text into numerical token IDs.
// const tokens = encoding.encode("Dhanush");

// console.log(tokens);

// decode() converts token IDs into UTF-8 bytes.
// const decodedBytes = encoding.decode(tokens);

// TextDecoder converts UTF-8 bytes into a readable string.
// const text = new TextDecoder().decode(decodedBytes);

// console.log(text);

const OPENAI_API_KEY = "your_api_key";

const client = new OpenAI({
    apiKey: OPENAI_API_KEY
})

const stream = await client.responses.create({
    model: "chatgpt-4o-latest",
    input: "Write story about a robot",
    temperature: 0.7,
    max_output_tokens: 50,
    stream: true
})

// Async iterable
// we use stream as true so we can get event like this
for await (const event of stream){
    if(event.delta){
        // This is help to write the events next to each other
        process.stdout.write(event.delta)
    }
}