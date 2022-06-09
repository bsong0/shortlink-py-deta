from fastapi import FastAPI, Response, status
from fastapi.responses import RedirectResponse, PlainTextResponse

import db.DetaDBConnectionImpl

app = FastAPI()
database = db.DetaDBConnectionImpl.DetaDBConnectionImpl()


@app.get("/{path}")
async def root(path: str, src: str = None, to: str = None):
    if path == 'new':
        database.put(src, to)
        return {'source': src, 'to': to}

    if path == 'remove':
        database.delete(src)
        return "Success"

    link = database.get(path)
    if link is not None:
        return RedirectResponse(url=link['value'], status_code=302)
    else:
        return PlainTextResponse("Not Found", 404)