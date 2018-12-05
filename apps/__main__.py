# Third
from loafer.managers import LoaferManager

# Local
from .routes import routes

service = LoaferManager(routes=routes)
service.run()
