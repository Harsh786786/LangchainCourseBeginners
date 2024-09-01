from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from secret_key import OPENAI_API_KEY
import os
information = """
elon musk is a great guy
"""

# ///////////////////// PROMPT TEMPLATE /////////////////////////
summary_temp =  """  give the information  {information} about a person
 from i want to create 
 1. a short summary
 2. two intreasting facts about them"""

summary_prompt_tempelate = PromptTemplate(input_variables="information", template=summary_temp)
# //////////////////////////////////////////////////////////////////////

llm_edit  =  ChatOpenAI(api_key=OPENAI_API_KEY,temperature=0, model_name="gpt-3.5-turbo")
chain = summary_prompt_tempelate | llm_edit
response = chain.invoke(input={"information":information})

print(response)