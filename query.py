import json


def standard_analyzer(query):
    q = {
        "analyzer": "standard",
        "text": query
    }
    return q


def basic_search(query):
    # import pdb
    # pdb.set_trace()
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q

def basic_search_with_fields(fields):
    """
    example of query
    {
 "query": {
    "bool" : {
      "must" : [
        {"term" : { "Composer" : "ஏ. ஆர். ரஹ்மான்" }},
 	      {"term" : { "Lyricist" : "வாலி" }},
		{"term":{"Star":"மாதவன்"}},
		{"range" : {"Year" : { "gte" : 2000, "lte" : 2010 }}}
      ]
    }
 }
}
    """

    return q
