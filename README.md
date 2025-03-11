# MixiBot

MixiBot is a chatbot application built with [Streamlit](https://streamlit.io/) and [LangChain](https://github.com/hwchase17/langchain). It leverages OpenAI's GPT-3.5-turbo and the YouTube Data API to interact with YouTube channels. MixiBot can fetch the latest videos from a specified YouTube channel, retrieve video details (such as title, link, and view count), and even summarize a video's main content.

## Features

- **Chat Interface:**  
  A user-friendly chat interface built with Streamlit.
- **YouTube Integration:**  
  Retrieve the latest videos from a YouTube channel using the YouTube Data API.
- **Extensible Tools:**  
  Built on LangChain's modular tools framework, making it easy to add new functionalities.

## Repository Structure
```bash
MixiBot/
  ├── app.py # Main Streamlit application entry point
  ├── functions.py # Functions to interact with YouTube API and summarize videos
  ├── tool.py # LangChain tool definitions for YouTube interactions
  ├── .env # Environment variables (create locally; do not commit)
  ├── requirements.txt # Python dependencies
```


