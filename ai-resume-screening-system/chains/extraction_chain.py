from transformers import pipeline
from langchain_core.runnables import RunnableLambda
from prompts.extract_prompt import extract_prompt

generator = pipeline("text-generation", model="gpt2")  # type: ignore

def run_llm(prompt):
    prompt_str = prompt.to_string()  
    return generator(prompt_str, max_length=150, do_sample=False)[0]["generated_text"]

llm = RunnableLambda(run_llm)

extraction_chain = (extract_prompt | llm).with_config(tags=["extraction"])