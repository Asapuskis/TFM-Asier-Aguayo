import scrapy

class usernameSpider(scrapy.Spider):
    name = "usernameSpider"
    start_urls = [
        'https://www.discogs.com/forum/thread/736737',
        'https://www.discogs.com/es/forum/thread/707251',
        'https://www.discogs.com/es/forum/thread/732681',
        'https://www.discogs.com/es/forum/thread/172073'
    ]

    def parse(self, response):
        for userPost in response.css('h4.push_right_mini'):
            yield {
                'username': userPost.css('a::text').get()
                #'author': userPost.css('small.author::text').get(),
            }

        next_page = response.css('li a.pagination_next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)