import requests
domain = "https://api.vk.com/method"
access_token = 'vktoken' # vktoken - VK API token

def get_friends(user_id, fields):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    key = 'bdate'
    query_params = {
        'domain' : domain,
        'access_token': access_token,
        'user_id': user_id,
        'fields': fields,
    }

    query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
    response = requests.get(query)
    return _sort_all_dates(response.json()['response']['count'], response.json()['response']['items'], key)

def _sort_all_dates (count, items, key):
    i = 0
    n_count = 0
    values = []
    while i < count:
        if key in items[i]:
            values.append(items[i][key])
            n_count += 1
        i += 1
    return _sort_dates_with_year(values,n_count,key)

def _sort_dates_with_year(values, count = None, key = None):
    if key == None:
        return values
    i = 0
    y_count=0
    values_with_yaer = []
    if count != None:
        while i < count:
            if len(values[i]) > 5:
                values_with_yaer.append(values[i])
                y_count+=1
            i+=1
    return _math_func(values_with_yaer,y_count)

def _math_func(bdates, count = None):
    if count == None:
        return bdates
    i=0
    buf=0
    int_values = []
    while i < count:
        j=-1
        z=0
        while j > -5 :
            buf += int((bdates[i])[j])*(10**z)
            j-=1
            z+=1
        i+=1
    return 2017 - (buf//i) - 1
    
if __name__ == '__main__':
    print(get_friends(85724972,'bdate'))