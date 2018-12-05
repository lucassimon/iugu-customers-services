# Third


class CreateCustomerHandler:

    def __init__(self):
        # TODO: Create a partner instance
        # because its handler will instantiate in routes urls

        # TODO: Read a .env with python-dotenv here or in partner.py?
        pass

    headers = {
        'Content-Type': 'application/json'
    }

    async def handle(self, message, *args, **kwargs):
        print(args)
        # TODO: Get message
        print(message)
        # TODO: Call the partner create method to do the integration
        # if an error ocurred in response returns false
        # if an error was catch in request returns false
        return True
