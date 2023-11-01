# INTRODUCTION

- Purpose: To automate an instagram post title and description generator.
- General Description: The project will enable autoGPT for instagram post with just typing the TOPIC or TITLE. You do not need to write the whole words since the project already set the suitable prompt template with the TITLE as the prompt input.
- Technology Stack: OpenAI, Langchain, Streamlit, WikipediaResearch

## INSTALLATION

1. Setup a new conda environment

```
conda create --name ENV_NAME
```

2. Install the environment dependencies

```
pip install streamlit langchain openai wikipedia chromadb tiktoken
```

or

```
pip install -r requirements.txt
```

3. Create .env file and insert your own OPENAI_APIKEY

```
OPENAI_API_KEY=""
```

4. Run the code on streamlit

```
streamlit run main.py
```
