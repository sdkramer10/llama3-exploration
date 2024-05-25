import json

import pandas as pd
import requests

system_message = 'You are a professional poet. Write a unique and original poem about the topic suggested by the user. Your response should contain ONLY the contents of the poem.'
llm = 'llama3:8b-instruct-q6_K'
url = 'http://localhost:11434/api/generate'

responses = list()
df = pd.read_csv('../data/poem_topics.csv')
for i, row in enumerate(df.iterrows()):
    print(f"Topic {i}: {row[1]['topic']}")

    data = {
        "model": llm,
        "prompt": row[1]['topic'],
        "stream": False,
        "options": {"seed": 42, "num_predict": 2048},
        "system": system_message
    }
    response = requests.post(url, data=json.dumps(data))
    response = json.loads(response.text)['response']

    responses.append(response)

df['poem'] = responses
df.to_csv(f'../data/poem_responses_{llm}.csv', index=False)