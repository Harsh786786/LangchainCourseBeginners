import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,  #---> create agent for use using tool llm and promptemplate
    AgentExecutor,   #----> run ntime of agent 
)
from langchain import hub #--> way to download premade prompts
#------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#//////////////////// Tool code because can not abel to import tool file /////////////////////////////
from langchain_community.tools.tavily_search import TavilySearchResults
# this function we will use in our agent file method 
def get_profile_url_usingTravily(name:str):
    search = TavilySearchResults()  #/// this object will run and give result
    res = search.run(f"{name}")    # /// serch any it will give result as ui me dekha tha na 
    return res[0]["url"]  #/// row one ka url wala answer do 
#//////------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# /////////////This methdo takes string and return string //////////////////////////////////////////////
def lookup(name: str) -> str:  
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo",
    )
#//////////////////////////////////////// Prompt template /////////////////////
    template = """ given the full name {name_of_person} i want you to get me a link to their linkdin profile page.
    Your answer should only contain only URL"""

    promp_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

#////////////////////////////////////// Tool For AGENT ///////////////////////////////
    tools_for_agent = [
        #//// When agent need it will run this tool based on requirment see description also
        Tool(
            name = "Crawl Google 4 linkedin profile page",
            func= get_profile_url_usingTravily,
            description = " Use for when we need  get the linkedin page url" #--> used by llm 
        )
    ]

#/////////////////////////////// ///////////////////////////////////////////////////   
    react_prompt = hub.pull("hwchase17/react")


# //////////////////////// Create agent /////////////////////////////////////////////////////
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    #//// RUNTIME FOR AGENT ////////////////
    agent_executor = AgentExecutor(agent=agent , tools=tools_for_agent , verbose=True)

#////////////// INVOKE AGENT ///////////////////////////////
    result = agent_executor.invoke(
        input = {"input": promp_template.format_prompt(name_of_person=name)}

    )    
#/////////////////////////////////////////////////////////////////////////////
    linkedin_profil_url = result["output"]
    return linkedin_profil_url
#////////////////////////////////////////////----------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if __name__ == "__main__":
    linkedin_url = lookup(name="Harsh Verma virtusa")
    print(linkedin_url)