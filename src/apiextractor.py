import requests


class APIExtractor:

    def __init__(self, state, city):
        self.state = state.lower()
        self.city = city.lower

        self.url = "http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?estado=" + self.state

    def return_url(self):
        return self.url

    def return_json(self):
        r = requests.get(self.url)
        return r.json()
