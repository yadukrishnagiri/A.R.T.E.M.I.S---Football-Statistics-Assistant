from flask import Flask, render_template, request, jsonify, send_from_directory
from query_data import query_rag  # Import your existing query_rag function

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()  # Get the JSON data from the request
    user_query = data.get('query')  # Extract the 'query' key from the JSON data

    if not user_query:
        return jsonify({"error": "No query provided"}), 400  # Return an error if no query is provided

    response = query_rag(user_query)
    return jsonify(response)  # Return the response as JSON


@app.route('/general_stats')
def general_stats():
    return render_template('general_stats.html')

@app.route('/club_stats')
def club_stats():
    return render_template('club_stats.html')

@app.route('/real_stats')
def real_stats():
    return render_template('real_stats.html')

@app.route('/man_u_stats')
def man_u_stats():
    return render_template('man_u_stats.html')

@app.route('/bayern_stats')
def bayern_stats():
    return render_template('bayern_stats.html')

@app.route('/ajax_stats')
def ajax_stats():
    return render_template('ajax_stats.html')

@app.route('/liverpool_stats')
def liverpool_stats():
    return render_template('liverpool_stats.html')

# Add error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)