const OpenAI = require("openai");

const openai = new OpenAI();

async function main () {
  const messages = [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "What is the weather in New York City?" }
  ];

  const tools = [
    {
      type: "function",
      function: {
        name: "get_current_weather",
        description: "Returns the current weather in given location.",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "City and country, e.g. San Francisco, CA, USA."
            }
          },
          required: ["location"]
        }
      }
    }
  ];

  const completion = await openai.chat.completions.create({
    messages: messages,
    model: "gpt-3.5-turbo-0125",
    tools: tools
  });

  const message = completion.choices[0].message;
  console.log(message.tool_calls[0]);
}

main();
