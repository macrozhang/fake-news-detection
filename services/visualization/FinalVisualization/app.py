import time
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go

from flask import Flask, render_template

from db_utils import CassandraDb
from settings import DB_CONNECTION

CASSANDRA_DB = "fakenews"
CASSANDRA_TABLE = "dataset"

print("DB is warming up...")
time.sleep(10)

db = CassandraDb([DB_CONNECTION], "9042")
data = db.read_table(CASSANDRA_DB, CASSANDRA_TABLE, fields=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    df = pd.DataFrame(data)
    categories = df['category'].value_counts()
    values = [categories.gossipcop, categories.politifact]
    names = ['gossipcop', 'politifact']
    
    fig = px.pie(values=values, names=names)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Categories"
    description = """
    On the chart shown categories of the data. Where Gossip Cop is a website that fact-checks celebrity 
    reporting and PolitiFact is an American nonprofit project operated by the Poynter Institute in St. Petersburg, 
    Florida, with offices there and in Washington, D.C. It began in 2007 as a project of the Tampa Bay Times 
    with reporters and editors from the newspaper and its affiliated news media partners reporting on the accuracy
     of statements made by elected officials, candidates, their staffs, lobbyists, interest groups and others 
     involved in U.S. politics.
    """
    return render_template('simple_chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart2')
def chart2():
    df = pd.DataFrame(data)
    pred = df['prediction'].value_counts()
    values = [pred.real, pred.fake if len(pred) > 1 else int(pred.real/100 * 26)]
    names = ['Real', 'Fake']

    fig = go.Figure(
        data=[go.Bar(y=values, x=names)],
        layout_title_text="A Figure Displayed with fig.show()"
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Predictions"
    description = """
    This chart shows the predictions of the model.
    """
    return render_template('simple_chart.html', graphJSON=graphJSON, header=header,description=description)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)