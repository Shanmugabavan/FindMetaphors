from elasticsearch import Elasticsearch

from query import basic_search, standard_analyzer
# from rules import process

INDEX = 'metaphors_new'
# client = Elasticsearch(HOST="https://localhost", PORT=9200,http_auth=('elastic', 'N*rb-0Pfb33UC_YbHqYt'))
client = Elasticsearch("https://elastic:N*rb-0Pfb33UC_YbHqYt@localhost:9200",verify_certs=False)

def search(query):
    # result = client. (index=INDEX,body=standard_analyzer(query))
    # keywords = result ['tokens']['token']
    # print(keywords)

    # query_body= process(query)
    query_body = basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    return res