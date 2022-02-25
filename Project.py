import unittest
#import unittest library
import requests
#import requests library

#Set the target webpage
url = 'https://brickset.com/sets/year-2010'
r = requests.get(url)
#This will get the whole page

print(r)

#This will get the staus code
print("Status Code:")
print("\t*", r.status_code, "OK")


#Get just the headers of the webpage
h=requests.head(url)
print("Header. ")
print("**********")
#To print line by line

for x in h.headers:
    print("\t",x,".",h.headers[x])

print("**********")

class Testcase(unittest.TestCase):
    def testExample (self):
        print("testing")

#Modifying the headers user-agents
headers = {
    'User-Agent' : 'Mobile'
}
url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)

import scrapy
#import scrapy library

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = [url]

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
#To recurse next page
        Page_selector = '.next a ; :attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
if __name__ == '__main__':
    unittest.main()