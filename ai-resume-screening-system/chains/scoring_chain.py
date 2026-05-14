from transformers import pipeline
from langchain_core.runnables import RunnableLambda
from prompts.score_prompt import score_prompt

generator = pipeline("text-generation", model="gpt2")  # type: ignore

def run_llm(prompt):
    prompt_str = prompt.to_string() 
    return generator(prompt_str, max_length=100, do_sample=False)[0]["generated_text"]

llm = RunnableLambda(run_llm)

scoring_chain = (score_prompt | llm).with_config(tags=["scoring"])