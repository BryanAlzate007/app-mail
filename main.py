from msal import ConfidentialClientApplication


client_id = 'CLIENT_ID'
client_secret = 'TU_CLIENT_SECRET'
tenant_id = 'TU_TENANT_ID'


authority = f'https://login.microsoftonline.com/{tenant_id}'
scope = ['https://graph.microsoft.com/.default']

app = ConfidentialClientApplication(
    client_id,
    authority=authority,
    client_credential=client_secret
)

def get_access_token():
    result = app.acquire_token_for_client(scopes=scope)
    if 'access_token' in result:
        return result['access_token']
    else:
        raise Exception(f"No se pudo obtener el token de acceso: {result.get('error_description')}")