from usp.tree import sitemap_tree_for_homepage

def get_sitemap(url):
    page_links = []

    """ Its raining outside dawg! and the music is high  """
    
    try:
        tree = sitemap_tree_for_homepage(url)
        page_links = [page.url for page in tree.all_pages()]
    except :
        return []
    return page_links