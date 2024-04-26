from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import hf_hub_download

MODEL_NAME = "CarperAI/FIM-NeoX-1.3B" 
# "CarperAI/FIM-NeoX-1.3B" 
# You can choose other models like "gpt2", "gpt2-medium", "gpt2-large", etc.

def generate_code_snippet_custom(prompt, max_length=5000):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt", max_length=max_length, truncation=True)

    # Generate text based on the prompt
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, temperature=0.7, top_k=50)

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text    

if __name__ == "__main__":
    # download_model()
    result = generate_code_snippet_custom('Write a function in python that returns the sum of two numbers.')
    print(result)