from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
Based on matching data, assign a score from 0 to 100.

Rules:
- More matching skills = higher score
- More missing skills = lower score

Return only:
Score: <number>

Data:
{match_data}
"""
)