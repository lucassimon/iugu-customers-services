# Python
from base64 import b64encode

# Third
from aiohttp import ClientSession, ClientTimeout


class Partner:

    ENDPOINT = "https://api.iugu.com/v1/"
    CUSTOMERS = "{}customers".format(ENDPOINT)
    PLANS = "{}plans".format(ENDPOINT)

    def __init__(self, token):
        self.token = token
        self.timeout = ClientTimeout(total=60)

    async def header(self):
        auth = '{}'.format(self.token)
        auth = b64encode(bytes(auth, 'utf-8')).decode('utf-8')

        return {
            'Content-Type': 'application/json',
            'User-Agent': 'Iugu Python Api ',
            'Accept': 'application/json',
            'Authorization': 'Basic {}'.format(auth)
        }

    async def create(self):
        response = None
        headers = await self.header()

        try:
            async with ClientSession() as session:
                async with session.post(self.CUSTOMERS, headers=headers) as response:
                    data = await response.json()
                    return data

        except Exception as e:
            raise e

        return response

    async def retrive(self):

        response = None
        headers = await self.header()
        # auth = BasicAuth(self.token, '')

        try:
            async with ClientSession() as session:
                async with session.get(self.CUSTOMERS, headers=headers) as response:
                    data = await response.json()
                    return data

        except Exception as e:
            raise e

        return response
