import synchronous.routing
import asynchronous.routing

websocket_urlpatterns = [
    *synchronous.routing.websocket_urlpatterns,
    *asynchronous.routing.websocket_urlpatterns
]
