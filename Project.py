import unittest

import requests
import scrapy


url= 'https://brickset.com/sets/year-2010'
r= requests.get(url)
print("status code")
print("\t *", r.status_code, "OK")

h=requests.head(url)
print(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t",x,".",h.headers[x])
print("**********")


class Testcase(unittest.TestCase):
    def testExample(self):
        print("testing")

headers = {
    'User-Agent' : 'Mobile'
}

url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["http://brickset.com/sets/year-2010"]
    def parse(self, response):
        xpath_selector='//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link':x.xpath(newsel).extract_first(),
            }

        Page_selector = '.next a ; :attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

if __name__ == '__main__':
    unittest.main()