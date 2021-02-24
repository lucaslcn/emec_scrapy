ENGLISH

Script created to scrap all data from the following website and all its siblings:
    http://emec.mec.gov.br/emec/consulta-ies/listar-endereco/d96957f455f6405d14c6542552b0f6eb/NTU=/list/2000
    
Assumes there is a file named 'codes.csv' with each university ID in it. The ID is used when creating the URL.
It uses Scrapy. To run:
	scrapy runspider spider.py
The output will be saved into 'out.csv'

PORTUGUESE

Script criado para realizar scraping de todos dados do seguinte website e todos os seus relativos:
	http://emec.mec.gov.br/emec/consulta-ies/listar-endereco/d96957f455f6405d14c6542552b0f6eb/NTU=/list/2000
Requer um arquivo chamado 'codes.csv' com o ID de cada universidade no mesmo. O ID é utilizado com conversão em base 64 para criar a URL.
Utiliza a biblioteca Scrapy. Para rodar:
	scrapy runspider spider.py
O output será salvo em 'out.csv' na mesma pasta.
