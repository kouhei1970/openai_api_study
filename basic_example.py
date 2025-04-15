from openai import OpenAI
client = OpenAI(api_key="sk-*******")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "あなたは優しい先生です。"},
        {"role": "user", "content": "微分って何？"}
    ]
)

print(response.choices[0].message.content)
