# ///////////////////////////////////////////////////////////////////////
import os
import requests  #---> for making http request to an api to get linkdin info 
from dotenv import load_dotenv
load_dotenv()
# /////////////////////////////////////////////////////////////////////////


# /////////////////////FUNCTION///////////////////////////////////////////////////
def scrape_linkdin_profile(linkedin_url:str , mock: bool=True):

    if mock:
            linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
            response = requests.get(
                linkedin_profile_url,
                timeout=10,
        )
    else: # --> use proxy curl to make http api request 
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXY_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url":linkedin_url},
            headers=header_dic,
            timeout=10,
        )
    data = response.json()
    # //////////////// Data cleaning Code /////////////////////
    data = {
        k: v
        for k ,v in data.items()
        if v not in ([],"","", None) 
        and k not in ["people_also_viewed", "certifications"]  
        }
    if data.get("groups"):
        for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")
    # ///////////////////////////////////////////////////////////////
    return data
# /////////////////////////////////////////////////////////////////////////////////////////


if __name__ == "__main__":
     print(
          scrape_linkdin_profile(
               linkedin_url= "https://www.linkedin.com/in/harshverma0/"
          )
     )
    