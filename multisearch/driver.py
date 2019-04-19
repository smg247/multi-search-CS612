from multisearch.searchers import GoogleSearcher

def run():
    google_searcher = GoogleSearcher('reddit', 30, 'http://google.com/search')
    google_searcher.search()

    for result in google_searcher.get_results():
        print(result)

run()