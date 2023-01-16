from flask import Flask, render_template, request
from searchquery import search
from elasticsearch_dsl import Index

app = Flask(__name__,template_folder='templates')


# @app.route('/search', methods=['GET', 'POST'])

@app.route('/search', methods=['GET', 'POST'])
def hello_world():
    import pdb
    # pdb.set_trace()
    # return "hello world"
    if request.method == 'POST':
        
        query = request.form['searchTerm']
        
        
        res = search(query)
        
        hits = res['hits']['hits']
        time = res['took']
        # aggs = res['aggregations']
        num_results =  res['hits']['total']['value']

        return render_template('result.html', query=query, hits=hits, num_results=num_results,time=time)

    if request.method == 'GET':
        # pdb.set_trace()
        return render_template('result.html', init='True')


if __name__ == '__main__':
    app.debug = True
    app.run()