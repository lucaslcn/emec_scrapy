import csv
import base64

import scrapy


BASE_URL = 'http://emec.mec.gov.br/emec/consulta-ies/listar-endereco/d96957f455f6405d14c6542552b0f6eb/%s/list/2000'

CSV_FILE = 'codes.csv'

'''
Script created to scrap all data from the following website and all its siblings:
    http://emec.mec.gov.br/emec/consulta-ies/listar-endereco/d96957f455f6405d14c6542552b0f6eb/NTU=/list/2000
    
Assumes there is a file named `codes.csv` with each university ID in it. The ID is used when creating the URL.
It uses Scrapy. To run:
$ scrapy runspider spider.py
The output will be saved into `out.csv`
'''


class QuotesSpider(scrapy.Spider):
    name = "universities"

    def start_requests(self):
        """ Reads `codes.csv` and creates all the URLs """
        with open(CSV_FILE, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for code, _, _ in reader:
                b64 = base64.b64encode(code.encode())
                url = BASE_URL % b64.decode()
                kwargs = {'code': code}
                yield scrapy.Request(
                    url=url,
                    callback=self.parse,
                    cb_kwargs=kwargs
                )

    def parse(self, response, code):
        """ Parses the, very simple, table and appends to `out.csv` """
        xpath = ".//tr[@class='corDetalhe1' or @class='corDetalhe2']"
        table_rows = response.xpath(xpath)

        processed_rows = []
        for row in table_rows:
            cells = row.css('td *::text').getall()
            cells = (c.strip() for c in cells)  # Remove extra spaces
            cells = (c.title() for c in cells)  # Title cases
            cells = (c for c in cells if c != '')  # Filter empty values
            cells = [code] + list(cells)
            processed_rows.append(cells)

        with open('out.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(processed_rows)