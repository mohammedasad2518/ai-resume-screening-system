from transformers import pipeline
from langchain_core.runnables import RunnableLambda
from prompts.explain_prompt import explain_prompt

generator = pipeline("text-generation", model="gpt2")  # type: ignore

def run_llm(prompt):
    prompt_str = prompt.to_string()
    return generator(prompt_str, max_length=200, do_sample=False)[0]["generated_text"]

llm = RunnableLambda(run_llm)

explanation_chain = (explain_prompt | llm).with_config(tags=["explanation"])