from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["resume_data", "match_data", "score"],
    template="""
Based on the resume evaluation:

Explain why this candidate received the given score.

Include:
- Strengths (matching skills)
- Weaknesses (missing skills)
- Final justification

Keep it clear and concise.

Score: {score}

Resume Data:
{resume_data}

Match Data:
{match_data}
"""
)