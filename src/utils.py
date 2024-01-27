import logging

from bs4 import BeautifulSoup
from requests import RequestException

from exceptions import (
    BROKEN_URL,
    RESPONSE_IS_NONE,
    TAG_NOT_FOUND,
    ParserFindTagException)


def get_response(session, url, encoding='utf-8'):
    """
    Получение ответа от сервера по указанному URL.
    """
    try:
        response = session.get(url)
        response.encoding = encoding
        return response
    except RequestException as e:
        raise RequestException(BROKEN_URL.format(url=url)) from e


def find_tag(soup, tag, attrs=None):
    """
    Поиск HTML-тега в объекте BeautifulSoup.
    """
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        logging.error(
            TAG_NOT_FOUND.format(tag=tag, attrs=attrs), stack_info=True
        )
        raise ParserFindTagException(
            TAG_NOT_FOUND.format(tag=tag, attrs=attrs)
        )
    return searched_tag


def get_pep_page_status(session, url):
    """
    Получение статуса PEP с его веб-страницы.
    """
    soup = get_soup(session, url)
    abbr = find_tag(soup, 'abbr')
    return abbr.text


def get_soup(session, url, features='lxml'):
    """
    Получение и парсинг HTML-содержимого по URL.
    """
    try:
        response = get_response(session, url)
    except RequestException as e:
        logging.error(RESPONSE_IS_NONE.format(url=url))
        raise e

    if response is None:
        raise Exception(RESPONSE_IS_NONE.format(url=url))

    soup = BeautifulSoup(response.text, features)
    return soup
