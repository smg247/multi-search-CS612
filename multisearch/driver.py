from multisearch.search import MultiSearch

def run():
    multisearch = MultiSearch('stephen goeddel', 10)
    results = multisearch.search()
    for result in results:
        print(result)


run()