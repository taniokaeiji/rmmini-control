import broadlink
import sqlite3

# DBに接続
conn = sqlite3.connect('db.sqlite3')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute('SELECT * FROM devices')
r = c.fetchone()

# DBのデータからホスト情報を作成
devtype = r['devtype']
host = r['host']
mac = bytearray.fromhex(r['mac_address'])
dev = broadlink.gendevice(devtype, (host, 80), mac)

# コマンドを投げる
c.execute('SELECT ir_command FROM commands WHERE id = 1 and device_id = 1')
r = c.fetchone()
data = bytearray.fromhex(r['ir_command'])
dev.send_data(data)
#print(data)

c.close()