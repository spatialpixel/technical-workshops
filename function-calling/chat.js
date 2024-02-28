const OpenAI = require("openai");

const openai = new OpenAI();

async function main () {
  const messages = [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "What can you tell me about artificial intelligence?" }
  ];

  const completion = await openai.chat.completions.create({
    messages: messages,
    model: "gpt-3.5-turbo"
  });

  console.log(completion.choices[0].message);
}

main();
