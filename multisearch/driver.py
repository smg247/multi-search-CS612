from multisearch.search import MultiSearch

def run():
    while True:
        print("\n")
        query = input("What would you like to multi-search for?")
        multisearch = MultiSearch(query, 10)
        results = multisearch.search()
        print("Results: ")
        for result in results:
            print(result)


run()