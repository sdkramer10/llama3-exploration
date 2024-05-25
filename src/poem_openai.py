from openai import OpenAI
import pandas as pd

system_message = 'You are a professional poet. Write a unique and original poem about the topic suggested by the user. Your response should contain ONLY the contents of the poem.'
llm = 'gpt-3.5-turbo'

responses = list()
client = OpenAI()
df = pd.read_csv('../data/poem_topics.csv')
for i, row in enumerate(df.iterrows()):
    print(f"Topic {i}: {row[1]['topic']}")

    response = client.chat.completions.create(
      model=llm,
      messages=[
          {"role": "system", "content": system_message},
          {"role": "user", "content": row[1]['topic']}
      ],
      seed=42,
    )
    response = response.choices[0].message.content
    responses.append(response)

df['poem'] = responses
df.to_csv(f'../data/poem_responses_{llm}.csv', index=False)