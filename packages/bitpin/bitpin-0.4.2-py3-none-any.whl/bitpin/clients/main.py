import typing as t
import requests
import aiohttp
import asyncio

from .base import BaseClient
from .exceptions import RequestException, APIException


__all__ = [
    'Client',
    'AsyncClient'
]


class Client(BaseClient):
    def __init__(
            self, api_key: t.Optional[str] = None, api_secret: t.Optional[str] = None,
            requests_params: t.Optional[t.Dict[str, t.Any]] = None,
    ):

        super().__init__(api_key, api_secret, requests_params)

        if self.API_KEY and self.API_SECRET:
            self.login()

    def _init_session(self) -> requests.Session:

        headers = self._get_headers()

        session = requests.session()
        session.headers.update(headers)
        return session

    def _request(self, method, uri: str, signed: bool, **kwargs):

        kwargs = self._get_request_kwargs(method, signed, **kwargs)

        self.response = getattr(self.session, method)(uri, **kwargs)
        return self._handle_response(self.response)

    @staticmethod
    def _handle_response(response: requests.Response):
        if not (200 <= response.status_code < 300):
            raise APIException(response, response.status_code, response.text)
        try:
            return response.json()
        except ValueError:
            raise RequestException('Invalid Response: %s' % response.text)

    def _request_api(
            self, method, path: str, signed: bool = False, version=BaseClient.PUBLIC_API_VERSION, **kwargs
    ):
        uri = self._create_api_uri(path, version)
        return self._request(method, uri, signed, **kwargs)

    def _get(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return self._request_api('get', path, signed, version, **kwargs)

    def _post(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return self._request_api('post', path, signed, version, **kwargs)

    def _put(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return self._request_api('put', path, signed, version, **kwargs)

    def _delete(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return self._request_api('delete', path, signed, version, **kwargs)

    def get_token(self, api_key: str = None, api_secret: str = None) -> t.Dict:
        return self._post(
            'usr/api/login/',
            json={
                'api_key': api_key or self.API_KEY,
                'secret_key': api_secret or self.API_SECRET
            }
        )

    def login(self, api_key: str = None, api_secret: str = None) -> t.Dict:
        res = self.get_token(api_key, api_secret)
        self.ACCESS_TOKEN = res['access']
        self.REFRESH_TOKEN = res['refresh']
        return res

    def refresh_token(self, refresh_token: str = None) -> t.Dict:
        return self._post(
            'usr/refresh_token/',
            json={
                'refresh': refresh_token or self.REFRESH_TOKEN
            }
        )

    def get_user_info(self):
        return self._get('usr/info/', signed=True)

    def get_currencies_info(self, currency_id: int = None, page: int = 1) -> t.Dict:
        res = self._get('mkt/currencies/', params={'page': page})
        if currency_id:
            res = self._pick(res, 'id', currency_id)
        return res

    def get_markets_info(self, market_id: int = None, page: int = 1) -> t.Dict:
        res = self._get('mkt/markets/', params={'page': page})
        if market_id:
            res = self._pick(res, 'id', market_id)
        return res

    def get_wallets(self, wallet_id: int = None) -> t.Dict:
        res = self._get('wlt/wallets/', signed=True)
        if wallet_id:
            res = self._pick(res, 'id', wallet_id)
        return res

    def get_orderbook(self, market_id: int, type: str) -> t.Dict:
        return self._get(f'mth/actives/{market_id}', version='v2', params={'type': type})

    def get_latest_trades(self, market_id: int) -> t.Dict:
        return self._get(f'mth/matches/{market_id}')

    def get_user_orders(
            self, market_id: int = None, type: str = None, state: str = None, mode: str = None, identifier: str = None
    ) -> t.Dict:
        res = self._get('odr/orders/', signed=True)

        if market_id:
            res = self._pick(res, 'id', market_id)

        if type:
            res = self._pick(res, 'type', type)

        if state:
            res = self._pick(res, 'state', state)

        if mode:
            res = self._pick(res, 'mode', mode)

        if identifier:
            res = self._pick(res, 'identifier', identifier)

        return res

    def create_order(
            self, market_id: int, type: str, mode: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        json = {
            'market': market_id,
            'amount1': amount,
            'price': price,
            'mode': mode,
            'type': type,
            'identifier': identifier
        }
        if mode.upper() == self.ORDER_MODE_LIMIT:
            json.update({'price_limit': price})
        return self._post('odr/orders/', signed=True, json=json)

    def order_limit(
            self, market_id: int, type: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return self.create_order(market_id, type, self.ORDER_MODE_LIMIT, amount, price, identifier)

    def order_market(
            self, market_id: int, type: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return self.create_order(market_id, type, self.ORDER_MODE_MARKET, amount, price, identifier)

    def order_limit_buy(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        return self.order_limit(market_id, self.TYPE_BUY, amount, price, identifier)

    def order_limit_sell(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        return self.order_limit(market_id, self.TYPE_SELL, amount, price, identifier)

    def order_market_buy(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        return self.order_market(market_id, self.TYPE_BUY, amount, price, identifier)

    def order_market_sell(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        return self.order_market(market_id, self.TYPE_SELL, amount, price, identifier)

    def cancel_order(self, order_id: str) -> t.Dict:
        return self._delete(f'odr/orders/{order_id}', signed=True)

    def get_user_trades(self, market_id: int = None, type: str = None) -> t.Dict:
        res = self._get('odr/matches', signed=True)

        if market_id:
            res = self._pick(res, 'id', market_id)

        if type:
            res = self._pick(res, 'type', type)

        return res

    def close_connection(self):
        if self.session:
            self.session.close()

    def __del__(self):
        self.close_connection()


class AsyncClient(BaseClient):
    def __init__(
            self, api_key: t.Optional[str] = None, api_secret: t.Optional[str] = None,
            requests_params: t.Optional[t.Dict[str, t.Any]] = None,
            loop: t.Optional[asyncio.AbstractEventLoop] = None
    ):

        super().__init__(api_key, api_secret, requests_params)
        self.loop = loop or asyncio.get_event_loop()

        if api_key and api_secret:
            self.loop.run_until_complete(self.login())

    def _init_session(self) -> aiohttp.ClientSession:
        session = aiohttp.ClientSession(
            loop=self.loop,
            headers=self._get_headers()
        )
        return session

    async def _request(self, method, uri: str, signed: bool, **kwargs):

        kwargs = self._get_request_kwargs(method, signed, **kwargs)

        async with getattr(self.session, method)(uri, **kwargs) as response:
            self.response = response
            return await self._handle_response(response)

    @staticmethod
    async def _handle_response(response: aiohttp.ClientResponse):
        if not str(response.status).startswith('2'):
            raise APIException(response, response.status, await response.text())
        try:
            return await response.json()
        except ValueError:
            txt = await response.text()
            raise RequestException(f'Invalid Response: {txt}')

    async def _request_api(self, method, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs):
        uri = self._create_api_uri(path, version)
        return await self._request(method, uri, signed, **kwargs)

    async def _get(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return await self._request_api('get', path, signed, version, **kwargs)

    async def _post(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return await self._request_api('post', path, signed, version, **kwargs)

    async def _put(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return await self._request_api('put', path, signed, version, **kwargs)

    async def _delete(self, path, signed=False, version=BaseClient.PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        return await self._request_api('delete', path, signed, version, **kwargs)

    @classmethod
    async def create(
            cls, api_key: t.Optional[str] = None, api_secret: t.Optional[str] = None,
            requests_params: t.Optional[t.Dict[str, t.Any]] = None,
            loop: t.Optional[asyncio.AbstractEventLoop] = None
    ) -> 'AsyncClient':

        self = cls(api_key, api_secret, requests_params, loop)

        await self.login()

        return self

    async def get_token(self, api_key: str = None, api_secret: str = None) -> t.Dict:
        return await self._post(
            'usr/api/login/',
            json={
                'api_key': api_key or self.API_KEY,
                'secret_key': api_secret or self.API_SECRET
            }
        )

    async def login(self, api_key: str = None, api_secret: str = None) -> t.Dict:
        res = await self.get_token(api_key, api_secret)
        self.ACCESS_TOKEN = res['access']
        self.REFRESH_TOKEN = res['refresh']
        return res

    async def refresh_token(self, refresh_token: str = None) -> t.Dict:
        return await self._post(
            'usr/refresh_token/',
            json={
                'refresh': refresh_token or self.REFRESH_TOKEN
            }
        )

    async def get_user_info(self):
        return await self._get('usr/info/', signed=True)

    async def get_currencies_info(self, currency_id: int = None, page: int = 1) -> t.Dict:
        res = await self._get('mkt/currencies/', params={'page': page})
        if currency_id:
            res = self._pick(res, 'id', currency_id)
        return res

    async def get_markets_info(self, market_id: int = None, page: int = 1) -> t.Dict:
        res = await self._get('mkt/markets/', params={'page': page})
        if market_id:
            res = self._pick(res, 'id', market_id)
        return res

    async def get_wallets(self, wallet_id: int = None) -> t.Dict:
        res = await self._get('wlt/wallets/', signed=True)
        if wallet_id:
            res = self._pick(res, 'id', wallet_id)
        return res

    async def get_orderbook(self, market_id: int, type: str) -> t.Dict:
        return await self._get(f'mkt/orderbook/{market_id}', version='v2', params={'type': type})

    async def get_latest_trades(self, market_id: int) -> t.Dict:
        return await self._get(f'mth/matches/{market_id}')

    async def get_user_orders(
            self, market_id: int = None, type: str = None, state: str = None, mode: str = None, identifier: str = None
    ) -> t.Dict:
        res = await self._get('odr/orders/', signed=True)

        if market_id:
            res = self._pick(res, 'id', market_id)

        if type:
            res = self._pick(res, 'type', type)

        if state:
            res = self._pick(res, 'state', state)

        if mode:
            res = self._pick(res, 'mode', mode)

        if identifier:
            res = self._pick(res, 'identifier', identifier)

        return res

    async def create_order(
            self, market_id: int, type: str, mode: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        json = {
            'market': market_id,
            'amount1': amount,
            'price': price,
            'mode': mode,
            'type': type,
            'identifier': identifier
        }
        if mode.upper() == self.ORDER_MODE_LIMIT:
            json.update({'price_limit': price})
        return await self._post('odr/orders/', signed=True, json=json)

    async def order_limit(
            self, market_id: int, type: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return await self.create_order(market_id, type, self.ORDER_MODE_LIMIT, amount, price, identifier)

    async def order_market(
            self, market_id: int, type: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return await self.create_order(market_id, type, self.ORDER_MODE_MARKET, amount, price, identifier)

    async def order_limit_buy(
            self, market_id: int, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return await self.order_limit(market_id, self.TYPE_BUY, amount, price, identifier)

    async def order_limit_sell(
            self, market_id: int, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return await self.order_limit(market_id, self.TYPE_SELL, amount, price, identifier)

    async def order_market_buy(
            self, market_id: int, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return await self.order_market(market_id, self.TYPE_BUY, amount, price, identifier)

    async def order_market_sell(
            self, market_id: int, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        return await self.order_market(market_id, self.TYPE_SELL, amount, price, identifier)

    async def cancel_order(self, order_id: str) -> t.Dict:
        return await self._delete(f'odr/orders/{order_id}', signed=True)

    async def get_user_trades(self, market_id: int = None, type: str = None) -> t.Dict:
        res = await self._get('odr/matches', signed=True)

        if market_id:
            res = self._pick(res, 'id', market_id)

        if type:
            res = self._pick(res, 'type', type)

        return res

    async def close_connection(self):
        if self.session:
            assert self.session
            await self.session.close()

    def __del__(self):
        asyncio.get_event_loop().create_task(self.close_connection())
