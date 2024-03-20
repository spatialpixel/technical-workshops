const OpenAI = require("openai");
const readline = require('readline');

const openai = new OpenAI();

const tools = [
  {
    type: "function",
    function: {
      name: "get_current_weather",
      description: "Returns the current weather in a given location.",
      parameters: {
        type: "object",
        required: ["location", "latitude", "longitude"],
        properties: {
          location: {
            type: "string",
            description: "City and country, e.g. San Francisco, CA, USA."
          },

          latitude: {
            type: "number",
            description: "The latitude of the place the user is asking about."
          },

          longitude: {
            type: "number",
            description: "The longitude of the place the user is asking about."
          }
        }
      }
    }
  }
];

const messages = [
  { "role": "system", "content": "You are a helpful assistant." }
];

async function main () {
  console.log(`I'm a GPT-powered chat who knows how to get the weather of your favorite cities. Ask away!

Oh, and I have a few commands too:
   "list" - lists all the raw messages I've seen
  
Press ctrl+c to exit.
`);
  const readline = require('readline');
  
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: '> '
  });
  
  rl.prompt();
  
  rl.on('line', async (input) => {
    // Evaluate the input
    try {
      if (input === "list") {
        console.log(messages);
      } else {
        await chat(input);
      }
    } catch (error) {
      console.error('Error:', error.message);
    }
  
    rl.prompt();
  }).on('close', () => {
    console.log('Exiting REPL.');
    process.exit(0);
  });
}

async function chat (prompt) {
  const promptMessage = { "role": "user", "content": prompt };
  messages.push(promptMessage);

  const completion = await openai.chat.completions.create({
    messages: messages,
    model: "gpt-3.5-turbo",
    tools: tools
  });

  const message = completion.choices[0].message;

  // console.log(message.tool_calls[0]);
  
  messages.push(message);
  
  if (!message.tool_calls) {
    console.log(message.content);
  } else {
    for (const tool_call of message.tool_calls) {
      const functionName = tool_call.function.name;
      const functionArgs = JSON.parse(tool_call.function.arguments);
  
      if (functionName === "get_current_weather") {
        const functionResult = await get_current_weather(functionArgs);
  
        // console.log(functionResult);
  
        messages.push({
          tool_call_id: tool_call.id,
          role: "tool",
          name: functionName,
          content: JSON.stringify(functionResult)
        })
      }
    }
  
    const completion2 = await openai.chat.completions.create({
      messages: messages,
      model: "gpt-3.5-turbo"
    });
  
    console.log(completion2.choices[0].message.content);
  }
}

async function get_current_weather (args) {
  // https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m

  const url = `https://api.open-meteo.com/v1/forecast?latitude=${args.latitude}&longitude=${args.longitude}&current=temperature_2m`

  const response = await fetch(url);
  return response.json()
}

main();
