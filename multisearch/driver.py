import threading

from multisearch.searchers import GoogleSearcher, BingSearcher
from multisearch.tabulator import Tabulator

GOOGLE_URL = 'http://google.com/search'
BING_URL = 'http://bing.com/search'

def run():
    google_results = search_google(10)
    bing_results = search_bing(10)

    tabulator = Tabulator(google_results, bing_results, 10)
    final_results = tabulator.tabulate()
    for final_result in final_results:
        print(final_result)


def search_google(num_of_results):
    google_searchers = []
    results = []
    for x in range(int(num_of_results/10)):
        google_searcher = GoogleSearcher('something really cool', (x * 10), GOOGLE_URL)
        google_searchers.append(google_searcher)
        google_searcher.start()

    for google_searcher in google_searchers:
        google_searcher.join()
        for result in google_searcher.get_results():
            results.append(result)

    return results


def search_bing(num_of_results):
    bing_searchers = []
    results = []
    for x in range(int(num_of_results/10) + 1):
        bing_searcher = BingSearcher('something really cool', (x * 10), BING_URL)
        bing_searchers.append(bing_searcher)
        bing_searcher.start()

    for bing_searcher in bing_searchers:
        bing_searcher.join()
        for result in bing_searcher.get_results():
            results.append(result)

    return results


run()