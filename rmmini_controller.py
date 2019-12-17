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
async def rmmini_command_list():
    print()

@app.get("/rmmini/{rmmini_id}/learn")
async def rmmini_learn():
    # enter_learning()
    # check_data()
    pass

@app.get("/rmmini/{rmmini_id}/{func_id}/send")
async def rmmini_send():
    # send_data(ir_packet)
    pass

def rmmini_getdevice():
    device = rmmini.gendevice(devtype, host, mac)
    return device.auth()