from google.adk.agents import Agent
from ..tools.custom_tools import flight_finder, hotel_finder


def create_logistics_agent(model_name: str = "gemini-2.0-flash"):
    """Creates the Logistics Coordinator agent."""
    return Agent(
        name="logistics_coordinator",
        model=model_name,
        description="Finds flight options and hotel recommendations for a trip.",
        instruction=(
            "You are a logistics coordinator. Find simulated flight options and hotel recommendations "
            "based on the destination and dates provided. "
            "Use flight_finder and hotel_finder tools to get options. "
            "Present the results clearly."
        ),
        tools=[flight_finder, hotel_finder],
    )
