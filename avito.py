import requests
from bs4 import BeautifulSoup
import csv
import lxml



def get_html(url):
	r = requests.get(url)
	return r.text

def get_total_pages(html):
	soup = BeautifulSoup(html, 'lxml')

	pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
	total_pages = pages.split('=')[1].split('&')[0]

	return int(total_pages)

def write_csv(data):
	with open('avito.csv', 'a') as f:
		writer = csv.writer(f)

		writer.writerow( (data['title'],
						  data['price'],
						  data['metro'],
						  data['url']) )

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')

	for ad in ads:
		# title, price, metro, url
		name = ad.find('div', class_='description').find('h3').text.strip().lower()

		if 'htc' in name:
			try:
				title = ad.find('div', class_='description').find('h3').text.strip()
			except:
				title = ''

			try:
				price = ad.find('div', class_='about').text.strip()
			except:
				price = ''

			try:
				metro = ad.find('div', class_='data').find_all('p')[-1].text.strip()
			except:
				metro = ''

			try:
				url = 'https://www.avito.ru' + ad.find('div', class_='description').find('a').get('href')
			except:
				url = ''

			data = {'title': title,
					'price': price,
					'metro': metro,
					'url': url}

			write_csv(data)
		else:
			continue


def main():
	url = 'https://www.avito.ru/moskva/telefony?p=1&q=htc'

	base_url = 'https://www.avito.ru/moskva/telefony?'
	page_part = 'p='
	query_part = '&q=htc'

	total_pages = get_total_pages(get_html(url))

	# for i in range(1, total_pages+1):
	for i in range(1,3):
		url_gen = base_url + page_part + str(i) + query_part
		# print (url_gen)
		html = get_html(url_gen)
		get_page_data(html)


if __name__ == '__main__':
	main()
	print ('Finish')
