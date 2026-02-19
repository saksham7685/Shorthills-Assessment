from google.adk.agents import Agent
from ..tools.custom_tools import extract_pdf_budget, currency_converter


def create_budget_agent(model_name: str = "gemini-2.0-flash"):
    """Creates the Budget Analyst agent."""
    return Agent(
        name="budget_analyst",
        model=model_name,
        description="Estimates total trip costs, converts currencies, and checks budget constraints.",
        instruction=(
            "You are a budget analyst. Estimate total costs, convert currencies, "
            "and ensure the trip fits within a specified budget. "
            "Use the extract_pdf_budget tool to check for policy constraints, "
            "and currency_converter for calculations. "
            "Provide a clear cost breakdown."
        ),
        tools=[extract_pdf_budget, currency_converter],
    )
