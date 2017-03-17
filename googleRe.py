#!/usr/bin/Python
import requests
import bs4
import re, operator
from sys import argv


def get_n_results(q):
    r = requests.get('http://www.google.com/search',
                     params={'q': q,
                             "tbs": "li:1"})
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, "html5lib")
    s = soup.find('div', {'id': 'resultStats'}).text
    if not s:
        return 0
    m = re.search(r'([0-9,]+)', s)
    return int(m.groups()[0].replace(',', ''))

	
class GoogleResults():
	def __init__(self):
		self.empt = {}


	def compare(self, *argv):
		if len(argv) != 0:
			for param in argv:
				self.empt.update({param : get_n_results(param)})
				# self.empt = sorted(self.empt.items(), key=operator.itemgetter(1))	
		else:
			self.empt.update({'Error' : 'No query passed'})

		return self.empt




