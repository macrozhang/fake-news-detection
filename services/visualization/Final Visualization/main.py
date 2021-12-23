from flask import Flask, render_template
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
from flask_apscheduler import APScheduler

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))
app = Flask(__name__, static_url_path='')
app.jinja_env.variable_start_string = '{{ '
app.jinja_env.variable_end_string = ' }}'

CASSANDRA_USER = "cassandra"
CASSANDRA_PASS = "cassandra"
CASSANDRA_HOST = "192.168.20.30"
CASSANDRA_PORT = "9042"
CASSANDRA_DB = "fakenews"
CASSANDRA_TABLE = "combinedData"


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'main:job1',
            'trigger': 'interval',
            'seconds': 600
        }
    ]
    SCHEDULER_API_ENABLED = True


def getData():
    auth_provider = PlainTextAuthProvider(username=CASSANDRA_USER, password=CASSANDRA_PASS)
    cluster = Cluster(contact_points=[CASSANDRA_HOST], port=CASSANDRA_PORT,
                      auth_provider=auth_provider)
    session = cluster.connect(CASSANDRA_DB)
    session.row_factory = dict_factory
    sql_query = "SELECT index_id, id, news_url, title, tweet_ids, y, category FROM {}.{};".format(CASSANDRA_DB,
                                                                                                  CASSANDRA_TABLE)
    df = pd.DataFrame()
    for row in session.execute(sql_query):
        df = df.append(pd.DataFrame(row, index=[0]))
    newdf = df.groupby(['category', 'y']).count()
    newdf = newdf.reset_index()
    newdf["key"] = newdf["category"] + ',' + newdf["y"]

    return newdf


def getBar():
    index_id = [int(i) for i in list(data["index_id"].values)]
    id = [int(i) for i in list(data["id"].values)]
    news_url = [int(i) for i in list(data["news_url"].values)]
    title = [int(i) for i in list(data["title"].values)]
    tweet_ids = [int(i) for i in list(data["tweet_ids"].values)]
    key = list(data["key"].values)
    bar = (
        Bar(
            init_opts=opts.InitOpts(
                width='100%',
                animation_opts=opts.AnimationOpts(
                    animation_delay=1000, animation_easing="bounceIn"
                )
            )
        )
            .add_xaxis(key)
            .add_yaxis("index", index_id)
            .add_yaxis("id", id)
            .add_yaxis("news_url", news_url)
            .add_yaxis("title", title)
            .add_yaxis("tweet_ids", tweet_ids)
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""))
    )

    data1 = data.groupby(["y"])["index_id"].sum().reset_index()

    x_data = list(data1["y"].values)
    y_data = [int(i) for i in list(data1["index_id"].values)]
    pie = (
        Pie(  init_opts=opts.InitOpts(
                width='100%',
                animation_opts=opts.AnimationOpts(
                    animation_delay=1000, animation_easing="bounceIn"
                )
            ))
            .add("", [list(z) for z in zip(x_data, y_data)])
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    return bar, pie


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    c1,c2 = getBar()
    return render_template('index.html',
                           count_c1_graph=Markup(c1.render_embed()),
                           count_c2_graph=Markup(c2.render_embed()),
                           )


data = getData()


def job1():
    global data
    data = getData()


app.config.from_object(Config())
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
