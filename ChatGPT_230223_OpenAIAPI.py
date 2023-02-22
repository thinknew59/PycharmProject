import openai
import requests

# OpenAI API Key를 설정합니다.
openai.api_key = 'YOUR_API_KEY'

# ChatGPT 모델의 ID를 설정합니다.
model_id = 'davinci'

# ChatGPT 모델에 입력할 문장을 설정합니다.
prompt = 'Hello, how are you?'

# API 호출 시 필요한 옵션을 설정합니다.
payload = {
    "model": model_id,
    "prompt": prompt,
    "temperature": 0.5,
    "max_tokens": 100
}

# API를 호출합니다.
response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', json=payload)

# API 호출 결과에서 ChatGPT 모델의 출력을 확인합니다.
output = response.json()['choices'][0]['text']
print(output)