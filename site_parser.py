import requests
import lxml.html
from database_tools import insert_post

url_origin = "https://minecraft-inside.ru"


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

    


