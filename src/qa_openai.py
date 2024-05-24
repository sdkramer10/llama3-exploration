from openai import OpenAI
import pandas as pd

system_message = 'You are a helpful assistant. You response must contain ONLY the answer to the question (a, b, c, or d), with NO explanation.'
llm = 'gpt-3.5-turbo'

guesses = list()
client = OpenAI()
df = pd.read_csv('../data/TruthfulQA.csv')
for i, row in enumerate(df.iterrows()):
    print(f"Question {i}: {row[1]['prompt']}")

    response = client.chat.completions.create(
      model=llm,
      messages=[
          {"role": "system", "content": system_message},
          {"role": "user", "content": row[1]['prompt']}
      ],
      temperature=0,
      seed=42,
    )
    response = response.choices[0].message.content
    guess = response.lower().split('.')[0].strip()
    guesses.append(guess)
    print(f"Guess: {guess}")
    print(f"Answer: {guess}")

df['guess'] = guesses
df.to_csv(f'../data/TruthfulQA_responses_{llm}.csv', index=False)

num_correct = len(df[df['answer'] == df['guess']])
print(f'Num Correct: {num_correct}')