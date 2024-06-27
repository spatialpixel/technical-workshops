const OpenAI = require("openai");

const openai = new OpenAI();

async function main () {
  const messages = [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "What is the weather in Lisbon, Portugal?" }
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
            },
            latitude: {
              type: "number",
              description: "The latitude of the city the user is asking about."
            },
            longitude: {
              type: "number",
              description: "The longitude of the city the user is asking about."
            }
          },
          required: ["location", "latitude", "longitude"]
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
  
  // Check to see if there are any tool calls to follow up on.
  // If so, go ahead and call those functions.
  if (message.tool_calls) {
    console.log(message.tool_calls[0]);
  
    messages.push(message);
  
    for (const tool_call of message.tool_calls) {
      const functionName = tool_call.function.name;
      const functionArgs = JSON.parse(tool_call.function.arguments);
  
      if (functionName === "get_current_weather") {
        const functionResult = await get_current_weather(functionArgs);
  
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
  } else {
    // If there are no tools to call, then print the resulting message to the console.
    console.log(message.content);
  }
}

async function get_current_weather (args) {
  // "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
  // https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m

  const url = `https://api.open-meteo.com/v1/forecast?latitude=${args.latitude}&longitude=${args.longitude}&current=temperature_2m`
  
  const response = await fetch(url);
  const json = await response.json();
  return json;
}

main();
