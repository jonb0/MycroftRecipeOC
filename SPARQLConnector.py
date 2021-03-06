from SPARQLWrapper import SPARQLWrapper, JSON

def execSPARQLQuery( selectQuery ,whereQuery ):
	
	sparql = SPARQLWrapper("http://graphdb.sti2.at:8080/sparql")

	query = """
	PREFIX schema: <http://schema.org/>
	SELECT  %s
	#FROM <https://broker.semantify.it/graph/O7PY8ri5T2/WxGcA2Nj1O/latest>
	FROM <https://broker.semantify.it/graph/O7PY8ri5T2/WxGcA2Nj1O/2018-11-03-09-51>
	WHERE {
		?s a schema:Recipe .
		%s
	} LIMIT 10
	""" % (selectQuery, whereQuery)

	sparql.setReturnFormat(JSON)
 
	sparql.setQuery(query)
	
	return sparql.query().convert()

selectQuery="?name"
whereQuery="?s schema:name ?name ."
results = execSPARQLQuery(selectQuery, whereQuery)

print(results)
