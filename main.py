from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Response, status
from fastapi.responses import RedirectResponse, PlainTextResponse

import db.DetaDBConnectionImpl

app = FastAPI()
database = db.DetaDBConnectionImpl.DetaDBConnectionImpl()
templates = Jinja2Templates(directory='templates')

@app.get("/{path}")
async def root(path: str, src: str = None, to: str = None, nojs: bool = False):
    if path == 'new':
        if src is not None and to is not None:
            database.put(src, to)
            return {'source': src, 'to': to}
        else:
            return "Not Found"

    if path == 'del':
        if src is not None:
            database.delete(src)
            return "Success"
        else:
            return "Not Found"

    link = database.get(path)
    if link is not None:
        if nojs:
            return RedirectResponse(url=link['value'], status_code=302)
        else:
            return templates.TemplateResponse("default.html", {"url": link})
    else:
        return PlainTextResponse("Not Found", 404)