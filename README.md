# 🤖 Multi-Step Reasoning Agent

A sophisticated AI agent built with **Streamlit** and **Gemini 3** that utilizes a multi-stage reasoning architecture (**Planner -> Executor -> Verifier**) to solve complex logic and mathematical problems with high traceability and reduced hallucinations.

---

## ✨ Key Features

* **Multi-Stage Reasoning Loop**: Unlike standard chatbots, this agent follows a structured cognitive process:
    * **The Planner**: Breaks down the query into logical, sequential steps.
    * **The Executor**: Carries out the plan to find a solution.
    * **The Verifier**: Audits the result for logical consistency before final delivery.
* **Interpretations & Debugging**: A dedicated transparency layer that exposes the agent's internal thought process.
* **Traceable Logs**: View the raw JSON metadata for every interaction to understand exactly how the agent reached its conclusion.
* **User-Centric UI**: Built with Streamlit for a clean, interactive experience.

---

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **AI Model**: Google Gemini 3 (Flash Preview)
* **Language**: Python 3.10+
* **Core Library**: `google-genai`

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* A Google Gemini API Key ([Get one here](https://aistudio.google.com/))

### Installation & Local Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/multi-step-reasoning-agent.git](https://github.com/your-username/multi-step-reasoning-agent.git)
    cd multi-step-reasoning-agent
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Secrets**
    Create a folder named `.streamlit` and a file named `secrets.toml` inside it:
    ```toml
    # .streamlit/secrets.toml
    GEMINI_API_KEY = "your_actual_api_key_here"
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## 🔍 How It Works (The Architecture)

This project demonstrates an **Agentic Workflow** where the model acts as its own supervisor to improve accuracy.

1.  **User Input**: The question is received via the Streamlit interface.
2.  **Planning Phase**: The `Planner` agent generates a `numbered_plan` to solve the problem.
3.  **Execution Phase**: The `Executor` follows the plan step-by-step and provides a `Final Answer`.
4.  **Verification Phase**: The `Verifier` performs a secondary audit. If the check fails, the UI flags the result as inconsistent.



---

## 🤝 Contributing
Feel free to fork this project, open issues, or submit pull requests. I am always looking for ways to improve the verification logic!

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
