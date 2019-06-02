from clients import rates

def load():
    rate = rates.estimate('', '', '', '', '', '', [])
    print(rate)

load()
