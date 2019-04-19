from multisearch.searchers import GoogleSearcher

def run():
    google_searcher = GoogleSearcher('reddit', 10, 'http://google.com/search')
    google_searcher.search()

run()