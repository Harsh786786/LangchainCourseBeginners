from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkdin_profile
import os
load_dotenv()

# ///////////////////// PROMPT TEMPLATE /////////////////////////
summary_temp =  """  give the Linkedin  information  {information} about a person
 from i want to create 
 1. a short summary
 2. two intreasting facts about them"""

summary_prompt_tempelate = PromptTemplate(input_variables="information", template=summary_temp)
# --------------------------------------------------------------->>>>>>>>>>>>>>>>

# ////////////////// LLM models ////////////////////////////////
llm_edit  =  ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'),temperature=0, model_name="gpt-3.5-turbo")
# llm_olama  =  ChatOllama(model="llama3")
# --------------------------------------------------------------->>>>>>>>>>>>


# /////////////Chain creation /////////////////////
chain = summary_prompt_tempelate | llm_edit
# ---------------------->>>>>>>>>>>>>>>>>>>>>>

linkedin_data = scrape_linkdin_profile(linkedin_url="https://www.linkedin.com/in/harshverma0/")
response = chain.invoke(input={"information":linkedin_data})

print(response)