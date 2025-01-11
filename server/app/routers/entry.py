from fastapi import APIRouter
from fastapi.responses import HTMLResponse

entryRouter = APIRouter()


@entryRouter.get("/")
def main():
    return HTMLResponse(
        """
            <div style="height:90vh; display:flex; justify-content:center; align-items:center;">
                <h1>Hello Server</h1>
            </div>
        """
    )
