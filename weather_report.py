import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'loc, cond, temperature, scale')


def print_the_header():
    print('------------------------------------------')
    print('             FORECAST APP')
    print('------------------------------------------')


def get_html_from_web(zip_code):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zip_code)
    response = requests.get(url)

    return response.text


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def get_weather_from_html(html):
    # $('.city-header h1 span').innerHTML
    # city_css = 'div.city-header h1 span'
    # weather_condition_css = 'div.condition-icon p'
    # weather_temp_css = 'div.wu-value'
    # weather_temp_css = 'div.wu-label'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find("div", {"class": "city-header"}).find('h1').find('span').get_text()
    condition = soup.find("div", {"class": "condition-icon"}).find('p').get_text()
    temperature = soup.find("span", {"class": "wu-value"}).get_text()
    temp_type = '°' + soup.find("span", {"class": "wu-label"}).get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temperature = cleanup_text(temperature)
    temp_type = cleanup_text(temp_type)

    report = WeatherReport(loc=loc, cond=condition, temperature=temperature, scale=temp_type)
    return report


def main():

    print_the_header()

    zip_code = input('What zip code do you want the weather for (97201)? ')
    html = get_html_from_web(zip_code)
    report = get_weather_from_html(html)

    print('The weather in {} is {} and {} {}'.format(report.loc, report.cond, report.temperature, report.scale))


if __name__ == '__main__':
    main()
