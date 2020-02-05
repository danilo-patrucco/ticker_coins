class gui:
    ''' GUI FOR THE TICKER '''

    def __init__(self, data):
        self.data = data

    def print_data_test(self):
        print(self.data['data'][0]['name'], ' USD ', self.data['data'][0]['quote']['USD']['price'])