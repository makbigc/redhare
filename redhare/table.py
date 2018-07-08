import requests
from bs4 import BeautifulSoup

from util import transform_data


class ResultTable:
    prefix = ("http://racing.hkjc.com/racing/Info"
              "/meeting/Results/english/Local/")

    def __init__(self, date, venue, race_no):
        self.date = date
        self.venue = venue
        self.race_no = race_no
        self.url = ResultTable.prefix + date + "/" + venue + "/" + race_no

        self.get_html()
        self.get_soup()

    def get_html(self):
        self.html = requests.get(self.url).text
        return self.html

    def get_soup(self):
        self.soup = BeautifulSoup(self.html, 'html.parser')
        return self.soup

    def is_valid_link(self):
        script = self.soup.find('script', attrs={'language': 'javascript',
                                                 'type': 'text/javascript'})
        var_list = script.contents[0].split('var ')

        # PageIsReady is the second to last variable in var_list
        # [0] is the variable name; [1] is its boolean value
        # e.g. PageIsReady = true;\r\n
        PageIsReady = var_list[-2].split(' = ')[1]
        return True if 'true' in PageIsReady else False

    def get_no_of_race(self):
        '''Return the number of races held on the same day'''

        div = self.soup.find('div', attrs={"class": "raceNum clearfix"})

        import re
        pattern = re.compile("/Local/" + self.date + "/" + self.venue)

        match = div.find_all('a', attrs={'href': pattern})
        return len(match)+1

    def get_result_list(self):

        def tr_with_class(tag):
            return tag.name == 'tr' and tag.has_attr('class')

        table_attrs = {"cellpadding": "1", "cellspacing": "1",
                       "class":
                       "tableBorder trBgBlue tdAlignC number12 draggable",
                       "width": "760px"}

        table = self.soup.find("table", attrs=table_attrs)
        data = table.tbody.find_all(tr_with_class)
        records = [record.contents for record in data]
        records = map(transform_data, records)
        records = [record for record in records]
        self.records = records
        return records

    def print_result(self):

        if not hasattr(self, 'records'):
            self.get_result_list()

        output_string = ('{:4} {:4} {:28} {:4} {:20} {:20} '
                         '{:3} {:4} {:3} {:12} {:12} {:12} {:4}')
        for record in self.records:
            print(output_string.format(*record))
