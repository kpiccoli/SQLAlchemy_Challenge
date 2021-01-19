## SQLAlchemy - CLIMATE ANALYSIS

![surfs-up.png](Images/surfs-up.png)

### Purpose
Using Python and SQLAlchemy ORM queries, Pandas, and Matplotlib, analyze data from Hawaii weather stations between 01/01/2010 to 08/23/2017, to provide climate analysis and data exploration.
The purpose of this study is to choose the better time of the year for a trip vacation to Hawaii.
<<<<<<< HEAD


### Tools
- Python
- SQLAlchemy
- Matplotlib
- Flask API

=======
>>>>>>> 74f104bd004cd85abcb0c57e7c4f6f25395ed113

### Dataset
- hawaii_measurement.csv
- hawaii_stations.csv


### Description
1. Precipitation Analysis - design a query to retrieve the last 12 months of precipitation data and plot it using the data frame. 
![precipitation](Images/precipitation.png)
2. Station Analysis - design a query to calculate the total number of stations and most active stations. Retrieve the last 12 months of temperature observation data (TOBS) and the highest number of observations. Plot the results as a histogram with `bins=12`.
![station-histogram](Images/station-histogram.png)
3. Temperature Analysis - identify the average temperature for the time of the trip and daily normals. 

![temperature](Images/temperature.png)

![daily-normals](Images/daily-normals.png)


### Climate App
Design a Flask API based on the queries developed.

#### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


