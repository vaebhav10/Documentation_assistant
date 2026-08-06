import asyncio
from crawl4ai import AsyncWebCrawler


async def crawl_page(query_url,retrieve_type):
    async with AsyncWebCrawler() as crawler:
        if not retrieve_type:
            results = await crawler.arun(query_url)
        else:
            tasks = [
                crawler.arun(url)
                for url in query_url
            ]
            results = await asyncio.gather(*tasks)

    return results
