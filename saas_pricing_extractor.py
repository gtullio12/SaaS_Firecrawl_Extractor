from firecrawl import Firecrawl
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("FIRECRAWL_API_KEY")

firecrawl = Firecrawl(api_key=api_key)

print(firecrawl.scrape('firecrawl.dev'))