from suds.client import Client

url = 'http://localhost:8000/?wsdl'
client = Client(url)



response = client.service.mod_product(12, "poire", "pepin", 20)

print(response)