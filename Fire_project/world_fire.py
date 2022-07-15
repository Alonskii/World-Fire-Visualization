import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

number_rows = 10_000

filename = 'fire_data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Print the index position of the data information
    #print(header_row)
    date_index = header_row.index("acq_date")
    lat_index = header_row.index("latitude")
    lon_index = header_row.index("longitude")
    bright_index = header_row.index("brightness")

    # Get the required fire data from the file.
    dates, lats, lons, brightness, hover_texts = [], [], [], [], []
    row_number = 0

    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        bright = float(row[bright_index])
        lab = f"{date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(date)
        lats.append(row[lat_index])
        lons.append(row[lon_index])
        brightness.append(bright)
        hover_texts.append(lab)

        row_number = row_number + 1
        if row_number == number_rows:
            break

# Map the fires..
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [bright/20 for bright in brightness],
        'color': brightness,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='1-Day World Fire Representation')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='fire_map.html')
