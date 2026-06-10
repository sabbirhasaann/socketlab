import synchronous.routing
import asynchronous.routing
import chat.routing

websocket_urlpatterns = [
    *synchronous.routing.websocket_urlpatterns,
    *asynchronous.routing.websocket_urlpatterns,
    *chat.routing.websocket_urlpatterns,
]
