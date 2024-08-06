import os
import tiktoken
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import ConfigurableField

# models
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatOpenAI(temperature=0).configurable_fields(
    model_name=ConfigurableField(
        id="model_name",
        name="Model Name",
        description="The model name of the LLM",
    )
)

response = model.invoke("あなたのモデルバージョンを教えてください。")
print(response)

response = model.with_config(configurable={"model_name": "gpt-4o"}).invoke("あなたのバージョンを教えてください。")
print(response)
