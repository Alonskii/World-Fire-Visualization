# World-Fire-Visualization

This is a python script that shows the one day global fire map visualization and it is intended to show the pictoral representation of regions that experienced a lot and less of wildfire within a 24 hour period.

It uses the plotly's Library for the visualization, and then we import the Scattergeo and Layout class to get the real time visualization at it occurs around the globe. 
The data was retrieved from #https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. You can actually find links to the data in CSV format in the TXT section, and also more recent data can be downloaded from the webpage. 

The project contains vital information about burning fire in different locations around the world, including the longitude and latitude, as well as the brightness of each fire.. 
The PNG file below shows the exact same result you'll get when you run the python file. 

Please note that there are over 27,000 rows listed in the CSV file. Handling the entire data set was difficult for my system, and as such I had to add a block to stop the process and deal with only 10,000 rows..
