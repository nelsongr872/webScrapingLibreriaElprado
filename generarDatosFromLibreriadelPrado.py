import urllib.request, unicodedata, csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

product_name = []
product_editorial = []
product_description = []
product_price = []
for i in range(1,153):#1001
#class author, editorial, product-desc, price product-price
#url: https://www.libreriadelprado.com/100-libros-antiguos?p=262
	url = 'https://www.libreriadelprado.com/100-libros-antiguos?p='+str(i)
	req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req).read()
	print(url + '\n')
	soup = BeautifulSoup(page)

	linksoup_array_product_name = soup.find_all('a',{'class':['product-name']})
	linksoup_array_product_description =soup.find_all('p',{'class':['product-desc']})
	linksoup_array_product_price =soup.find_all('span',{'class':['price product-price']})
	



	def annadirDatosaArrayDeDatosRepetidos(arrayLinkSoupProduct_, arrayProduct_):
		#bandera
		flag1 = True
		for x in arrayLinkSoupProduct_:
			x = x.string.strip()
			normalizado=unicodedata.normalize('NFKD',x).encode('ascii','ignore')
			if len(normalizado)>1:
				if flag1:
					flag1 = not flag1
				else:
					flag1 = not flag1
					arrayProduct_.append(normalizado)

	def annadirDatosaArray(arrayLinkSoupProduct_, arrayProduct_):
		for x in arrayLinkSoupProduct_:
			x = x.string.strip()
			normalizado=unicodedata.normalize('NFKD',x).encode('ascii','ignore')
			arrayProduct_.append(normalizado)

	annadirDatosaArrayDeDatosRepetidos(linksoup_array_product_name, product_name)
	annadirDatosaArray(linksoup_array_product_description, product_description)
	annadirDatosaArray(linksoup_array_product_price, product_price)
	
	print(len(product_name))
	print(len(product_description))
	if len(product_name) != len(product_price):
		print(len(product_name) - len(product_price))
	else:
		print(len(product_price))

def borrarDatosDeLibrosQuefaltan(arrayProduct_):
	for x in range(0, len(arrayProduct_)):
		if x == 204 or x == 894 or x == 907 or x == 1012 or x == 1034 or x == 1039 or x == 1053 or x == 1069 or x == 1079 or x == 1088 or x == 1222 or x == 1226 or x == 1228 or x == 1274 or x == 1307 or x == 1342 or x == 1520 or x == 1793 or x == 1849 or x == 1940 or x == 2344 or x == 2345 or x == 2346 or x == 2347 or x == 2348 or x == 2548 or x == 2577 or x == 2645 or x == 2990:
			arrayProduct_.pop(x)
	
def volcardatosEnCSV(product_name,product_description,product_price):
	for x in range(0, len(product_name)):
		with open('librosDeLibreriaELprado.csv', 'a') as csv_file:
						writer = csv.writer(csv_file)
						writer.writerow([product_name[x], product_description[x], product_price[x]])


borrarDatosDeLibrosQuefaltan(product_name)
borrarDatosDeLibrosQuefaltan(product_description)
volcardatosEnCSV(product_name,product_description,product_price)
print('fin del programa')
		


#def volcarDatosEnCsv(product_name,product_author,product_editorial,product_description,product_price)







