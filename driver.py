from multisearch.search import MultiSearch

'''
All code in this project is my own. I did utilize various stack overflow articles and tutorials to re-familiarize myself with python syntax and threading/beautiful soup examples, but I did not copy/paste any code, I simply used them for reference.
'''
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