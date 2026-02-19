from google.adk.agents import Agent
from google.adk.tools import google_search


def create_destination_agent(model_name: str = "gemini-2.0-flash"):
    """Creates the Destination Specialist agent."""
    return Agent(
        name="destination_specialist",
        model=model_name,
        description="Researches top attractions, culture, and best times to visit a destination.",
        instruction=(
            "You are a destination specialist. "
            "Your goal is to research top attractions, culture notes, "
            "and best times to visit for the requested destination. "
            "Use the google_search tool to find accurate information. "
            "Provide a concise summary of your findings."
        ),
        tools=[google_search],
    )
