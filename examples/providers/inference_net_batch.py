from bespokelabs import curator

# View all available models at https://docs.inference.net/resources/models
# inference.net currently only supports a 24h completion window
llm = curator.LLM(
    model_name="meta-llama/llama-3.1-8b-instruct/fp-16", backend="inference.net", batch=True, backend_params={"max_retries": 1, "completion_window": "24h"}
)

response = llm("What is the capital of Montana?")
print(response["response"])
