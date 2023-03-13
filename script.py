

import requests
from bs4 import BeautifulSoup
import pickle
from send_email import push_email


URL = "https://www.ozbargain.com.au/product/bose-noise-cancelling-headphones-700"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
curr_id = soup.find('h2', {"class": "title"})["id"]
    
with open("recents.csv", "rb") as r:
    try:
        id_recent_dict = pickle.load(r)
        id_set = id_recent_dict['id']
        recent_id = id_recent_dict['mrecent']
        if curr_id != recent_id and curr_id not in id_set:
                id_set.add(curr_id)
                id_recent_dict['mrecent'] = curr_id
                with open("recents.csv", "wb") as w:
                    pickle.dump(id_recent_dict, w, pickle.HIGHEST_PROTOCOL)
                push_email()
        else:
            pass
    except:
        id_recent_dict = {'id': set(), 'mrecent':None}
        with open("recents.csv", "wb") as w:
            pickle.dump(id_recent_dict, w, protocol= pickle.HIGHEST_PROTOCOL)