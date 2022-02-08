import socket
import requests
import scrapy

HOST, PORT = "", 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))
s.listen(True)

print("Serving HTTP on port %s..."%PORT)

while True:
    client_connection, client_address = s.accept()
    request = client_connection.recv(1024)
    print(request.decode("utf-8"))
    http_response = """\
HTTP/1.1 200 OK

Welcome This is my first webpage. Great!
"""

    client_connection.sendall(bytes(http_response, "utf-8"))
    client_connection.close()

url= 'http://www.wikipedia.org'
r= requests.get(url)

print(r.text)

print("Status code:")
print("\t*", r.status_code)

h=requests.head(url)
print("Header.")
print("**********")

for x in h.headers:
    print("\t",x,".",h.headers[x])

print("**********")

headers = {
    'User-Agent' : 'Iphone 8'
}
url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["http://brickset.com/sets/year-2019"]
    def parse(self, response):
        xpath_selector = '//img'
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