# MixiBot

MixiBot is a chatbot application built with [Streamlit](https://streamlit.io/) and [LangChain](https://github.com/hwchase17/langchain). It leverages OpenAI's GPT-3.5-turbo and the YouTube Data API to interact with YouTube channels. MixiBot can fetch the latest videos from a specified YouTube channel, retrieve video details (such as title, link, and view count).

## Features

- **Chat Interface:**  
  A user-friendly chat interface built with Streamlit.
- **YouTube Integration:**  
  Retrieve the latest videos from a YouTube channel using the YouTube Data API.
- **Extensible Tools:**  
  Built on LangChain's modular tools framework, making it easy to add new functionalities.

## Repository Structure
```bash
├── MixiBot/
  ├── app.py # Main Streamlit application entry point
  ├── functions.py # Functions to interact with YouTube API
  ├── tool.py # LangChain tool definitions for YouTube interactions
  ├── .env # Environment variables (create locally; do not commit)
  ├── requirements.txt # Python dependencies
  ├── README.md
```
## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Quyet160903/MixiBot.git
cd MixiBot
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a <b>.env</b>
file in the project root with the following content:
```bash
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_YOUTUBE_API_KEY=your_youtube_api_key_here
```

## Running the Application
To start MixiBot, run:
```bash
streamlit run app.py
```

### Tools: Streamlit, Langchain, Pydantic, OpenAI

### Result:
![image](https://github.com/user-attachments/assets/1493cf8c-b28a-4ab6-a793-48b51bfb84aa)

