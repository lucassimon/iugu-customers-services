# Third
from loafer.ext.aws.routes import SNSQueueRoute

# Local
from .handlers import CreateCustomerHandler

routes = [
    SNSQueueRoute(
        name='route1',
        provider_queue='iugu-customers-main-prd',
        provider_options={
            'endpoint': 'localhost:4100'
        },
        handler=CreateCustomerHandler(),
    )
]
