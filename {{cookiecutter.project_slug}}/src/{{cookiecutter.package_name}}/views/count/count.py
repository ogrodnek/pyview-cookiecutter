from pyview import LiveView, LiveViewSocket
from pyview.events import event, BaseEventHandler

from typing import TypedDict


class CountContext(TypedDict):
    count: int


class CountLiveView(BaseEventHandler, LiveView[CountContext]):
    async def mount(self, socket: LiveViewSocket[CountContext], session):
        socket.context = CountContext({"count": 0})

    @event("increment")
    async def handle_inrecrement(
        self, event, payload, socket: LiveViewSocket[CountContext]
    ):
        socket.context["count"] += 1

    @event("decrement")
    async def handle_decrement(
        self, event, payload, socket: LiveViewSocket[CountContext]
    ):
        socket.context["count"] -= 1

    async def handle_params(self, url, params, socket: LiveViewSocket[CountContext]):
        # check if "c" is in params
        # and if so set self.count to the value
        if "c" in params:
            socket.context["count"] = int(params["c"][0])
