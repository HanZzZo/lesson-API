from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

transport = RequestsHTTPTransport(
    url='https://countries.trevorblades.com/',
    verify=True,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

def get_countries_by_continent(continent_code):
    query = gql(f"""
    {{
      continent(code: "{continent_code}") {{
        name
        countries {{
          code
          name
          capital
          languages {{
            name
          }}
        }}
      }}
    }}
    """)
    result = client.execute(query)
    return result["continent"]
