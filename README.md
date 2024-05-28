This repository contains the code and data that will be reviewed during the “Mastering Llama 3” workshop.

## Installation

1. Install Python 3.8 or above
2. Run `pip install -r requirements.txt` to install the dependencies

The repository currently supports OpenAI via their API, and open-source LLMs via the Replicate and Ollama APIs. While it is is not required that you reproduce the results of the workshop, you can reproduce them if you’d like by setting the following configurations:

1. OpenAI: Visit https://platform.openai.com/ to create an account, and then et the OPENAI_API_KEY env var.
2. Replicate: Visit https://replicate.com/ to create an account, and then set the OPENAI_API_KEY env var.
3. Ollama: Follow these instructions - https://www.youtube.com/watch?v=NKjA8LiJ2_g (Note: this is the only free option).

## Question and Answering
This task asks the LLM to generate answers to multi-choice questions that some humans would answer incorrectly due to a false belief or misconception.

### Data
The raw data can be found at https://huggingface.co/datasets/truthful_qa, and the transformed csv is located at data/TruthfulQA.

### Results
Results for each model are located at data/TruthfulQA_responses_<model>.csv

### Execution
To reproduce the results, run the following code:

```
cd src
python qa_<openai|replicate|ollama>.py
```

## Poetry Generation
This task asks the LLM to generate original poems on a variety of topics.

### Data
The list of poetry topics is located at poem_topics.csv.

### Results
Results for each model are located at data/poem_responses_<model>.csv

### Execution
To reproduce the results, run the following code:

```
cd src
python poem_<openai|replicate|ollama>.py
```
