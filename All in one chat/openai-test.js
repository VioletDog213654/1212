import OpenAI from 'openai';
const openai = new OpenAI({ apiKey: 'sk-hV0GFR7b8CIY8qDAxezLL9NZbJPZHzq10G0oZuu9HHNC9byj',base_url:"https://api.moonshot.cn" });

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "你好" }],
    model: "moonshot-v1-8k",
  })
  console.log(completion.choices[0]);
}

main();