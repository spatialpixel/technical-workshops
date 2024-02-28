const OpenAI = require("openai");

const openai = new OpenAI();

async function main () {
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
  }
}

main();
