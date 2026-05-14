from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job_desc"],
    template="""
Compare resume with job description.

Find:
- Matching Skills
- Missing Skills

Format:
Matching Skills: <comma-separated>
Missing Skills: <comma-separated>

Resume Data:
{resume_data}

Job Description:
{job_desc}
"""
)