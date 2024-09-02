import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# ////////////////////////////////////////////////////
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkdin_profile

import streamlit as st

load_dotenv()

# ///////////////////// PROMPT TEMPLATE /////////////////////////
summary_temp = """Give a short summary and two interesting facts about a person based on the LinkedIn information provided: {information}"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_temp)
# --------------------------------------------------------------->>>>>>>>>>>>>>>>

# ////////////////// LLM models ////////////////////////////////
llm_edit = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), temperature=0, model_name="gpt-3.5-turbo")
# Uncomment and configure the model if needed
# llm_olama = ChatOllama(model="llama3")
# --------------------------------------------------------------->>>>>>>>>>>>

# /////////////Chain creation /////////////////////
chain = LLMChain(prompt=summary_prompt_template, llm=llm_edit)
# ---------------------->>>>>>>>>>>>>>>>>>>>>>

# Set up the title of the app
st.title("LINKDIN PROFILE SUMMARY APP BY HARSH ")

# Input field for LinkedIn URL
linkedin_url = st.text_input("Enter LinkedIn URL:")
if st.button("Submit"):
    if linkedin_url:
        try:
            linkedin_data = scrape_linkdin_profile(linkedin_url)
            response = chain.run(information=linkedin_data)
            st.text_area("Profile Summary", value=response, height=200)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a LinkedIn URL.")
