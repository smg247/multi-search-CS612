from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests

from multisearch.results import Result


class Searcher(ABC):

    def __init__(self, query, num_results, base_url):
        self.query = query
        self.num_results = num_results
        self.base_url = base_url
        self.results = []

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
        rank = 0
        start = 0
        while rank < self.num_results:
            params = {
                'q' : self.query,
                'start' : start
            }
            r = requests.get(url=url, params=params)
            content = self.get_content(r)
            potential_results = content.find_all(class_='r')

            for potential_result in potential_results:
                if rank >= self.num_results: # due to 'extra' results we may have to stop before the end of the page
                    break

                link = potential_result.a
                href = self.get_href(link)
                title = link.get_text().strip()

                result = Result(href, title, rank)

                self.results.append(result)
                rank+= 1

            start += 10

    def get_href(self, link):
        href = link['href']
        href = href.replace('/url?q=', '')  # strip out the extra google stuff from the beginning of the link
        index_of_end = href.index('&sa')
        href = href[0:index_of_end] # strip out the extra google stuff from the end of the link
        return href


class BingSearcher(Searcher):

    def search(self):
        pass