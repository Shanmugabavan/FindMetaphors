from flask import Flask, render_template, request
from searchquery import search, basic_search_with_fields, search_advanced_query
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
        fields = {}
 
        Composer = {
            "arrahman" : "ஏ. ஆர். ரஹ்மான்",
            "ilayaraja" : "இளையராஜா",
            "imman" : "இமான்",
            "yuvan" : "யுவன்"
        }
        Lyricist = {
            "vairamuthu" : "வைரமுத்து",
            "vaali" : "வாலி",
            "na.muthukumar" : "நா. முத்துக்குமார்",
            "damarai" : "தாமரை",
            "yugaparathi" : "யுகபாரதி"
        }
        Singer = {
            "smt" : "சங்கர் மகாதேவன்",
            "karthik" : "கார்த்திக்",
            "hariharan" : "ஹரிகரன்",
            "gosal" : "ஷ்ரேயா கோசல்",
            "spb" : "S.P பாலசுப்ரமணியம்"
        }



        if request.form['Composer'] != 'none':
            fields["Composer"] = Composer[request.form['Composer']]
        if request.form['Lyricist'] != 'none':
            fields["Lyricist"] = Lyricist[request.form['Lyricist']]
        if request.form['Singer'] != 'none':
            fields["Singer"] = Singer[request.form['Singer']]

        fields["Year"] = {
            "gte": int(request.form['start_year']),
            "lte": int(request.form['end_year'])
        }
        res = basic_search_with_fields(fields)
        
        # check request.form dict have basic or advanced key
        print(request.form.get('basic'))
        if request.form['basic'] == 'Basic':
            res = search(query)
            fields = query
        elif request.form['basic'] ==  'Advanced':
            res = search_advanced_query(query)
            fields = query
        else:
            res = basic_search_with_fields(fields)
        
        # res = search(query)


        
        hits = res['hits']['hits']
        time = res['took']
        # aggs = res['aggregations']
        num_results =  res['hits']['total']['value']

        return render_template('result2.html', query=fields, hits=hits, num_results=num_results,time=time)

    if request.method == 'GET':
        # pdb.set_trace()
        return render_template('result2.html', init='True')


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)