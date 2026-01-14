from backend.constants import NEGATIVE_PROMPT

def qa_agent(prompt):
    return {
        "final_prompt": prompt,
        "negative_prompt": NEGATIVE_PROMPT
    }
