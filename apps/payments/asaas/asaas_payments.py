from django.conf import settings
from urllib.parse import urlencode
from urllib.parse import urljoin
import requests

class AsaasBasePayment:
    def __init__(self):
        self._API_KEY = settings.ASAAS_API_KEY
        self._BASE_URL = (
            'https://api.asaas.com/'
            if not settings.DEBUB
            else 'https://api-sandbox.asaas.com/v3/'
        )

    def _send_request(self, path, method='GET', body=None, headers={}, params_url={}, user_api_key=True):
        method.upper()
        url = self._mount_url(path, params_url)

        if not isinstance(headers, dict):
            headers = {}
        
        if user_api_key:
            headers['access_token'] = str(self._API_KEY)

        headers['Content-Type'] = 'application/json'

        match method:
            case 'GET':
                response = requests.get(url, headers=headers)
            case 'POST':
                response = requests.post(url, headers=headers, data=body)
            case 'PUT':
                response = requests.put(url, headers=headers, data=body)
            case 'DELETE':
                response = requests.delete(url, headers=headers)
            case _:
                raise ValueError('Method invalid')

    def _mount_url(self, path, params_url):
        if isinstance(params_url, dict):
            parameters = urlencode(params_url)
        
        url = urljoin(self._BASE_URL, path)
        if parameters:
            url = f'{url}?{parameters}'
        print(url)

class AsaasCustomer(AsaasBasePayment):
    def create_customer(self, **kwargs):
        '''
        Possibilidades de parametros para kwargs no link:
        https://docs.asaas.com/reference/criar-novo-cliente
        '''
        if 'name' not in kwargs.keys() or 'cpfCnpj' not in kwargs.keys():
            raise KeyError('name e cpfCnpj são obrigatorios')
        
        return self._send_request(
            path='customers',
            method='POST',
            body=kwargs
        ).json()
    
    def list_customers(self, **kwargs):
        '''
        Possibilidades de parametros para kwargs no link:
        https://docs.asaas.com/reference/listar-clientes
        '''
        return self._send_request(
            path='customers',
            params_url=kwargs
        ).json()
    
    def get_customer(self, customer_id):
        return self._send_request(
            path=f'customers/{customer_id}'
        ).json()