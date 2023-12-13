# SQL from queries_dict
from visuals import bar_chart
from queries_dict import queries_dict
class Query:
    def __init__(self, sql, title, xlabel, ylabel, xdata=None, ydata=None):
        self.sql = sql
        self.xdata = xdata
        self.ydata = ydata
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

class QueryBar(Query):
    def __init__(self, sql, title, xlabel, ylabel, xdata=None, ydata=None):
        super().__init__(sql, title, xlabel, ylabel, xdata, ydata)
    def produce_chart(self):
        bar_chart(x= self.xdata, y=self.ydata, labelx= self.xlabel, labely= self.ylabel, title=self.title)
class QueryScatter(Query):
    def __init__(self, sql, title, xlabel, ylabel, xdata, ydata):
        super().__init__(sql, title, xlabel, ylabel, xdata, ydata)
        
    def produce_chart():
        pass
