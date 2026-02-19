# Travel Concierge — Multi-Agent Trip Planner

A multi-agent travel planning system built with the **Google Agent Development Kit (ADK)**. The system orchestrates three specialized sub-agents to research destinations, find flights and hotels, and analyze budgets — producing a complete travel itinerary in one conversation.

## Architecture

```
travel_concierge/
├── agent.py                  # Root agent — orchestrates the sub-agents
├── sub_agents/
│   ├── destination.py        # Destination Specialist (uses Google Search)
│   ├── logistics.py          # Logistics Coordinator (flights & hotels)
│   └── budget.py             # Budget Analyst (costs & currency conversion)
├── tools/
│   └── custom_tools.py       # Custom tools (flight_finder, hotel_finder, etc.)
└── .env                      # API key (not tracked by git)
```

### Sub-Agents

| Agent | Role | Tools |
|---|---|---|
| **Destination Specialist** | Researches attractions, culture, and best times to visit | `google_search` |
| **Logistics Coordinator** | Finds flight options and hotel recommendations | `flight_finder`, `hotel_finder` |
| **Budget Analyst** | Estimates costs, converts currencies, checks budget constraints | `extract_pdf_budget`, `currency_converter` |

## Prerequisites

- **Python 3.10+**
- A **Google Gemini API key** — get one at [Google AI Studio](https://aistudio.google.com/apikey)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/saksham7685/Shorthills-Assesment.git
cd Shorthills-Assesment
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file inside the `travel_concierge/` directory:

```
GOOGLE_API_KEY=your_api_key_here
```

> Replace `your_api_key_here` with your actual Gemini API key.

## How to Run the Agent

Start the agent using the ADK CLI:

```bash
adk web
```

This launches the ADK web interface. Select **`travel_concierge`** from the agent list and start chatting.

### Example Prompt

```
Plan a 5-day trip to Tokyo from New York for 2 people with a budget of $3000.
```

The root agent will automatically:
1. Delegate to the **Destination Specialist** to research Tokyo
2. Delegate to the **Logistics Coordinator** to find flights and hotels
3. Delegate to the **Budget Analyst** to verify costs fit within $3000
4. Synthesize everything into a complete travel itinerary

## Tech Stack

- [Google ADK](https://google.github.io/adk-docs/) — Agent Development Kit
- [Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/) — LLM backbone
- Python 3.10+
