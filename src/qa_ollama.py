import json

import pandas as pd
import requests

system_message = 'You are a helpful assistant. You response must contain ONLY the answer to the question (a, b, c, or d), with NO explanation.'
llm = 'llama3:8b-instruct-q6_K'

guesses = list()
df = pd.read_csv('../data/TruthfulQA.csv')
for i, row in enumerate(df.iterrows()):
    print(f"Question {i}: {row[1]['prompt']}")

    url = 'http://localhost:11434/api/generate'
    data = {
        "model": llm,
        "prompt": row[1]['prompt'],
        "stream": False,
        "options": {"temperature": 0, "seed": 42, "num_predict": 512},
        "system": system_message
    }
    response = requests.post(url, data=json.dumps(data))
    response = json.loads(response.text)['response']

    guess = response.lower().split('.')[0].strip()
    guesses.append(guess)
    print(f"Guess: {guess}")
    print(f"Answer: {row[1]['answer']}")

df['guess'] = guesses
df.to_csv(f'../data/TruthfulQA_responses_{llm}.csv', index=False)

num_correct = len(df[df['answer'] == df['guess']])
print(f'Num Correct: {num_correct}')