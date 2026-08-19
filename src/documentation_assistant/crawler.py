import asyncio
from crawl4ai import AsyncWebCrawler,BM25ContentFilter,CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

md_generator = DefaultMarkdownGenerator(
    content_filter=PruningContentFilter()
)
config = CrawlerRunConfig(
        markdown_generator=md_generator
    )

async def crawl_page(query_url,retrieve_type):
    async with AsyncWebCrawler() as crawler:
        if not retrieve_type:
            results = await crawler.arun(query_url,config=config)
        else:
            tasks = [crawler.arun(url,config=config)for url in query_url]
            results = await asyncio.gather(*tasks)

    return results
