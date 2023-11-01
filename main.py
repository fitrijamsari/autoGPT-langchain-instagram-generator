# Import the necessary library
import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory, SimpleMemory
from langchain.prompts import PromptTemplate
from langchain.utilities import WikipediaAPIWrapper

# Load variables from the .env file
load_dotenv()

# Access the variables using os.environ
api_key = os.getenv("OPENAI_API_KEY")

# Streamlit Apps Framework
st.title("🦜️🔗 Instagram Post Generator")
prompt = st.text_input("What title of the instagram post you want to generate?")

# prompt templates
title_template = PromptTemplate(
    input_variables=["topic"],
    template="write me a post title {topic} for my instagram post",
)
script_template = PromptTemplate(
    input_variables=["title", "wikipedia_research"],
    template=(
        "You a social media content creater. Write me a full instagram post script"
        " based on this TITLE: {title} while leveraging this wikipedia"
        " research:{wikipedia_research} in a professional tone"
    ),
)

# Memory
# memory = ConversationBufferMemory(input_key="topic", memory_key="chat_history")
title_memory = ConversationBufferMemory(input_key="topic", memory_key="chat_history")
script_memory = ConversationBufferMemory(input_key="title", memory_key="chat_history")


# llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(
    llm=llm,
    prompt=title_template,
    verbose=True,
    output_key="title",
    memory=title_memory,
)
script_chain = LLMChain(
    llm=llm,
    prompt=script_template,
    verbose=True,
    output_key="script",
    memory=script_memory,
)

wiki = WikipediaAPIWrapper()

# No need SequantialChain in this case since we just want to run the prompt and result independently

# # NOTE: SimpleSequentialChain only provide the last output, but SequentialChain will output all outputs
# sequential_chain = SequentialChain(
#     chains=[title_chain, script_chain],
#     verbose=True,
#     input_variables=["topic"],
#     output_variables=["title", "script"],
# )

# show to screen if threre is a prompt
if prompt:
    # response = sequential_chain({"topic": prompt})
    # st.write(response["title"])
    # st.write(response["script"])

    # with st.expander("See all the outputs"):
    #     st.info(memory.buffer)

    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    st.write(script)

    with st.expander("Title History"):
        st.info(title_memory.buffer)

    with st.expander("Script History"):
        st.info(script_memory.buffer)

    with st.expander("Wikipedia Research"):
        st.info(wiki_research)
