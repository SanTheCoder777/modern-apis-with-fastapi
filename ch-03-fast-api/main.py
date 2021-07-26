import fastapi
import uvicorn
from typing import Optional
# import json
api = fastapi.FastAPI()


@api.get("/")
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the APT</h1>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=4&y=7'>api/calculate?x=4&y=6</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    return fastapi.responses.HTMLResponse(content=body, status_code=200)


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    value = x + y
    if z == 0:
        # return fastapi.Response(content=json.dumps({"error": "ERROR: Z cannot be zero"}),
        #                         media_type="application/json",
        #                         status_code=400)
        return fastapi.responses.JSONResponse(content={"error": "ERROR: Z cannot be zero"},
                                              status_code=400)
    if z is not None:
        value /= z
    resp_data = {
        "x": x,
        "y": y,
        "z": z,
        "value": value
    }
    # return resp_data
    # return fastapi.Response(content=json.dumps(resp_data),
    #                         media_type="application/json",
    #                         status_code=200)
    return fastapi.responses.JSONResponse(content=resp_data,
                                          status_code=200)


uvicorn.run(api, host="127.0.0.1", port=8001)
