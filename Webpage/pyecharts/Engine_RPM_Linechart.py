from pyecharts.charts import Line, Bar, Tab
import pandas as pd
from pyecharts import options as opts

df = pd.read_csv('./User2_Dataset.csv',  index_col = [1], parse_dates = ['Date'])
average_speed = df['Average_speed']
distance_travelled = df['Distance_travelled']
fuel_used = df['Fuel_used']
vehicle_speed = df['Vehicle_speed']
engine_rpm = df['Engine_RPM']

x_date = ['2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', 
        '2021-05', '2021-06','2021-07', '2021-08', '2021-09' ]

def linechart()->Line:
    line = (
        Line()
        .add_xaxis(x_date)
        .add_yaxis("Average speed", average_speed)
        .add_yaxis("Distance_travelled", distance_travelled)
        .add_yaxis("Fuel Used", fuel_used)
        .add_yaxis("Vehicle Speed", vehicle_speed)

        )
    return line

def barchart():
    c = (
        Bar()
        .add_xaxis(x_date)
        .add_yaxis("Engine_RPM", list(engine_rpm))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Engine RPM per month"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c

tab = Tab()
tab.add(linechart(), "Linechart")
tab.add(barchart(), "Barchart")
tab.render("data_analysis.html")