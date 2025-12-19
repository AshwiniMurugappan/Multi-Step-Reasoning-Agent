# 🤖 Multi-Step Reasoning Agent

A sophisticated AI agent built with **Streamlit** and **Gemini 3** that utilizes a multi-stage reasoning architecture (Planner -> Executor -> Verifier) to solve complex logic and mathematical problems with high traceability.

![Streamlit App Screenshot](https://your-image-link-here.com/screenshot.png) 
*(Tip: Replace this link with a screenshot of your app once it's running)*

## ✨ Key Features

- **Multi-Stage Reasoning Loop**: Unlike standard chatbots, this agent follows a structured cognitive process:
  - **The Planner**: Breaks down the query into logical, sequential steps.
  - **The Executor**: Carries out the plan to find a solution.
  - **The Verifier**: Audits the result for logical consistency before final delivery.
- **Interpretations & Debugging**: A dedicated transparency layer that exposes the agent's internal thought process and "Status: Success/Failed" flags.
- **Traceable Logs**: View the raw JSON metadata for every interaction to understand exactly how the agent reached its conclusion.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: Google Gemini 3 (Flash Preview)
- **Language**: Python 3.10+
- **Protocol**: Asyncio for non-blocking agent calls

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- A Google Gemini API Key ([Get one here](https://aistudio.google.com/))

### Installation & Local Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/multi-step-reasoning-agent.git](https://github.com/your-username/multi-step-reasoning-agent.git)
   cd multi-step-reasoning-agent
