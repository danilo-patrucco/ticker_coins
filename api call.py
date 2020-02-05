# This example uses Python 2.7 and the python-request library.
import tkinter
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import GUI

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '2',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '69c171b6-b7db-4e05-83fa-34c5d89d6ca2',
}

session = Session()
session.headers.update(headers)
root = GUI.Tk()
my_gui = GUI.gui(root)
root.mainloop()

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    #ticker = GUI.gui(data)
    #ticker.print_data_test()

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)