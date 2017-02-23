import scrapy


# new instance of class scrapy.Spider
class GOTwiki2Spider(scrapy.Spider):
    name = "GOTwiki2"
    main = 'http://awoiaf.westeros.org/index.php/A_Game_of_Thrones-Prologue'
    start_urls = [main]

    def parse(self, response):
        pov = response.xpath('//table[@class="infobox"]/tr[4]/td/a/text()').extract_first()
        setting = response.xpath('//table[@class="infobox"]/tr[5]/td/a/text()').extract_first()
        book = response.xpath('//table[@class="infobox"]/tr[2]/th/i/a/text()').extract_first()
        chronology = response.xpath('//table[@class="infobox"]/tr[8]/th/table/tr[1]/td[2]/strong/text()').extract_first()
        if not chronology:
            chronology = response.xpath('//table[@class="infobox"]/tr[8]/th/table/tr[2]/td[2]/strong/text()').extract_first()
        if not chronology:
            chronology = response.xpath('//table[@class="infobox"]/tr[8]/th/table/tr/td[2]/text()').extract_first()

        yield {'pov': pov,
               'setting': setting,
               'chronology': chronology,
               'book': book}

        url_base = 'http://awoiaf.westeros.org'
        try:
            url_path = response.xpath('//table[@class="infobox"]/tr[8]/th/table/tr/td[3]/a/@href').extract()[0]
        except:
            url_path = response.xpath('//table[@class="infobox"]/tr[6]/th/table/tr/td[3]/a/@href').extract()[0]
        next_url = url_base + url_path
        next_url=response.urljoin(next_url)

        yield scrapy.Request(next_url, callback=self.parse)
