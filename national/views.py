import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def get_recent_sentences():
    url = 'https://www.scourt.go.kr/supreme/info/JpBoardListAction.work?gubun=1'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    result = []
    for item in soup.find('table', attrs={'class': 'tableHor'}).find_all('tr')[1:]:
        tds = item.find_all('td')
        date = tds[1].text.strip()
        number = tds[2].text.strip()
        name = tds[3].text.strip()
        result.append((date, number, name))
    return result


def get_news():
    url = 'https://m.lawtimes.co.kr/List/Case-Curation'
    soup = BeautifulSoup(requests.get(url, {'con': '판결기사'}).text, 'html.parser')
    result = []
    for item in soup.find('section', attrs={'id': 'Content_sectionArticle'}).find_all('article'):
        case = item.find('span', attrs={'class': 'case-num'}).text.strip()
        title = item.find('div', attrs={'class': 'article-txt'}).find('h4').text.strip()
        date = item.find('time').text.strip()
        result.append((case, title, date))
    return result

def index(request):
    recent_sentences = get_recent_sentences()
    news = get_news()
    return render(request, 'index.html', {'recent_sentences': recent_sentences, 'news': news})
