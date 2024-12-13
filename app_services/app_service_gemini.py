import vertexai
import streamlit as st
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
import app_config as app_config


generation_config = {
    "max_output_tokens": app_config.MAX_OUTPUT_TOKENS,
    "temperature": app_config.TEMPERATURE,
    "top_p": 0.95,
}

def call_llm(selected_region, msg,data,persona):

    region = selected_region if selected_region else "us-west1"

    vertexai.init(project=app_config.PROJECT_ID, location=region)
        
    model = GenerativeModel(
        app_config.LLM_MODEL,
        system_instruction=[persona]
    )    

    prompt=[]

    prompt.append(msg)

    if(data):
       prompt.append(data)

    response = model.generate_content(
        prompt,
        generation_config=generation_config,
        stream=False,
    )

    return response.text