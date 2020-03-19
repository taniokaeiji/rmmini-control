from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import broadlink
import db
from models import Rmmini, Command

app = FastAPI()
device = None

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    devices = db.session.query(Rmmini).all()
    db.session.close()

    return templates.TemplateResponse('index.html', {'request': request, 'devices': devices})

@app.get("/rmmini/discovery")
async def rmmini_discovery():
    devices = broadlink.discover(timeout=10)
    #if len(devices):
    #    for node in devices:

@app.get("/rmmini/{rmmini_id}/command_list")
async def rmmini_command_list(rmmini_id: int, request: Request):
    commands = db.session.query(Command).filter(Command.device_id == rmmini_id).all()
    db.session.close()

    return templates.TemplateResponse('commands.html', {'commands': commands, 'request': request})

@app.get("/rmmini/{rmmini_id}/learn")
async def rmmini_learn():
    # enter_learning()
    # check_data()
    pass

@app.get("/rmmini/{rmmini_id}/{func_id}/send")
async def rmmini_send(request: Request, rmmini_id: int, func_id: int):
    rmmini_info = db.session.query(Rmmini).filter(Rmmini.id == rmmini_id).first()
    # DBのデータからホスト情報を作成
    #mac = bytearray.fromhex(rmmini_info.mac_address)
    device = broadlink.gendevice(rmmini_info.devtype, (rmmini_info.host, 80), bytearray.fromhex(rmmini_info.mac_address))
    if device.auth():
        ir_command = db.session.query(Command.ir_command).filter(
            Command.device_id == rmmini_id,
            Command.id == func_id).value(Command.ir_command)
        db.session.close()
        device.send_data(bytearray.fromhex(ir_command))
    else:
        return False
