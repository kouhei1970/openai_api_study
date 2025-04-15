from openai import OpenAI
client = OpenAI(api_key="sk-*******")

messages = [
    {"role": "system", "content": "あなたはやさしい物理の先生です。"},
    {"role": "user", "content": "エネルギー保存則って何？"},
    {"role": "assistant", "content": "エネルギー保存則は、エネルギーが常に一定であるという法則です。"},
    {"role": "user", "content": "じゃあ摩擦があるとどうなるの？"},
]
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)
