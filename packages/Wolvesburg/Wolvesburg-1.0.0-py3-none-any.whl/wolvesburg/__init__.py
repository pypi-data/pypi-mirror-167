import pickle


def get(filename: str):
    f = open(filename, 'rb')
    data = pickle.load(f)
    f.close()
    return data


class Wolvesburg:
    def __init__(self, name, date):
        self.name = name
        self.date = date


def deposit(filename: str, data: Wolvesburg):
    f = open(filename, 'wb')
    pickle.dump(data, f)
    f.close()

