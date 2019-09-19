import requests
import lxml.html
import sys
from database_tools import insert_post, connect_to_database

url_origin = "https://minecraft-inside.ru"
url_parse = "https://minecraft-inside.ru/mods/page/1/"

if len(sys.argv) == 1:
    print("Enter your password: <script_name> <password>")
    exit(1)
else:
    connect_to_database(sys.argv[1])

def request(url):
    return requests.get(url).content


def parse_page(url):
    

    doc = lxml.html.fromstring(request(url))
    posts = doc.xpath('.//div[@class="box box_grass post"]')

    for post in posts:
        data_array = []
        
        href = post.xpath('.//h2[@class="box__title"]/a/@href')
        content = request(f"{url_origin}{href[0]}")

        post_doc = lxml.html.fromstring(content)

        title = post_doc.xpath('//div[@class="box__heading"]/h1[@class="box__title"]/text()')
        description = post.xpath('.//div[@class="box__body"]/div/text()')
        download_link = post_doc.xpath('//td[@class="dl__info"]/a/@href')
        
        data_array.append(title[0])
        data_array.append(description[0])
        data_array.append(download_link[0])
    
        insert_post(data_array)

    


parse_page(url_parse)


