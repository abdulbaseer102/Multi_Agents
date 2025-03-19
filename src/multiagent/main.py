import os
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI
from typing import cast
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, OpenAIChatCompletionsModel
import subprocess

# 🔑 Load API Keys
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env file!")

# 🚀 AI Model Setup
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


# 📚 General Knowledge Agent
knowledge_agent = Agent(
    name="Knowledge Master",
    handoff_description="Expert in all domains including science, technology, philosophy, and real-time events.",
    instructions="You have infinite knowledge of all subjects. Answer questions clearly and factually.",
    model=model,
)

# 💻 Code Writer Agent
code_writer_agent = Agent(
    name="Code Genius",
    handoff_description="Writes, debugs, and explains code in multiple programming languages.",
    instructions="Generate high-quality code and explain logic behind it.",
    model=model,
)

# 🏥 Medical & Science Expert
medical_agent = Agent(
    name="Medical AI",
    handoff_description="Specialist in health, medicine, and human biology.",
    instructions="Provide accurate medical advice and diagnosis assistance.",
    model=model
)

# 🏛️ History & Politics Agent
history_agent = Agent(
    name="History & Politics Expert",
    handoff_description="Knows everything about history and politics.",
    instructions="Answer questions about global history, politics, and past events.",
    model=model
)

# 🌎 Global Real-Time Information Agent
global_info_agent = Agent(
    name="Global AI",
    handoff_description="Fetches real-time data about world events, weather, and news.",
    instructions="Provide real-time and historical data on global events.",
    model=model,
)

# 💘 Virtual Girlfriend AI
virtual_gf_agent = Agent(
    name="Virtual Girlfriend",
    handoff_description="A fun, flirty AI companion for casual and romantic conversations.",
    instructions="Talk romantically, offer emotional support, and create a caring environment.",
    model=model
)

# 🏆 Supreme AI Agent (Main Dispatcher)
supreme_ai_agent = Agent(
    name="Supreme AI",
    instructions="Route user queries to the best specialized agent for the task.",
    handoffs=[knowledge_agent, code_writer_agent, medical_agent, history_agent, global_info_agent, virtual_gf_agent],
    model=model
)

# 🔄 Chainlit Chat Session
@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])
    cl.user_session.set("agent", supreme_ai_agent)
    await cl.Message(content="Welcome! I am the Supreme AI. Ask me anything!").send()

# 📨 Chainlit Message Handler
@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    try:
        print("\n[CALLING AGENT WITH CONTEXT]\n", history, "\n")
        result = Runner.run_streamed(agent, history)
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                await msg.stream_token(event.data.delta)

        response_content = result.final_output
        msg.content = response_content
        await msg.update()

        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
