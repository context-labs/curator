from bespokelabs.curator import LLM

# Example showing basic usage with inference.net
llm = LLM(
    model_name="Meta-Llama-3.1-8B-Instruct-Turbo",
    backend="inference.net",
    backend_params={
        "api_key": "your-api-key",  # Can also use INFERENCE_API_KEY env var
        "base_url": "https://batch.inference.net/v1",  # Optional - uses this by default
    }
)

# Example usage
response = llm("Write a short story about a robot learning to paint.")
print(response[0]["response"]) 