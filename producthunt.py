from bs4 import BeautifulSoup
import requests

## methods in class return a dict with products, descriptions, upvotes, and links of todays new products on ProductHunt.
## requires BeautifulSoup, install via commandline with pip install bs4

class ProductHunt():

	def parse_html(self,url):
		html_doc = requests.get(url)	
		return BeautifulSoup(html_doc.text)

	def products(self,today):
		print("parsing html...")
	 	b = self.parse_html("http://www.producthunt.com/")
	 	print("done.")
		t = [x.find_all('a',class_="post-url title") for x in b.find_all('div',class_="day")][0]
	 	h = [x.find_all('a',class_="post-url title",href=True) for x in b.find_all('div',class_="day")][0]
	 	s = [x.find_all('span',class_="post-tagline description") for x in b.find_all('div',class_="day")][0]
	 	v = [x.find_all('span',class_="vote-count") for x in b.find_all('div',class_="day")][0]
	 	products = [("product",x.get_text()) for x in t]
	 	descriptions = [("description",x.get_text()) for x in s]
	 	upvotes = [("upvote",int(x.get_text())) for x in v]
	 	links = [("link","http://www.producthunt.com"+x['href']) for x in h]
	 	result = [dict([w] + [x] + [y] + [z]) for (w,x,y,z) in zip(products, descriptions,upvotes,links)]
		return result
