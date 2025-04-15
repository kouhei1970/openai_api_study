from openai import OpenAI
client = OpenAI(api_key="sk-*******")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=1.0,  # より自由で創造的な応答
    messages=[
        {"role": "system", "content": "あなたはユーモアのある先生です。"},
        {"role": "user", "content": "AIってなんですか？"}
    ]
)

print(response.choices[0].message.content)
