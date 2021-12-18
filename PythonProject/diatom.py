from bs4 import *
import requests
import os

# Klasör Oluşturma
def folder_create(images):
	try:
		folder_name = input("Klasör Adını Giriniz:- ")		
		os.mkdir(folder_name)

	# Aynı isimli klasör varsa farklı bir isim iste
	except:
		print("Bu İsimde Bir Klasör Bulunmaktadır!")
		folder_create()

	# Resim indirme
	download_images(images, folder_name)


# Tüm görüntüler bu urlden indirilir
def download_images(images, folder_name):

	
	count = 0

	# Url de bulunan tüm resimleri yazdırır.
	print(f"Toplam {len(images)} Resim Bulundu!")


	if len(images) != 0:
		for i, image in enumerate(images):
			
			try:
				
				image_link = image["data-srcset"]
				
			except:
				try:
					
					image_link = image["data-src"]
				except:
					try:
						
						image_link = image["data-fallback-src"]
					except:
						try:
							
							image_link = image["src"]

						except:
							pass

			# Görsel içeriği alınmaktadır.
			try:
				r = requests.get(image_link).content
				try:
					
					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					# Resim indirme işlemi başlatılır.
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)

					# İndirilen görüntünün sayısını almaktadır.
					count += 1
			except:
				pass

		# Tüm resimler indirilebiliyorsa
		if count == len(images):
			print("Tüm Resimler İndirildi!")
			
		# Tüm resimler indirilemiyorsa
		else:
			print(f"Toplam {len(images)} Resimden {count} İndirildi ")


def main(url):

	
	r = requests.get(url)
 
	soup = BeautifulSoup(r.text, 'html.parser')

	images = soup.findAll('img')

	folder_create(images)


url = input("URL Giriniz:- ")

main(url)
