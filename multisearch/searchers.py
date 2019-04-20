from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
import threading

from multisearch.results import Result


class Searcher(ABC, threading.Thread):

    def __init__(self, query, start_index, base_url):
        super().__init__()
        self.query = query
        self.start_index = start_index
        self.base_url = base_url
        self.results = []

    def get_results(self):
        return self.results

    def get_content(self, request):
        return BeautifulSoup(request.content, 'html.parser')

    @abstractmethod
    def run(self):
        pass


class GoogleSearcher(Searcher):

    def run(self):
        url = self.base_url
        rank = self.start_index
        params = {
            'q' : self.query,
            'start' : self.start_index
        }
        r = requests.get(url=url, params=params)
        content = self.get_content(r)
        potential_results = content.find_all(class_='r')

        for potential_result in potential_results:
            link = potential_result.a
            href = self.get_href(link)
            title = link.get_text().strip()

            result = Result(href, title, rank)

            self.results.append(result)
            rank+= 1

    def get_href(self, link):
        href = link['href']
        href = href.replace('/url?q=', '')  # strip out the extra google stuff from the beginning of the link
        index_of_end = href.index('&sa')
        href = href[0:index_of_end] # strip out the extra google stuff from the end of the link
        return href


class BingSearcher(Searcher):

    def run(self):
        pass