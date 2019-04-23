from multisearch.search import MultiSearch

def main():
    while True:
        print("\n")
        query = input("What would you like to multi-search for?")
        multisearch = MultiSearch(query, 10)
        results = multisearch.search()
        print("Results: ")
        for result in results:
            print(result)


if __name__ == '__main__':
    main()