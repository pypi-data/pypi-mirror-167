from requests_html import HTMLSession
from pprint import pprint


def olx_min_finder(phrase, min_price=5000, pagination=1):
    session = HTMLSession()
    phrase = phrase.replace(" ", "-")

    url = f"https://www.olx.ua/d/uk/list/q-{phrase}/"
    urls = [url]
    if pagination > 1:
        urls += [url+f"?page={i}" for i in range(2, pagination+1)]

    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    min_price_product = None

    for url in urls:
        print("Робимо запит: ", url)
        response = session.get(url, headers=headers)
        for ad in response.html.xpath('//div[@data-cy="l-card"]'):
            product = dict()
            href = ad.xpath('//a/@href')[0]
            product['link'] = 'https://www.olx.ua' + href
            name = ad.xpath('//h6/text()')[0]
            product['name'] = name

            try:
                price = ad.xpath('//p[@data-testid="ad-price"]/text()')[0]
                product['price'] = int(price.replace('грн.', '').replace(' ', ''))
            except IndexError:
                continue

            if product['price'] < min_price:
                continue

            if not min_price_product or (min_price_product['price'] > product['price']):
                min_price_product = product

    return min_price_product


if __name__ == "__main__":
    phrase = input("Введіть назву товару: ")
    min_product = olx_min_finder(phrase)
    pprint(min_product)
