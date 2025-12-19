import streamlit as st
import json
import asyncio
from google import genai
from google.genai import types

# --- 1. Setup & Secrets ---
st.set_page_config(page_title="Reasoning Agent", page_icon="🤖")

# Streamlit automatically finds the key in .streamlit/secrets.toml
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("Missing API Key! Please check .streamlit/secrets.toml")
    st.stop()

MODEL_ID = "gemini-3-flash-preview"

# --- 2. Reasoning Agent Core ---
class ReasoningAgent:
    def __init__(self, client):
        self.client = client

    async def _call_llm(self, sys_inst, prompt):
        response = self.client.models.generate_content(
            model=MODEL_ID,
            config=types.GenerateContentConfig(system_instruction=sys_inst, temperature=0.1),
            contents=prompt
        )
        return response.text

    async def solve(self, question):
        # Phase 1: Planning
        plan = await self._call_llm("You are a Planner. Create a numbered list of steps.", question)
        
        # Phase 2: Executing
        exec_prompt = f"Question: {question}\nPlan: {plan}\nSolve it. End with 'Final Answer: <val>'"
        execution = await self._call_llm("You are an Executor. Follow the plan exactly.", exec_prompt)
        
        # Phase 3: Verifying
        ver_prompt = f"Question: {question}\nProposed Solution: {execution}"
        ver_raw = await self._call_llm("You are a Verifier. Output JSON: {'passed': bool, 'details': str}", ver_prompt)
        
        passed = "true" in ver_raw.lower()
        return {
            "answer": execution.split("Final Answer:")[-1].strip() if "Final Answer:" in execution else "N/A",
            "status": "success" if passed else "failed",
            "reasoning": execution.split("Final Answer:")[0].strip(),
            "metadata": {"plan": plan, "verifier_details": ver_raw}
        }

# --- 3. Streamlit Interface ---
st.title("🤖 Multi-Step Reasoning Agent")
st.markdown("---")

user_input = st.text_input("Enter your math/logic question:", placeholder="e.g. If I have 5 apples and eat 2, how many are left?")

if st.button("Run Reasoning Agent"):
    if user_input:
        with st.spinner("🧠 Thinking... (Planning -> Executing -> Verifying)"):
            agent = ReasoningAgent(client)
            # Use asyncio.run for local streamlit
            result = asyncio.run(agent.solve(user_input))
            
            # Display Main Result
            st.success(f"Final Answer: {result['answer']}")
            st.write(result['reasoning'])
            
            # Debug Data Section
            with st.expander("🔍 Internal Reasoning Logs (Debug Data)"):
                st.json(result)
    else:
        st.warning("Please enter a question first.")