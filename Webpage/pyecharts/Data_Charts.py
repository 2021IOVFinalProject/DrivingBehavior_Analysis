from datetime import date
from pyecharts.charts import Line, Bar, Scatter, Boxplot, Pie, Tab
from pyecharts import options as opts 
import pandas as pd

df = pd.read_csv('./new_data.csv')
average_speed = df['Average_Vehiclespeed(km/h)']
distance_travelled = df['Distance_travelled(km)']
fuel_used = df['Fuel_used(L)']
engine_rpm = df['Average_EngineRPM(rpm)']

x_date = ['2020-10','2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', 
        '2021-05', '2021-06','2021-07', '2021-08', '2021-09']

line = (
        Line(init_opts = opts.InitOpts(width='1200px',height='700px'))
        .add_xaxis(x_date)
        .add_yaxis("Average speed", average_speed)
        .add_yaxis("Distance travelled", distance_travelled)
        .add_yaxis("Fuel Used", fuel_used)
)

bar = (
    Bar(init_opts = opts.InitOpts(width='1200px',height='700px'))
    .add_xaxis(x_date)
    .add_yaxis("Engine_RPM", list(engine_rpm))
    .add_yaxis("Distance travelled", list(distance_travelled))
    .add_yaxis("Average speed", list(average_speed))
    .add_yaxis("Fuel Used", list(fuel_used))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Driver data per month"),
        datazoom_opts=[opts.DataZoomOpts()],
        )
)

df2 = pd.read_csv('./DrivingBehavior_Dataset.csv', parse_dates= True)
num = df2['num']
average_speed2 = df2['Average_Vehiclespeed(km/h)']
distance_travelled2 = df2['Distance_travelled(km)']
fuel_used2 = df2['Fuel_used(L)']
engine_rpm2 = df2['Average_EngineRPM(rpm)']
driver_risk2 = df2['Driver_Risk']

scatter = (
    Scatter(init_opts = opts.InitOpts(width='1200px',height='700px'))
    .add_xaxis(num)
    .add_yaxis("Average speed", average_speed2)
        .add_yaxis("Distance travelled", distance_travelled2)
        .add_yaxis("Average EngineRPM", engine_rpm2)
        .add_yaxis("Fuel Used", fuel_used2)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Driver data per month"),
            xaxis_opts=opts.AxisOpts(
                name='Data amounts',
                name_location='middle',
            ),
            datazoom_opts=[opts.DataZoomOpts()],
        )
)

box = Boxplot(init_opts = opts.InitOpts(width='1200px',height='700px'))
x_cate = ['Distance travel', 'Average engineRPM', 'Fuel used', 'Average speed']

box_distance = [[228.08, 351.13, 275.11, 158.44, 246, 260.38, 318.98, 258.21, 292.85, 290.18, 250.87]]

box_rpm = [[81.93, 85.88, 88.95, 74.51, 61.93, 72.55, 74.85, 88.86, 71.36, 74.78, 75.7, 68.95]]

box_fuel = [[92.6, 138.34, 106.9, 99.82, 58.94, 90.94, 91.48, 115.52, 103.27, 100.88, 107.06, 92.69]]

box_speed = [[35.64, 44.4, 44.39, 33.43, 26.21, 34.32, 39.04, 49.14, 35.42, 39.31, 37.6, 29.53]]

box.add_xaxis([])

box.add_yaxis("Distance travel", box.prepare_data(box_distance))
box.add_yaxis("Average engineRPM", box.prepare_data(box_rpm))
box.add_yaxis("Fuel used", box.prepare_data(box_fuel))
box.add_yaxis("Average speed", box.prepare_data(box_speed))
box.set_global_opts(
            title_opts=opts.TitleOpts(title="Driver data per month"),
            #datazoom_opts=[opts.DataZoomOpts()],
        )

x_axis = ['2020/10', '2020/11', '2020/12', '2021/01', '2021/02', '2021/03', '2021/04', '2021/05', '2021/06', '2021/07', '2021/08', '2021/09']

y_zero = [20, 11, 13, 20, 20, 17, 14, 11, 17, 17, 18, 22]
y_one = [2, 3, 3, 5, 1, 4, 3, 2, 2, 2, 3, 4]
y_two = [1, 8, 5, 3, 4, 3, 3, 1, 5, 5, 1, 1]
y_three = [8, 8, 10, 3, 3, 7, 10, 17, 6, 7, 9, 3]


stackedbar = (
    Bar(init_opts = opts.InitOpts(width='1200px',height='700px'))
    .add_xaxis(x_axis)
    .add_yaxis("0", list(y_zero), stack="stack1")
    .add_yaxis("1", list(y_one), stack="stack1")
    .add_yaxis("2", list(y_two), stack="stack1")
    .add_yaxis("3", list(y_three), stack="stack1")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Driver Risk Stacked Bar Chart")

        )
)

print(driver_risk2.value_counts()) 

data = [('3', 91), ('2', 40), ('1', 34), ('0', 200)]

pie = Pie(init_opts = opts.InitOpts(width='1200px',height='700px'))
pie.add(
        series_name='Driver Risk',
        data_pair=data,
        radius=['30%', '70%'],
        rosetype='radius'
)

pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}：{d}%'))
pie.set_global_opts(title_opts=opts.TitleOpts(title='Driver Risk'))

tab = Tab()
tab.add(line, "Line chart")
tab.add(bar, "Bar chart")
tab.add(scatter, "Scatter plot")
tab.add(box, "Boxplot")
tab.add(stackedbar, "Stacked Bar chart")
tab.add(pie, "Pie chart")
tab.render("data_analysis.html")
