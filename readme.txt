# Bikeshare Project:
_Udacity project using pandas library in Python; practicing data exploration._

# Project Overview:

The project focuses on data exploration for three major U.S. cities - Chicago, Washington, and New York City - using pandas and munpy on python to do the task.

### Program Details:

The project asks the user to input the "city" (e.g. Whashington), "month" for which he/she wants to view data (e.g. January; also includes an 'all' option; which implies no filter is requried), and the "day" for which he/she wants to view data (e.g. Monday; also includes an 'all' option, which implies no filter is requried).

User inputs are handled for exceptions, and forms the base for loading and filteration of data, then performing some statistics; as per the provided filters, such as:

* Most popular month
* Most popular day
* Most popular hour
* Most popular start station
* Most popular end station
* Most popular combination of start and end stations
* Total trip duration
* Average trip duration
* Types of users by number
* Types of users by gender (if applicable)
* The oldest user (if applicable)
* The youngest user (if applicable)
* The most common birth year amongst users (if applicable)

Finally, the user is asked to enter "yes", if he/she wishes to restart the prgram, and "no" for ending the program.

# Requirements:

* Language: Python 3.6 or above
* Libraries: pandas, numpy, time

# Project Data:
contained in the data folder as follows:
* chicago.csv
* new_york_city.csv
* washington.csv

# Used Functions:
1. get_filters : which received the user inputs and form the filters for the data.
2. load_data : specifies which part of the data is loaded, based on the user inputs for the city, month and day.
3. time_stats : do some statistics part regarding most frequent month, day, and hour
4. station_stats : do some statistics part regarding most frequent start, end and combination stations.
5. trip_duration_stats : do some statistics part regarding total and average travelling time
6. user_stats : do some statistics part regarding user types and gender& Birth Year (if applicable).
7. display_raw : offers user to show chunks of raw data.
8. main : integrate the previous functions.


Osama Naguib
