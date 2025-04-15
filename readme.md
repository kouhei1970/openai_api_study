# OpenAI API 入門：ChatCompletion の使い方（新形式対応）

---

## 【目的】
OpenAI API の新しい形式（v1.0.0以降）の `ChatCompletion` 使用方法を理解する

---

## 【ChatCompletion とは】
- ChatGPTのように「問答式のチャット」を実現するためのAPI
- チャット履歴（誰が何を言ったか）を、構造化されたリストとして渡す
- OpenAIライブラリ v1.0.0 以降は `OpenAI` クラスを使う新形式に変更

---

## 【基本構文（新形式）】
```python
from openai import OpenAI
client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "あなたは優しい先生です。"},
        {"role": "user", "content": "微分って何？"}
    ]
)

print(response.choices[0].message.content)
```

---

## 【パラメータ解説】
| 名前 | 意味 |
|--------|--------|
| `model` | 使用するAIモデル (`"gpt-4"` など) |
| `messages` | ロール付きメッセージのリスト |
| `temperature` | 応答のランダムさ（0で固定, 1で自由） |
| `max_tokens` | 最大出力トークン数 |

---

## 【messages の構造】
```python
messages = [
    {"role": "system", "content": "あなたは、親切なPython教師です。"},
    {"role": "user", "content": "for文って何に使うの？"},
]
```

| role | 意味 |
|------|------|
| `system` | AIの立場（人格や視点）を定義 |
| `user` | 人間の質問や入力 |
| `assistant` | AIからの返答（省略可能） |

---

## 【実行サンプル（v1.0.0以降対応）】
```python
from openai import OpenAI
client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "あなたは親切な先生です。"},
        {"role": "user", "content": "AIってなんですか？"}
    ]
)

print(response.choices[0].message.content)
```

---

## 【実行結果】
Q: AIってなんですか？  
A: AIは、人のように考えるように作られたプログラムや技術の組み合わせです...

---

## 【追加例①：temperature を変えてみよう】
```python
response = client.chat.completions.create(
    model="gpt-4",
    temperature=1.0,  # より自由で創造的な応答
    messages=[
        {"role": "system", "content": "あなたはユーモアのある先生です。"},
        {"role": "user", "content": "AIってなんですか？"}
    ]
)
```

- `temperature=0.0`：事実ベースで安定した応答
- `temperature=1.0`：自由度の高い創造的な応答

---

## 【追加例②：assistant ロールで文脈を持たせる】
```python
messages = [
    {"role": "system", "content": "あなたはやさしい物理の先生です。"},
    {"role": "user", "content": "エネルギー保存則って何？"},
    {"role": "assistant", "content": "エネルギー保存則は、エネルギーが常に一定であるという法則です。"},
    {"role": "user", "content": "じゃあ摩擦があるとどうなるの？"},
]
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages
)
```
- `assistant` ロールを使うと「AIが以前にこう答えた」という文脈が伝わる

---

## 【まとめ】
- `OpenAI` クラス経由で `client.chat.completions.create()` を使う（v1.0以降）
- `system` ロールでAIの立場や口調を指定
- `messages` リストでチャット履歴を構成し、`assistant` で文脈も継続可能
- `temperature` を調整することで応答の性格を変化させられる
- Python から簡単に利用できるが、**ライブラリのバージョンに注意**

---

