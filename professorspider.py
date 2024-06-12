# # # import scrapy
# # # from professorscraper.items import ProfessorscraperItem

# # # class ProfessorspiderSpider(scrapy.Spider):
# # #     name = "professorspider"
    
# # #     allowed_domains = ["cse.ucsd.edu"]
# # #     start_urls = ["https://cse.ucsd.edu/people/faculty-profiles/faculty"]

# # #     def parse(self, response):

# # #         professors=response.css('strong::text').getall()
# # #         print(professors)
        
# # #         #hrefs=response.css('a[href="/people/faculty-profiles/christine-alvarado"]').getall()
# # #         hrefs=response.css('href')
# # #         print(hrefs)
# # #         for professor_name in professors:
            
# # #             yield {'name':professor_name}
# # #         link_rel=[]
# # #         for professor in professors:
            
# # #             prof=professor.split(" ")
# # #             prof="-".join(prof)
# # #             prof=prof[:-1]
# # #             link=f'https://cse.ucsd.edu/people/faculty-profiles/{prof}'
# # #             link_rel.append(link)
# # #         print(link_rel)
        
# # #         for i,link in enumerate(link_rel):
# # #             next_page=response.css(link)
# # #             if next_page is not None:
# # #                 next_page_url = 'https://books.toscrape.com/' + f'{professor[i]}'
# # #                 yield response.follow(next_page_url, callback=self.parse)




            
            


# # # # import scrapy

# # # # class BookspiderSpider(scrapy.Spider):
# # # #     name = 'bookspider'
# # # #     allowed_domains = ['books.toscrape.com']
# # # #     start_urls = ['https://books.toscrape.com/']

# # # #     def parse(self, response):
# # # #         books = response.css('article.product_pod')
# # # #         for book in books:
# # # #             yield{
# # # #                 'name' : book.css('h3 a::text').get(),
# # # #                 'price' : book.css('div.product_price .price_color::text').get(),
# # # #                 'url' : book.css('h3 a').attrib['href'],
# # # #             }
        

        
# # import re
# # import scrapy
# # from professorscraper.items import ProfessorscraperItem

# # class ProfessorspiderSpider(scrapy.Spider):
# #     name = "professorspider"
    
# #     allowed_domains = ["cse.ucsd.edu"]
# #     start_urls = ["https://cse.ucsd.edu/people/faculty-profiles/faculty"]

# #     def parse(self, response):
# #         professors = response.css('strong::text').getall()
        
# #         for professor in professors:
# #             # Remove non-letter characters from the professor's name
# #             clean_prof_name = re.sub(r'[^a-zA-Z\s]', '', professor.strip())
# #             # Split the professor's name and create the relative URL
# #             prof_slug = '-'.join(clean_prof_name.split()).lower()
# #             prof_url = f"/people/faculty-profiles/{prof_slug}"
            
# #             # Follow the link to the professor's profile page
# #             yield response.follow(prof_url, callback=self.parse_professor)

# #     def parse_professor(self, response):
# #         # Extract the email address from the professor's profile page
# #         email = response.css('.profile .email a::text').get()
        
# #         # Yield the professor's name and email as an item
# #         yield {
# #             'name': response.css('h1::text').get(),
# #             'email': email
# #         }

# import scrapy

# class ProfessorspiderSpider(scrapy.Spider):
#     name = "professorspider"
    
#     allowed_domains = ["cse.ucsd.edu"]
#     start_urls = ["https://cse.ucsd.edu/people/faculty-profiles/faculty"]

#     def parse(self, response):
#         professors = response.css('strong::text').getall()
        
#         for professor in professors:
#             # Follow the link to the professor's profile page
#             yield response.follow(f"/people/faculty-profiles/{professor}", callback=self.parse_professor)

#     def parse_professor(self, response):
#         # Extract the email address using XPath
#         email = response.xpath('/html/body/section/div/div/div[3]/div/article/div/div[2]/a/text()').get()
        
#         # Yield the professor's name and email as an item
#         yield {
#             'name': response.css('h1::text').get(),
#             'email': email
#         }
import scrapy

class ProfessorspiderSpider(scrapy.Spider):
    name = "professorspider"
    
    allowed_domains = ["cse.ucsd.edu"]
    start_urls = ["https://cse.ucsd.edu/people/faculty-profiles/faculty"]

    def parse(self, response):
        professors = response.css('strong::text').getall()
        
        for professor in professors:
            # Follow the link to the professor's profile page
            yield response.follow(f"/people/faculty-profiles/{professor}", callback=self.parse_professor)

    def parse_professor(self, response):
        # Extract the href attribute value using XPath
        href_link = response.xpath('/html/body/section/div/div/div[3]/div/article/div/div[2]/a/').get()
        href_link=href_link.split('>')[1][:-3]
        
        
        # Yield the professor's name and href link as an item
        yield {
            'name': response.css('h1::text').get(),
            'href_link': href_link
        }
