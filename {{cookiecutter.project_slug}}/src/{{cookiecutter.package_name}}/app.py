from fastapi.staticfiles import StaticFiles
from pyview import PyView
from .views import CountLiveView

app = PyView()
app.mount("/static", StaticFiles(packages=[("pyview", "static")]), name="static")

routes = [("/", CountLiveView)]

for path, view in routes:
    app.add_live_view(path, view)
