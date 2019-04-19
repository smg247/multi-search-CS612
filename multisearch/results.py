import urllib


class Result:

    def __init__(self, link, title, rank):
        self.link = link
        self.title = title
        self.rank = rank

    def get_clickable_link(self):
        return urllib.parse.unquote(self.link)

    def __str__(self):
        return 'TITLE: ' + self.title + ' LINK: ' + self.get_clickable_link() + ' RANK: ' + str(self.rank)