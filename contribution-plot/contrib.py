import calmap
import datetime
import todoist
api = todoist.TodoistAPI('PUT API TOKEN HERE')

import pandas as pd

import matplotlib.pyplot as plt


start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2021, 12, 22) # today
delta = datetime.timedelta(days=1)

response_data = dict()
response_data['date_time'] = []
response_data['count'] = []

while start_date <= end_date:
    start_string = str(start_date)+"T08:00" # 8 is PST, 5 is EST, 4 is EDT, 7 is PDT
    
    start_date += delta
    end_string = str(start_date)+"T08:00"

    data = api.completed.get_all(since=start_string, until=end_string)

    tmp = datetime.datetime(start_date.year, start_date.month, start_date.day)


    count = len(data['items'])
    if count > 0:
        response_data['date_time'].append(tmp)
        response_data['count'].append(count)

data = pd.DataFrame(response_data)

#Setting the date_time column as the index
data = (data.reset_index().set_index('date_time').resample('1D').mean())

# following code is from
# https://towardsdatascience.com/create-githubs-style-contributions-plot-for-your-time-series-data-79df84ec93da

#plotting the calender heatmap for the year
plt.figure(figsize=(20,10))
calmap.yearplot(data['count'], 
                cmap='YlGn', 
                fillcolor='lightgrey',
                daylabels='MTWTFSS',
                dayticks=[0, 2, 4, 6],
                linewidth=2)
plt.show()