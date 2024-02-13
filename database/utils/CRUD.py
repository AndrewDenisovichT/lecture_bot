from typing import Dict, List, TypeVar

from peewee import ModelSelect

from database.common.models import ModelBase
from ..common.models import db

T = TypeVar('T')


def _store_data(db: db, model: T, *data: List[Dict]) -> None:
    """
    Операция записи в БД
    :param db: наша БД
    :param model: таблица в БД
    :param data: информация для записи
    :return: None
    """
    with db.atomic():  # атомарность транзакций
        model.insert_many(*data).execute()  # вствить сразу несколько записей в таблицу


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    """
    Операция извлечения информации из БД
    :param db:
    :param model:
    :param columns:
    :return:
    """
    with db.atomic():
        response = model.select(*columns)

    return response


class CRUDInterface():

    @staticmethod
    def create():  # store
        return _store_data

    @staticmethod
    def retrieve():
        return _retrieve_all_data

if __name__=='__main__':
    _store_data()
    _retrieve_all_data()
    CRUDInterface()