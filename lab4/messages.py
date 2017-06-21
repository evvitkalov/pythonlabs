import requests
import plotly
from pprint import pprint as pp
from datetime import datetime
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime
from datetime import date
domain = "https://api.vk.com/method"
access_token = 'vk' # vk - VK API token


def messages_get_history(user_id, peer_id, offset=0, count=20):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(peer_id, int), "peer_id must be positive integer"
    assert peer_id > 0, "peer_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "offset must be positive integer"
    assert count >= 0, "count must be positive integer"
    query_params = {
        'domain' : domain,
        'access_token': access_token,
        'offset': offset,
        'count': count,
        'user_id': user_id,
        'peer_id': peer_id,
    }

    query = "{domain}/messages.getHistory?offset={offset}&count={count}&user_id={user_id}&peer_id={peer_id}&access_token={access_token}&v=5.64".format(**query_params)
    response = requests.get(query)
    return response
    

def count_dates_from_messages(messages_date, count=0):
    i = 1
    counter = []
    counter.append((messages_date[i]))
    counter_nums = []
    counter_nums.append(1)
    counter_elements = 0
    buf = (messages_date[i])
    while i < count:
        messages_date[i] = (messages_date[i])
        if messages_date[i] == buf:
            counter_nums[counter_elements]+=1
        else:
            buf = messages_date[i]
            counter.append(buf)
            counter_elements+=1
            counter_nums.append(1)
        i+=1
    return counter,counter_nums

def _dates(dates_values,count=0):
    i=0
    buf = 0
    print (dates_values)
    print (count)
    new_dates=[]
    while i < count:
        new_dates.append(datetime.strftime(date.fromtimestamp(dates_values[i]),"%Y.%m.%d"))
        i+=1
    return new_dates

if __name__ == "__main__":
    n=200
    offset = 0
    history = messages_get_history (164755486,166896795,offset,n)
    i = 0
    count = n-1
    dates_from_messages = [] 
    while count > i:
         dates_from_messages.append(history.json()['response']['items'][count]['date'])
         count-=1
		 # plotly_username - your plot.ly username, api_key - plot.ly API key
    plotly.tools.set_credentials_file(username='plotly_username', api_key='api_key')
    new_messages = _dates(dates_from_messages,n-1)
    count,num_count = count_dates_from_messages(new_messages,n-1)
    print (new_messages)
    data = [go.Scatter(x=count,y=num_count)]
    py.plot(data)





    
