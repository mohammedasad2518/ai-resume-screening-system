from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract the following from the resume:

- Skills
- Experience
- Tools

Rules:
- Only extract what is present
- Do not assume anything

Format:
Skills: <comma-separated>
Experience: <text>
Tools: <comma-separated>

Resume:
{resume}
"""
)