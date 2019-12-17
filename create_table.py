from models import *
import db
import os

if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path) or \
        db.engine.dialect.has_table(db.engine, 'devices') or \
        db.engine.dialect.has_table(db.engine, 'commands'):
        # テーブルを作成する
        Base.metadata.create_all(db.engine)

    # サンプルとしてRMminiを1つ追加
    rmmini = Rmmini(name="リビング", devtype=10039, host='192.168.1.149', mac_address='69c96f34ea34')
    db.session.add(rmmini)
    db.session.commit()

    db.session.close()