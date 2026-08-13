import synchronous.routing
import asynchronous.routing
import chat.routing
import genconsumer.routing

websocket_urlpatterns = [
    *synchronous.routing.websocket_urlpatterns,
    *asynchronous.routing.websocket_urlpatterns,
    *chat.routing.websocket_urlpatterns,
    *genconsumer.routing.websocket_urlpatters,
]
