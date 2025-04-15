## 【追加例②：assistant ロールで文脈を持たせる】

```python
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
```

- `assistant` ロールは「過去のAIの発言」を明示的に示すためのものです。
- このロールを使うと、**前回のAIの応答を踏まえた「続きの会話」**ができます。
- `assistant` を入れないと、AIは過去の応答を知らない状態として扱います。
- 文脈を維持した対話を構成するには `user` と `assistant` を交互に記録するのが有効です。】

```python
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

