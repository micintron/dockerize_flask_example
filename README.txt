This code builds an API using flask nginx and Guinicon to pull and clean viable text from a web page.

Current endpoints 2

'/' 
home checks the API is running 

'scrape_site' 
Takes in url and pulls in text from site then returns extracted data in json format


Use 
docker-compose build
docker-compose up

Commands in terminal of central folder to build the container


Risks / Blockers
Dose not yet handle SSL certificate error's those break the call
Dose not yet bypass sites that block scraping calls to content
