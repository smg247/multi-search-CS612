from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests

class Searcher(ABC):

    def __init__(self, query, num_results, base_url):
        self.query = query
        self.num_results = num_results
        self.base_url = base_url

    def set_results(self, results):
        self.results = results

    def get_results(self):
        return self.results

    def get_content(self, request):
        return BeautifulSoup(request.content, 'html.parser')

    @abstractmethod
    def search(self):
        pass


class GoogleSearcher(Searcher):

    def search(self):
        url = self.base_url
        params = {'q':self.query}
        r = requests.get(url=url, params=params)
        content = self.get_content(r)
        print(content.prettify())




class BingSearcher(Searcher):

    def search(self):
        pass