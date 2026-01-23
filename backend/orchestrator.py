from backend.agents.category_agent import category_agent
from backend.agents.messaging_agent import messaging_agent
from backend.agents.visual_agent import visual_agent
from backend.agents.styling_agent import styling_agent
from backend.agents.synthesizer_agent import synthesizer_agent
from backend.agents.qa_agent import qa_agent
from backend.agents.prompt_generation import llm_prompt_generator

def generate_poster_prompt(project: dict, creative: dict):
    strategy = category_agent(creative["category"])
    messaging = creative["headline"]
    visual = visual_agent(
        creative["category"],
        background_provided=bool(creative["bg_file_path"])
    )
    styling = styling_agent()

    synthesized_prompt = synthesizer_agent(
        project, creative, strategy, visual, styling, messaging
    )

    prompt = llm_prompt_generator(synthesized_prompt, creative["bg_file_path"])

    return qa_agent(prompt)
