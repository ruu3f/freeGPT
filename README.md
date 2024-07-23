<img src="https://repository-images.githubusercontent.com/636250478/f62a1186-b84b-4e7a-86f1-145e32163a59" align="right" width=170>

[![PyPI](https://img.shields.io/pypi/v/freeGPT)](https://pypi.org/project/freeGPT)
[![Downloads](https://static.pepy.tech/badge/freeGPT)](https://pypi.org/project/freeGPT)
[![Status](https://img.shields.io/pypi/status/freeGPT)](https://pypi.org/project/freeGPT)

# freeGPT

freeGPT provides free access to text and image generation models.

 *There is also an official [Discord bot](https://github.com/Ruu3f/freeGPT-discord).*

## Getting Started:

    python -m pip install -U freeGPT

## Sources:

| Model        | Website                                                |
| ------------ | ------------------------------------------------------ |
| gpt3         | [chat9.yqcloud.top](https://chat9.yqcloud.top/)        |
| gpt4         | [you.com](https://you.com/)                            |
| gpt3_5       | [vitalentum.net](https://vitalentum.net/free-chat-gpt) |
| prodia       | [prodia.com](https://prodia.com/)                      |
| pollinations | [pollinations.ai](https://pollinations.ai/)            |

## Support this repository:

- ⭐ **Star the project:** Star this and the [freeGPT-discord repository](https://github.com/Ruu3f/freeGPT-discord). It means a lot to me! 💕

## Examples:

### Text Completion:

```python
from freeGPT import Client

while True:
    prompt = input("👦: ")
    try:
        resp = Client.create_completion("MODEL", prompt)
        print(f"🤖: {resp}")
    except Exception as e:
        print(f"🤖: {e}")
```
### With Memory Support:

```python
from freeGPT import Client

class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_to_history(self, user_input, bot_response):
        self.history.append(f"User: {user_input}\nBot: {bot_response}")

    def get_history(self):
        return "\n".join(self.history)

memory = ConversationMemory()

while True:
    prompt = input("👦: ")
    history = memory.get_history()
    try:
        full_prompt = f"{history}\nUser: {prompt}\nBot:"
        resp = Client.create_completion("gpt3_5", full_prompt)
        print(f"🤖: {resp}")
        memory.add_to_history(prompt, resp)
    except Exception as e:
        print(f"🤖: {e}")
```

### Image Generation:

```python
from freeGPT import Client
from PIL import Image
from io import BytesIO

while True:
    prompt = input("👦: ")
    try:
        resp = Client.create_generation("MODEL", prompt)
        Image.open(BytesIO(resp)).show()
        print(f"🤖: Image shown.")
    except Exception as e:
        print(f"🤖: {e}")
```

## Star History Chart:

[![Star History Chart](https://api.star-history.com/svg?repos=Ruu3f/freeGPT&theme=dark)](https://github.com/Ruu3f/freeGPT/stargazers)
