import typing as t
from abc import ABC, abstractmethod

import requests


__all__ = [
    'BaseClient',
]


class BaseClient(ABC):
    API_URL = 'https://api.bitpin.ir'
    PUBLIC_API_VERSION = 'v1'

    REQUEST_TIMEOUT: float = 10

    TYPE_BUY = 'BUY'
    TYPE_SELL = 'SELL'

    ORDER_MODE_LIMIT = 'LIMIT'
    ORDER_MODE_MARKET = 'MARKET'

    def __init__(
            self, api_key: t.Optional[str] = None, api_secret: t.Optional[str] = None,
            requests_params: t.Optional[t.Dict[str, str]] = None,
    ):
        self.API_KEY = api_key
        self.API_SECRET = api_secret

        self.ACCESS_TOKEN = None
        self.REFRESH_TOKEN = None

        self._requests_params = requests_params
        self.session = self._init_session()

    @staticmethod
    def _get_kwargs(locals_: t.Dict, del_keys: t.List[str] = None, del_nones: bool = False) -> t.Dict:
        _del_keys = ['self', 'cls']
        if del_keys is not None:
            _del_keys.extend(del_keys)

        if del_nones is True:
            return {key: value for key, value in locals_.items() if (key not in _del_keys) and (value is not None)}

        return {key: value for key, value in locals_.items() if key not in _del_keys}

    @staticmethod
    def _get_headers() -> t.Dict:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        return headers

    def _create_api_uri(self, path: str, version: str = PUBLIC_API_VERSION) -> str:
        _ = self.API_URL + '/' + version + '/' + path
        if not _.endswith('/'):
            _ += '/'
        return _

    def _get_request_kwargs(self, method, signed: bool, **kwargs) -> t.Dict:
        kwargs['timeout'] = self.REQUEST_TIMEOUT

        if self._requests_params:
            kwargs.update(self._requests_params)

        data = kwargs.get('data', None)
        if data and isinstance(data, dict):
            kwargs['data'] = data

            if 'requests_params' in kwargs['data']:
                kwargs.update(kwargs['data']['requests_params'])
                del (kwargs['data']['requests_params'])

        if signed is True:
            headers = kwargs.get('headers', {})
            headers.update({'Authorization': f'Bearer {self.ACCESS_TOKEN}'})
            kwargs['headers'] = headers

        if data and method == 'get':
            kwargs['params'] = '&'.join('%s=%s' % (data[0], data[1]) for data in kwargs['data'])
            del (kwargs['data'])

        return kwargs

    @staticmethod
    def _pick(response: t.Dict, key: str, value: t.Any, result_key: str = 'results') -> t.Dict:
        for d in response.get(result_key):
            if d[key] == value:
                response[result_key] = d
                return response
        raise ValueError(f"{key} {value} not found in {response}")

    @staticmethod
    def _validate(value: t.Any, type: t.Type, valids: t.List[t.Any] = None) -> t.Any:
        if valids is not None:
            if value not in valids:
                raise ValueError(f"{value} is not in {valids}")
        if not isinstance(value, type):
            raise TypeError(f"{value} is not {type}")
        return value

    @abstractmethod
    def _init_session(self) -> requests.Session:
        raise NotImplementedError('_init_session not implemented')

    @abstractmethod
    def _request(self, method, uri: str, signed: bool, **kwargs):
        raise NotImplementedError('_request not implemented')

    @staticmethod
    @abstractmethod
    def _handle_response(response: requests.Response):
        raise NotImplementedError('_handle_response not implemented')

    @abstractmethod
    def _request_api(
            self, method, path: str, signed: bool = False, version=PUBLIC_API_VERSION, **kwargs
    ):
        raise NotImplementedError('_request_api not implemented')

    @abstractmethod
    def _get(self, path, signed=False, version=PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        raise NotImplementedError('_get not implemented')

    @abstractmethod
    def _post(self, path, signed=False, version=PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        raise NotImplementedError('_post not implemented')

    @abstractmethod
    def _put(self, path, signed=False, version=PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        raise NotImplementedError('_put not implemented')

    @abstractmethod
    def _delete(self, path, signed=False, version=PUBLIC_API_VERSION, **kwargs) -> t.Dict:
        raise NotImplementedError('_delete not implemented')

    @abstractmethod
    def get_token(self, api_key: str = None, api_secret: str = None) -> t.Dict:
        raise NotImplementedError('get_token not implemented')

    @abstractmethod
    def login(self, api_key: str = None, api_secret: str = None) -> t.Dict:
        raise NotImplementedError('login not implemented')

    @abstractmethod
    def refresh_token(self, refresh_token: str = None) -> t.Dict:
        raise NotImplementedError('refresh_token not implemented')

    @abstractmethod
    def get_user_info(self) -> t.Dict:
        raise NotImplementedError('get_market_stats not implemented')

    @abstractmethod
    def get_currencies_info(self, currency_id: int = None, page: int = 1) -> t.Dict:
        raise NotImplementedError('get_currencies not implemented')

    @abstractmethod
    def get_markets_info(self, market_id: int = None, page: int = 1) -> t.Dict:
        raise NotImplementedError('get_currencies_stats not implemented')

    @abstractmethod
    def get_wallets(self, currency_id: int = None) -> t.Dict:
        raise NotImplementedError('get_orderbook not implemented')

    @abstractmethod
    def get_orderbook(self, market_id: int, type: str) -> t.Dict:
        raise NotImplementedError('get_recent_trades not implemented')

    @abstractmethod
    def get_latest_trades(self, market_id: int) -> t.Dict:
        raise NotImplementedError('get_profile not implemented')

    @abstractmethod
    def get_user_orders(
            self, market_id: int = None, type: str = None, state: str = None, mode: str = None, identifier: str = None
    ) -> t.Dict:
        raise NotImplementedError('get_cards not implemented')

    @abstractmethod
    def create_order(
            self, market_id: int, type: str, mode: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        raise NotImplementedError('add_card not implemented')

    @abstractmethod
    def cancel_order(self, order_id: str) -> t.Dict:
        raise NotImplementedError('delete_card not implemented')

    @abstractmethod
    def get_user_trades(self, market_id: int = None, type: str = None) -> t.Dict:
        raise NotImplementedError('get_ibans not implemented')

    @abstractmethod
    def order_market(
            self, market_id: int, type: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        raise NotImplementedError('order_market not implemented')

    @abstractmethod
    def order_limit(
            self, market_id: int, type: str, amount: float, price: float = None, identifier: str = None
    ) -> t.Dict:
        raise NotImplementedError('order_limit not implemented')

    @abstractmethod
    def order_market_buy(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        raise NotImplementedError('order_market_buy not implemented')

    @abstractmethod
    def order_market_sell(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        raise NotImplementedError('order_market_sell not implemented')

    @abstractmethod
    def order_limit_buy(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        raise NotImplementedError('order_limit_buy not implemented')

    @abstractmethod
    def order_limit_sell(self, market_id: int, amount: float, price: float = None, identifier: str = None) -> t.Dict:
        raise NotImplementedError('order_limit_sell not implemented')

    @abstractmethod
    def close_connection(self):
        raise NotImplementedError('close_connection not implemented')
