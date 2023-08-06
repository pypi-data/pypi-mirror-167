import pickle


def get(filename: str):
    filename += '.wolvesburg'
    f = open(filename, 'rb')
    data = pickle.load(f)
    f.close()
    return data


class Wolvesburg:
    def __init__(self):
        pass


def deposit(filename: str, data: Wolvesburg):
    filename += '.wolvesburg'
    f = open(filename, 'wb')
    pickle.dump(data, f)
    f.close()

