from bespokelabs.curator import LLM
from typing import List
from pydantic import BaseModel

# Example showing batch processing with structured output
class Story(BaseModel):
    title: str
    content: str
    moral: str

prompts = [
    "Write a story about friendship",
    "Write a story about perseverance",
    "Write a story about creativity"
]

llm = LLM(
    model_name="Meta-Llama-3.1-8B-Instruct-Turbo",
    response_format=Story,  # Enable structured output
    batch=True,  # Enable batch processing
    backend="inference.net",
    backend_params={
        "api_key": "your-api-key",  # Can also use INFERENCE_API_KEY env var
        "base_url": "https://batch.inference.net/v1",  # Optional - uses this by default
        "batch_size": 10,  # Process 10 prompts at a time
    }
)

# Process multiple prompts in parallel
responses = llm(prompts)
for story in responses:
    print(f"\nTitle: {story['title']}")
    print(f"Content: {story['content']}")
    print(f"Moral: {story['moral']}") 