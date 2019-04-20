import threading

from multisearch.searchers import GoogleSearcher

def run():
    results = search_google(100)

    for result in results:
        for r in result:
            print(r)


def search_google(num_of_results):
    google_searchers = []
    results = []
    for x in range(int(num_of_results/10)):
        google_searcher = GoogleSearcher('something really cool', (x * 10), 'http://google.com/search')
        google_searchers.append(google_searcher)
        google_searcher.start()

    for google_searcher in google_searchers:
        google_searcher.join()
        results.append(google_searcher.get_results())
    return results


run()