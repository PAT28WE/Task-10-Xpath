Absolute XPATH Guvi following list-/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a 
                                   /html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a/text()
                                   /html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button/div 


Relative XPATH Guvi following list -//*[@id="mount_0_0_JN"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a/text()
                                    //*[@id="mount_0_0_JN"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button/div


Absolute XPATH Guvi follower list-/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/text()
                                 -/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]

Relative XPATH Guvi follower list-//*[@id="mount_0_0_JN"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/text()
                                 -//*[@id="mount_0_0_JN"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div

extract the total number of followers and following from the URL mentioned above program:

# importing libraries
from bs4 import BeautifulSoup
import requests
 
# instagram URL
URL = "https://www.instagram.com/{}/"
 
# parse function
def parse_data(s):
     
    # creating a dictionary
    data = {}
     
    # splitting the content 
    # then taking the first part
    s = s.split("-")[0]
     
    # again splitting the content 
    s = s.split(" ")
     
    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
     
    # returning the dictionary
    return data
 
# scrape function
def scrape_data(username):
     
    # getting the request from url
    r = requests.get(URL.format(username))
     
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
     
    # finding meta info
    meta = s.find("meta", property ="og:description")
     
    # calling parse method
    return parse_data(meta.attrs['content'])
 
# main function
if __name__=="__main__":
     
    # user name
    username = "geeks_for_geeks"
     
    # calling scrape function
    data = scrape_data(username)
     
    # printing the info
    print(data)
OUTPUT:{'Followers': '362K', 'Following': '3'}