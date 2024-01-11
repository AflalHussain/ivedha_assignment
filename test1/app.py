from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['http://localhost:9200'])

@app.route('/add', methods=['POST'])
def add_to_elasticsearch():
    try:
        data = request.get_json()
        index_name = f'{data.service_name}_status_index'

        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name)

        es.index(index=index_name, body=data)

        return jsonify({"message": f"{data.service_name} status added to Elasticsearch successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/healthcheck', methods=['GET'])
def retrieve_statuses():
    try:
        indexes = ['httpd_status_index','rabbitmq_status_index','postgresql_status_index']
        status_results = []
        for index in indexes:
            result = es.search(index=index, body={
                "query": {"match_all": {}},
                "sort": [{"@timestamp": {"order": "desc"}}],
                "size": 1
            })

            hits = result.get('hits', {}).get('hits', [])

            status = hits[0]['_source']
            status_results.append(status)

        return jsonify(status_results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/healthcheck/<service_name>', methods=['GET'])
def retrieve_service_status(service_name):
    try:
        services = ['httpd', 'rabbitmq', 'postgresql']
        if service_name in services:
            index_name = f"{service_name}_status_index"

            result = es.search(index=index_name, body={
                "query": {"match_all": {}},
                "sort": [{"@timestamp": {"order": "desc"}}],
                "size": 1
            })

            hits = result.get('hits', {}).get('hits', [])

            status = hits[0]['_source']

            return jsonify(status), 200
        else:
            return jsonify({"error": "service name invalid"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)