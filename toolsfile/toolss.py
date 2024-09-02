from langchain_community.tools.tavily_search import TavilySearchResults

# this function we will use in our agent file method 
def get_profile_url_usingTravily(name:str):
    search = TavilySearchResults()  #/// this object will run and give result
    res = search.run(f"{name}")    # /// serch any it will give result as ui me dekha tha na 
    return res[0]["url"]  #/// row one ka url wala answer do 
