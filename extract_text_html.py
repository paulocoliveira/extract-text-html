import urllib
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

search_tags = input("Please enter search tags (separated by comma): ")
urls = input("Please enter url list (separated by comma): ")
urls = urls.split(",")
search_tags = search_tags.split(",")

print("")
print("Starting job...")

file_name = "extract_result.csv" 

with open(file_name, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    titles = ["URL"]
    for tag in search_tags:
        titles.append(tag)
    titles.append("total")
    spamwriter.writerow(titles)

    for url in urls:
        print("Analyzing: {}".format(url))
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="lxml")
        text = soup.get_text()
        total = 0
        line = [url]
        for tag in search_tags:
            quantity = 0
            quantity = text.count(tag)
            line.append(quantity)
            total += quantity
        line.append(total)
        if total != 0:
            spamwriter.writerow(line)

print("")
print("Job finished! Verify generated file. (extract_result.csv)")
