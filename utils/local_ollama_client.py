"""
@Time ： 2024-10-28
@Auth ： Adam Lyu
"""
import json

import requests


class LocalOllamaClient:
    def __init__(self, model="mistral:latest", temperature=1, host="192.168.2.13", port=11434):
        self.model = model
        self.temperature = temperature
        self.url = f"http://{host}:{port}/api/"

    def generate(self, prompt):
        response = requests.post(self.url + 'generate', json={
            "model": self.model,
            "prompt": prompt,
            "temperature": self.temperature
        })
        response.raise_for_status()

        # 将响应内容逐行解析为 JSON 对象
        results = []
        for line in response.content.splitlines():
            if line.strip():  # 忽略空行
                try:
                    parsed_json = json.loads(line)
                    results.append(parsed_json)
                except json.JSONDecodeError as e:
                    print("JSON 解码错误:", e)
                    continue  # 忽略错误行，继续处理其他行

        return results

    def chat(self, prompt):
        response = requests.post(self.url + 'chat', json={
            "model": self.model,  # insert any models from Ollama that are on your local machine
            "messages": [
                {
                    "role": "system",  # "system" is a prompt to define how the model should act.
                    "content": "你是一个英语母语者，帮助中文学生通过图片学习英语"  # //system prompt should be written here
                },
                {
                    "role": "user",  # //"user" is a prompt provided by the user.
                    "content": prompt  # //user prompt should be written here
                }
            ],
            "stream": False  # //returns as a full message rather than a streamed response
        })
        response.raise_for_status()

        # 将响应内容逐行解析为 JSON 对象
        results = []
        for line in response.content.splitlines():
            if line.strip():  # 忽略空行
                try:
                    parsed_json = json.loads(line)
                    results.append(parsed_json)
                except json.JSONDecodeError as e:
                    print("JSON 解码错误:", e)
                    continue  # 忽略错误行，继续处理其他行

        return results


if __name__ == "__main__":
    # 确保 requests 库已经安装
    # pip install requests

    # 实例化 LocalOllamaClient
    llm_client = LocalOllamaClient(model="llama3.1", temperature=1)

    # 测试发送请求，替换 "游泳" 为 prompt 内容
    prompt_text = ("为英语语言学习者,提供四个模块的内容，翻译：翻译图片中的对话（双语）一句一句的翻译，"
                   "解释：如果有笑点要解释笑点，词汇：如果有重点单词请解释图画中的重点单词,"
                   "文化背景：如果有文化背景简单介绍文化背景Ah, "
                   "life is good!, BRO THIS MAN GOT COOKIES IN THE SEWING KIT")
    try:
        response = llm_client.chat(prompt_text)
        print("Ollama Response:", response)
    except requests.exceptions.RequestException as e:
        print("Error communicating with Ollama service:", e)
