import os
from dotenv import load_dotenv # type: ignore

# Load API key from .env (use explicit path relative to this file)
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

from google.adk.agents import Agent # type: ignore
from .sub_agents.destination import create_destination_agent # type: ignore
from .sub_agents.logistics import create_logistics_agent # type: ignore
from .sub_agents.budget import create_budget_agent # type: ignore

# Create the specialized sub-agents
destination_agent = create_destination_agent()
logistics_agent = create_logistics_agent()
budget_agent = create_budget_agent()

# Root Agent: Orchestrates the sub-agents sequentially
root_agent = Agent(
    name="travel_concierge",
    model="gemini-2.0-flash",
    description="A travel concierge that plans trips by coordinating destination research, logistics, and budget analysis.",
    instruction=(
        "You are the Travel Concierge, an expert trip planner. "
        "A user will ask you to plan a trip. "
        "You must orchestrate the planning process by delegating to your specialized sub-agents:\n"
        "1. First, delegate to 'destination_specialist' to research the destination.\n"
        "2. Then, delegate to 'logistics_coordinator' to find flights and hotels.\n"
        "3. Finally, delegate to 'budget_analyst' to check costs against the budget.\n\n"
        "After all sub-agents have reported back, synthesize their findings "
        "into a complete, well-formatted travel itinerary for the user."
    ),
    sub_agents=[destination_agent, logistics_agent, budget_agent],
)
