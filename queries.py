from elasticsearch import Elasticsearch

# from query import basic_search, standard_analyzer

INDEX = "metaphors_new"
client = Elasticsearch(
    "https://localhost:9200",
    verify_certs=False,
    http_auth=["elastic", "N*rb-0Pfb33UC_YbHqYt"],
)


def standard_analyzer(query):
    q = {"analyzer": "standard", "text": query}
    return q


def basic_search(query):
    # import pdb
    # pdb.set_trace()
    q = {"query": {"query_string": {"query": query}}}
    return q


def search(query):
    query_body = basic_search(query)
    print("Searching ")
    res = client.search(index=INDEX, body=query_body)
    print(res)
    return res


def basic_search_with_fields(keywords):
    q = {}
    q["query"] = {}
    q["query"]["bool"] = {}
    q["query"]["bool"]["must"] = []

    for keyword in keywords:
        if keyword == "Year":
            q["query"]["bool"]["must"].append({"range": {keyword: keywords[keyword]}})
        else:
            q["query"]["bool"]["must"].append({"term": {keyword: keywords[keyword]}})

    res = client.search(index=INDEX, body=q)
    return res


def search_advanced_query(query):
    q = {"query": {"wildcard": {"Metaphor": {"value": "*" + query + "*"}}}}
    res = client.search(index=INDEX, body=q)

    return res


# search by lyricist
def lyricistSearch(query):
    q = {"query": {"match": {"lyricist ": {"query": query}}}}
    return q


# search by singer
def singerSearch(query):
    q = {"query": {"match": {"Singer": {"query": query}}}}
    return q
