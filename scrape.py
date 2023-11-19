import requests
from bs4 import BeautifulSoup

# Base URL for relative links
base_url = "https://www.moldpres.md"

def get_news_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the news blocks or links. This will depend on the specific structure of the website.
    # Here's a hypothetical example:
    news_blocks = soup.find_all('p', class_='news-category-link news__with_image')  # class name is just an example
    links = [base_url + block.find('a')['href'] for block in news_blocks if block.find('a')]
    return links

def parse_individual_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the necessary information from the individual news page
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else 'No title'

    archive_item_attrib = soup.find('p', class_="archive-item-atrib")
    date_span = archive_item_attrib.find('span') if archive_item_attrib else None
    date = date_span.get_text(strip=True) if date_span else 'No date'


    # Find the div with class 'normal-text' and extract all paragraphs' text
    info_div = soup.find('div', class_="normal-text")
    paragraphs_text = [p.get_text(strip=True) for p in info_div.find_all('p')] if info_div else ['No information']

    # Find images within the 'info_div'
    images_src = []
    if info_div:
        # Note the class name change to 'news--images' based on your HTML structure
        image_div = info_div.find('div', class_="news--images")
        if image_div:
            images = image_div.find_all('img')
            for img in images:
                if img.has_attr('src'):
                    # Join the base URL with the img src attribute
                    images_src.append(requests.compat.urljoin(url, img['src']))

    return {
        'title': title,
        'date': date,
        'info': paragraphs_text,
        'images': images_src
    }
# Main function to get news
def main():
    print("hre")
    politics_news_url = "https://www.moldpres.md/news/politics"
    links = get_news_links(politics_news_url)

    print("got news")
    data_news = []
    for link in links[:6]:  # Limit to the first 10 news articles
        print("link")
        news_data = parse_individual_news(link)
        data_news.append(news_data)
    return data_news


if __name__ == "__main__":
    main()