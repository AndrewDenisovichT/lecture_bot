from database.utils.CRUD import CRUDInterface
from database.common.models import db, History

with db:
    db.create_tables([History])

crud = CRUDInterface()

if __name__ == '__main__':
    crud()
