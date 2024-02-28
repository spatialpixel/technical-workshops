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

  messages.push(message);

  for (const tool_call of message.tool_calls) {
    const functionName = tool_call.function.name;
    const functionArgs = JSON.parse(tool_call.function.arguments);

    if (functionName === "get_current_weather") {
      const functionResult = get_current_weather(functionArgs);

      messages.push({
        "tool_call_id": tool_call.id,
        "role": "tool",
        "name": functionName,
        "content": JSON.stringify(functionResult)
      });
    }
  }

  const completion2 = await openai.chat.completions.create({
    messages: messages,
    model: "gpt-3.5-turbo-0125"
  });

  console.log(completion2.choices[0].message);
}

function get_current_weather (args) {
  return {
    weather_response: "It's 38 degrees Fahrenheit and cloudy."
  }
}

main();
