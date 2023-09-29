from flask import Flask, request
from ElasticSearchLogger.main.log.logES import LogAPI
app = Flask(__name__)

app.add_url_rule('/log', view_func=LogAPI.post)

if __name__ == '__main__':
    app.run(debug=True)
