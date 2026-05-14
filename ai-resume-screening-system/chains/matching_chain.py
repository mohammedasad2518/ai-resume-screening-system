from transformers import pipeline
from langchain_core.runnables import RunnableLambda
from prompts.match_prompt import match_prompt

generator = pipeline("text-generation", model="gpt2")  # type: ignore

def run_llm(prompt):
    prompt_str = prompt.to_string()  
    return generator(prompt_str, max_length=150, do_sample=False)[0]["generated_text"]

llm = RunnableLambda(run_llm)

matching_chain = (match_prompt | llm).with_config(tags=["matching"])