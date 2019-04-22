import threading

from multisearch.searchers import GoogleSearcher, BingSearcher
from multisearch.tabulator import Tabulator

GOOGLE_URL = 'http://google.com/search'
BING_URL = 'http://bing.com/search'


class MultiSearch:

    def __init__(self, query, num_results):
        self.query = query
        self.num_results = num_results
        self.google_results = []
        self.bing_results = []

    def search(self):
        num_results_to_grab = self.num_results * 4

        google_thread = threading.Thread(target=self.search_google, args=(num_results_to_grab,))
        google_thread.start()

        bing_thread = threading.Thread(target=self.search_bing, args=(num_results_to_grab,))
        bing_thread.start()

        google_thread.join()
        bing_thread.join()

        tabulator = Tabulator(self.google_results, self.bing_results, num_results_to_grab)
        final_results = tabulator.tabulate()

        final_results = final_results[0:self.num_results]
        return final_results

    def search_google(self, num_of_results):
        google_searchers = []
        for x in range(int(num_of_results/10)):
            google_searcher = GoogleSearcher(self.query, (x * 10), GOOGLE_URL)
            google_searchers.append(google_searcher)
            google_searcher.start()

        for google_searcher in google_searchers:
            google_searcher.join()
            for result in google_searcher.get_results():
                self.google_results.append(result)

    def search_bing(self, num_of_results):
        bing_searchers = []
        for x in range(int(num_of_results/10) + 1):
            bing_searcher = BingSearcher(self.query, (x * 10), BING_URL)
            bing_searchers.append(bing_searcher)
            bing_searcher.start()

        for bing_searcher in bing_searchers:
            bing_searcher.join()
            for result in bing_searcher.get_results():
                self.bing_results.append(result)
