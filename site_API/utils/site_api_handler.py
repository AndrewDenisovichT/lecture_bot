# Здесь будем писать обращение к двум эндпоинтам
from typing import Dict

import requests


def _make_response(method: str, url: str, headers: Dict, params: Dict,
                   timeout: int, succeess=200):
    # лектор использует запрос через htpps(GET),
    # через requests аргумента methode нет
    """
    Эта функция будет делать запрос на сервер через API
    :param method: лектор использует запрос через htpps(GET)
    :param url:
    :param headers: заголовки
    :param params: это quarystring из main.py
    :param timeout:
    :param succeess: статус запроса
    :return:
    """
    responce = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = responce.status_code

    if status_code == succeess:
        return responce

    return status_code


# Далее мы напишем функции которые будут обрабатывать разные запросы
# Вот эти хвосты url = "https://numbersapi.p.rapidapi.com/6/(21/date)"
# 21/date

def _get_date_fact(method: str, url: str, headers: Dict, params: Dict, date_day: str,
                   date_month: str, timeout: int, func=_make_response):
    url = '{0}/{1}/{2}/date'.format(url, date_month, date_day)

    responce = func(method, url, headers=headers, params=params, timeout=timeout)

    return responce


def _get_math_fact(method: str, url: str, headers: Dict, params: Dict, number: int,
                   timeout: int, func=_make_response):
    url = '{0}/{1}/math'.format(url, number)

    responce = func(method, url, headers=headers, params=params, timeout=timeout)

    return responce


class SiteApiInterface():

    @staticmethod
    def get_date_fact():
        return _get_date_fact

    @staticmethod
    def get_math_fact():
        return _get_math_fact


if __name__=='__main__':
    _make_response()
    _get_date_fact()
    _get_math_fact()

    SiteApiInterface()

    # видео закончил на 1:26:20