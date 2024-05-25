import pandas as pd
import replicate

system_message = 'You are a professional poet. Write a unique and original poem about the topic suggested by the user. Your response should contain ONLY the contents of the poem.'
llm = 'meta-llama-3-8b-instruct'

responses = list()
df = pd.read_csv('../data/poem_topics.csv')
for i, row in enumerate(df.iterrows()):
    print(f"Topic {i}: {row[1]['topic']}")

    response = replicate.run(
        f'meta/{llm}',
        input={
            "prompt": row[1]['topic'],
            "max_tokens": 2048,
            "system_prompt": system_message,
            "log_performance_metrics": False,
            "seed": 42,
        },
    )
    response = ''.join(response)
    responses.append(response)

df['poem'] = responses
df.to_csv(f'../data/poem_responses_{llm}.csv', index=False)