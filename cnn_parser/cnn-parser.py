import requests
from selectolax.parser import HTMLParser

def get_html(url):
    response = requests.get(url)
    html = response.text
    return html

def parse_cnn_articles(html_content):
    tree = HTMLParser(html_content)
    articles = []
    
    # Define the specific class for the container that holds the article information
    container_class = 'container_vertical-strip__item--type-section'

    # Find all containers with the specified class
    containers = tree.css(f'div.{container_class}')

    for container in containers:
        article = {}

        # Extract article title
        article_title = container.css('span.container__headline-text')[0].text()
        article['article_title'] = article_title

        # Extract article URL
        article_url = container.css('a.container__link--type-article')[0].attributes['href']
        article['article_url'] = article_url

        articles.append(article)

    return articles

def main():
    url = 'https://edition.cnn.com/business/tech'
    html_content = get_html(url)
    
    if html_content:
        articles = parse_cnn_articles(html_content)
        
        if articles:
            for index, article in enumerate(articles, start=1):
                print(f"Index: {index}")
                print(f"Title: {article['article_title']}")
                print(f"URL: {article['article_url']}")
                print()
        else:
            print("No articles found on the page.")
    else:
        print("Failed to fetch the HTML content from the URL.")

if __name__ == '__main__':
    main()