import datetime, requests

def get_params():
    today = datetime.datetime.today()
    one_day =  datetime.timedelta(days=1)
    yesterday = today - one_day
    fromdate = int(yesterday.timestamp())
    todate = int(today.timestamp())
    tagg = 'Python'
    params = f'?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&tagged={tagg}&site=stackoverflow'
    return params

def get_questions():
    host = 'https://api.stackexchange.com/'
    uri = '2.3/questions'
    params = get_params()
    url = host + uri
    response = requests.get(url, params=params)
    print(response.json())

if __name__ == '__main__':
    get_questions()