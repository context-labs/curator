from bespokelabs.curator import LLM


# View all available models at https://docs.inference.net/resources/models
llm = LLM(model_name="meta-llama/llama-3.1-8b-instruct/fp-16", backend="inference.net", backend_params={"max_retries": 1})

response = llm("Write a short story about a dog and a cat.")
print(response[0]["response"])
