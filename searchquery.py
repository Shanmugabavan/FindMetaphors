from elasticsearch import Elasticsearch

from query import basic_search, standard_analyzer

INDEX = 'metaphors_new'
client = Elasticsearch("https://localhost:9200", verify_certs=False,
                   http_auth=['elastic', 'N*rb-0Pfb33UC_YbHqYt'],)

def search(query):
    query_body = basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    print(res)
    return res

def basic_search_with_fields(fields):
    q = {}
    q["query"] = {}
    q["query"]["bool"] = {}
    q["query"]["bool"]["must"] = []
    
    for field in fields:
        if field == 'Year':
            q["query"]["bool"]["must"].append({"range":{field:fields[field]}})
        else:
            q["query"]["bool"]["must"].append({"term":{field:fields[field]}})


    res = client.search(index=INDEX, body=q)
    return res


def search_advanced_query(query):
    q = {
       "query": {
            "wildcard": {
            "Metaphor": {
                "value": "*"+query+"*"
            }
            }
        }
    }
    res = client.search(index=INDEX, body=q)

    return res