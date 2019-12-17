from datetime import datetime

from db import Base

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

import hashlib

SQLITE3_NAME = "./db.sqlite3"

class Rmmini(Base):
    """
    Devicesテーブル

    id : 主キー
    name : 識別用の名前
    devtype: デバイスタイプ
    host: IPアドレス
    mac_address: MACアドレス
    """
    __tablename__ = 'devices'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    name = Column('name', String(256))
    devtype = Column('devtype', INTEGER(unsigned=True))
    host = Column('host', String(256))
    mac_address = Column('mac_address', String(256))

    def __init__(self, name, devtype, host, mac_address):
        self.name = name
        self.devtype = devtype
        self.host = host
        self.mac_address = mac_address

    def __str__(self):
        return str(self.id) + ':' + self.name

class Command(Base):
    """
    赤外線コマンド

    id : 主キー
    device_id: 外部キー
    target_name: 受信機器
    function_name: 機能名
    ir_command: 赤外線コマンド
    """
    __tablename__ = 'commands'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    device_id = Column('device_id', ForeignKey('devices.id'))
    target_name = Column('target_name', String(256))
    function_name = Column('function_name', String(256))
    ir_command = Column('ir_command', String(512))

    def __init__(self, device_id: int, target_name: str, function_name: str, ir_command: str):
        self.device_id = device_id
        self.target_name = target_name
        self.function_name = function_name
        self.ir_command = ir_command

    def __str__(self):
        pass