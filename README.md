## Setup the ElasticSearch
1. Download Elastic Search  and Setup Elastic Search - 
	1. `https://www.elastic.co/downloads/elasticsearch`
	2. Extract the downloaded folder
	3. To up the elasticsearch server - `bin/elasticsearch.bat`
	4. Default username - `elastic`
		Default password - `changeme`
			Optional - resetting password - `bin/elasticsearch-reset-password.bat`
	5. Save the key (When very first time running which we need for setup Kibana)
	6. Can check the server is up using: `https://127.0.0.1:9200/`
## Setup the Kibana
1. Download Kibana and setup kibana
	1. `https://www.elastic.co/downloads/kibana` 
	2. Extract the downloaded folder
	3. To up the kibana server - `bin/kibana.bat`
2. Setup kibana with Elastic search server
	1. Elastic search server should be up
	2. go to url: `https://localhost:5601/app/home` 
	3. Enter the key of elastic search
	4. Enter username and password
3. Upload the csv file and put the index - `metaphors_new`
4. Now index and keywords will be automatically generated and can view in the dashboard

## Setup the environment

 1. Clone the Repository - `git clone https://github.com/Shanmugabavan/FindMetaphors.git`
 2. change the directory to repository - `cd FindMetaphors`
 3. Creating the python virtual environment
 `python -m venv env` 
 `"env/Scripts/activate.bat"` 
 4. Install all the dependencies - `pip install -r requirements.txt`
 5. In the `searchquery.py`edit the file accordingly - `INDEX = 'metaphors_new'`
	    ` client = Elasticsearch("https://username:password@localhost:9200",verify_certs=False)`
6.Edit the search.html	    
7. Run the python flask app
	1. flask --app app --debug run
	2. Copy the URL and paste to Browser and route to `/search`
		-`http://localhost:5000/search`
	3. Search the metaphors of tamil songs :)
