from typing import TypedDict
import aiohttp
import secret
from SharkBot import Errors


class Prompt(TypedDict):
    role: str
    content: str


SHARKBOT_PROMPT = Prompt(
    role="system",
    content="You are SharkBot, a member of our clan that is designed to give fun and interesting responses. Pretend to be a human using discord. You can use discord markdown and emojis to make your responses look better. Always give the most comedic and chaotic response to a prompt. Assume you will be given no more information, do not ask for it. Use they/them pronouns."
)


async def make_request(messages: list[dict]) -> tuple[int, dict]:
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers=secret.OpenAI.API_HEADERS,
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": messages
                }
        ) as resp:
            return resp.status, await resp.json()


async def make_image_request(message: str) -> tuple[int, dict]:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.openai.com/v1/images/generations",
            headers=secret.OpenAI.API_HEADERS,
            json={
                "prompt": message,
                "n": 1,
                "size": "1024x1024"
            }
        ) as resp:
            response = await resp.json()
            if "error" in response:
                raise Errors.OpenAI.BadPromptError(message)
            return resp.status, response


async def ask_sharkbot(message: str) -> tuple[int, dict]:
    return await make_request([SHARKBOT_PROMPT, {"role": "user", "content": message}])