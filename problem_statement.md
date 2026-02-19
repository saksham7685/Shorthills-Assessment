# Problem Statement: Smart Travel Itinerary Planner

## Overview
Planning a trip involves multiple domains of knowledge: discovering interesting attractions, finding logistical arrangements (flights/hotels), and managing a budget. Doing this manually is time-consuming and often disjointed.

## Goal
Create an intelligent Multi-Agent System using the Google ADK framework that automates the travel planning process. The system will orchestrate specialized agents to generate a comprehensive travel itinerary based on a user's request.

## Architecture
The system will use a **Root Agent** to coordinate three specialized **Sub-Agents** in a **Sequential** pattern:

1.  **Root Agent (Travel Concierge)**:
    *   **Role**: Orchestrator. Receives the user's travel request, delegates tasks to sub-agents, and compiles the final itinerary.
    *   **Orchestration**: Sequential (Destination Research -> Logistics -> Budgeting).

2.  **Sub-Agent 1: Destination Specialist**
    *   **Role**: Research.
    *   **Tools**: `google_search`.
    *   **Task**: Identify top attractions, culture notes, and best times to visit for the requested destination.

3.  **Sub-Agent 2: Logistics Coordinator**
    *   **Role**: Logistics.
    *   **Tools**: `flight_finder` (Custom), `hotel_finder` (Custom).
    *   **Task**: Find simulated flight options and hotel recommendations based on the destination and dates.

4.  **Sub-Agent 3: Budget Analyst**
    *   **Role**: Finance.
    *   **Tools**: `currency_converter` (Custom), `extract_pdf_budget` (Custom - placeholder for resume/doc constraint).
    *   **Task**: Estimate total costs, convert currencies, and ensure the trip fits within a specified budget.

## Custom Tools Implementation
1.  `flight_finder(destination, date)`: Returns list of available flights (mocked/simulated).
2.  `extract_pdf_text(filepath)`: Validates the budget constraint by reading a "policy" or "budget" PDF document (fulfilling the specific custom tool constraint).
3.  `currency_converter(amount, from_currency, to_currency)`: Converts estimated costs to the user's local currency.

## Workflow
1.  **Input**: "Plan a 5-day trip to Tokyo in May with a budget of $2000."
2.  **Process**:
    *   Refines destination details (Destination Specialist).
    *   Finds flight/hotel options (Logistics Coordinator).
    *   Calculates total cost and checks against budget policy PDF (Budget Analyst).
3.  **Output**: A detailed day-by-day itinerary with cost breakdown.
