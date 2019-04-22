class Tabulator:

    def __init__(self, google_results, bing_results, max_result_num):
        self.google_results = google_results
        self.bing_results = bing_results
        self.max_result_num = max_result_num

    def tabulate(self):
        final_results = []
        for google_result in self.google_results:
            matching_bing_result = self.find_matching_result(google_result, self.bing_results)
            if matching_bing_result is not None:
                google_result.rank = google_result.rank + matching_bing_result.rank
                self.bing_results.remove(matching_bing_result)
            else:
                google_result.rank = google_result.rank + self.max_result_num

            self.google_results.remove(google_result)
            final_results.append(google_result)

        for bing_result in self.bing_results:
            bing_result.rank = bing_result.rank + self.max_result_num
            final_results.append(bing_result)

        self.sort_results(final_results)
        return final_results

    def find_matching_result(self, result, results_to_search):
        for result_to_search in results_to_search:
            if result_to_search.get_clickable_link() == result.get_clickable_link():
                return result_to_search

        return None

    def sort_results(self, results):
        results.sort(key=lambda result:result.rank)
