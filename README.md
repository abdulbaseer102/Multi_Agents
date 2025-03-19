# Multi-Agent System using OpenAI SDK & Gemini API

## Overview
This project implements a sophisticated multi-agent system using the OpenAI SDK and Gemini API. The system consists of multiple specialized AI agents, each designed to handle a specific domain or task. The architecture is built using **Chainlit** for interactive conversations and **OpenAI SDK** for agent functionalities.

## Features
- **Multiple Specialized Agents**:
  - `Triage Agent`: Routes user queries to appropriate agents.
  - `History Tutor Agent`: Answers historical questions.
  - `OpenAI SDK Expert`: Guides users on OpenAI SDK framework.
  - `Code Writer Agent`: Writes clean and efficient code.
  - `Global Knowledge Agent`: Provides general knowledge.
  - `Pakistan Info Agent`: Gives details about Pakistan.
  - `Girlfriend Agent`: Simulates a friendly and engaging conversational partner.
- **Custom Tool Support**: Agents can use tools like web search or code execution.
- **Context Management**: Maintains chat history for personalized responses.
- **Streaming Responses**: Provides real-time interaction.
- **Secure API Handling**: Uses environment variables for API keys.

## Technologies Used
- **Python 3.x**
- **OpenAI SDK** (Using Gemini API for model inference)
- **Chainlit** (For chat interface)
- **Pydantic** (For structured data validation)
- **AsyncOpenAI** (Asynchronous API handling)
- **Dotenv** (For managing environment variables)

## Installation & Setup
### Prerequisites
Ensure you have Python 3.8+ installed.

### Clone the Repository
```bash
git clone https://github.com/yourusername/multi-agent-system.git
cd multi-agent-system
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up API Keys
Create a `.env` file in the root directory and add the following:
```ini
GEMINI_API_KEY=your_gemini_api_key_here
```

### Run the Multi-Agent System
```bash
chainlit run agent.py
```

## How It Works
1. **User Interaction**: The system starts with the `Triage Agent` which routes queries.
2. **Agent Selection**: Based on user input, the query is forwarded to the appropriate agent.
3. **Processing & Response**:
   - The agent processes the request using **Gemini API**.
   - It retrieves historical context if needed.
   - The response is streamed back to the user in real-time.

## Agent Descriptions
### `Triage Agent`
- Acts as a central dispatcher.
- Routes user queries to the correct agent.

### `History Tutor Agent`
- Specializes in historical events and context.

### `OpenAI SDK Expert`
- Provides guidance on OpenAI SDK and AI development.

### `Code Writer Agent`
- Generates high-quality, well-structured code.
- Can suggest improvements and best practices.

### `Global Knowledge Agent`
- Answers general knowledge questions.

### `Pakistan Info Agent`
- Provides real-time information about Pakistan.

### `Girlfriend Agent`
- Engages in friendly and conversational interactions.

## Troubleshooting
### Common Issues & Fixes
| Issue | Solution |
|--------|---------|
| `GEMINI_API_KEY is not set` | Ensure `.env` file contains a valid API key. |
| `ModuleNotFoundError: No module named 'chainlit'` | Run `pip install chainlit` |
| `Error: 'ResponseCreatedEvent' object has no attribute 'delta'` | Ensure correct OpenAI SDK version is installed. |
| `for` loop indentation error | Check indentation on `for event in result.stream_events():` |

## Future Enhancements
- **Multi-modal capabilities** (text, image, video processing)
- **Memory persistence for long-term context tracking**
- **Integration with external APIs** (Google Search, Wolfram Alpha, etc.)

## License
This project is licensed under the MIT License.

## Contributors
- **Abdul Baseer** - Developer

## Contact
For any queries or issues, feel free to reach out via **baseek8@gmail.com**.

