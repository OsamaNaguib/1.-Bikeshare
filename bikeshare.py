import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = list(CITY_DATA.keys())
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city =input('Please write one of the following cities:\n Chicago \n New York City \n Washington \n').lower()
            if city in cities:
                break
            else:
                print("\n Invalid entry")
        except ValueError:
            print("\n Invalid entry")
        finally:
            print("\n You've entered {}".format(city))
                  
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('please write one of the following Months: \n {}\n'.format(months).lower())
            if month in months:
                break
            else:
                print("\n Invalid entry")
        except ValueError:
            print("\n Invalid entry")
        finally:
            print("\n You've entered {}".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('please write one of the following days: \n {}\n'.format(days).lower())
            if day in days:
                break
            else:
                print("\n Invalid entry")
        except ValueError:
            print("\n Invalid entry")
        finally:
            print("\n You've entered {}".format(day))
    print ("\n\nYou've enetered it all: \n {} - {} - {}".format(city, month , day)) 
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month & day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if not all months
    if month == "all" and day == "all":
        print (df)
    elif month.lower() == "all" and day.lower() != "all":
        df = df.loc[df['day_of_week'] == day.title()]
        print(df)
    elif month.lower() != "all" and day.lower() == "all":
        month = months.index(month)
        df = df.loc[df['month'] == month]
        print(df)
    elif month.lower() != "all" and day.lower() != "all":
        month = months.index(month)
        df = df.loc[(df['month'] == month) & (df['day_of_week'] == day.title())]
        print(df)
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('*' * 40 )
    print('\n The most common month: {} \n'.format(df['month'].mode()))

    # TO DO: display the most common day of week
    print('\n The most common dat of week: {} \n'.format(df['day_of_week'].mode()))

    # TO DO: display the most common start hour
    print('\n The most common start hour: {} \n'.format(df['hour'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df.head()

    # TO DO: display most commonly used start station
    print('\n The most commonly used start station: {} \n'.format(df['Start Station'].mode()))

    # TO DO: display most commonly used end station
    print('\n The most commonly used end station: {} \n'.format(df['End Station'].mode()))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + 'to' + df['End Station']
    print('\n The most frequent combination of start station and end station trip: {} \n'.format(df['start_end'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\n The total travel time: {} \n '.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\n The mean travel time: {} \n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n The counts of user types: \n{} \n'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    while True:
        try:
            print('\n The counts of gender: \n{} \n'.format(df['Gender'].value_counts()))
            break
        except Exception:
            print("There is no gender information in this city.")    
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            print('\n The earliest birth is: {} \n '.format(df.sort_values(by = 'Birth Year')['Birth Year'].head(1)))
            print('\n The most recent birth is: {} \n'.format(df.sort_values(by = 'Birth Year',ascending=False)['Birth Year'].head(1)))
            print('\n The most common year of birth is: {} \n'.format(df['Birth Year'].mode()))
            break
        except Exception:
            print("There is no Birth Years information in this city.")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    display_raw = input('\n Would you like to see the raw data? Enter yes or no.\n')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n')
                if display_raw != 'yes':
                    print('Thank You')
                    break #breaking out of the for loop
            break
        except KeyboardInterrupt:
            print('Thank you.')
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = list(CITY_DATA.keys())
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city =input('Please write one of the following cities:\n Chicago \n New York City \n Washington \n').lower()
            if city in cities:
                break
            else:
                print("\n Invalid entry")
        except ValueError:
            print("\n Invalid entry")
        finally:
            print("\n You've entered {}".format(city))
                  
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('please write one of the following Months: \n {}\n'.format(months).lower())
            if month in months:
                break
            else:
                print("\n Invalid entry")
        except ValueError:
            print("\n Invalid entry")
        finally:
            print("\n You've entered {}".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('please write one of the following days: \n {}\n'.format(days).lower())
            if day in days:
                break
            else:
                print("\n Invalid entry")
        except ValueError:
            print("\n Invalid entry")
        finally:
            print("\n You've entered {}".format(day))
    print ("\n\nYou've enetered it all: \n {} - {} - {}".format(city, month , day)) 
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month & day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if not all months
    if month == "all" and day == "all":
        print (df)
    elif month.lower() == "all" and day.lower() != "all":
        df = df.loc[df['day_of_week'] == day.title()]
        print(df)
    elif month.lower() != "all" and day.lower() == "all":
        month = months.index(month)
        df = df.loc[df['month'] == month]
        print(df)
    elif month.lower() != "all" and day.lower() != "all":
        month = months.index(month)
        df = df.loc[(df['month'] == month) & (df['day_of_week'] == day.title())]
        print(df)
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('*' * 40 )
    print('\n The most common month: {} \n'.format(df['month'].mode()))

    # TO DO: display the most common day of week
    print('\n The most common dat of week: {} \n'.format(df['day_of_week'].mode()))

    # TO DO: display the most common start hour
    print('\n The most common start hour: {} \n'.format(df['hour'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df.head()

    # TO DO: display most commonly used start station
    print('\n The most commonly used start station: {} \n'.format(df['Start Station'].mode()))

    # TO DO: display most commonly used end station
    print('\n The most commonly used end station: {} \n'.format(df['End Station'].mode()))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + 'to' + df['End Station']
    print('\n The most frequent combination of start station and end station trip: {} \n'.format(df['start_end'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\n The total travel time: {} \n '.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\n The mean travel time: {} \n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n The counts of user types: \n{} \n'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    while True:
        try:
            print('\n The counts of gender: \n{} \n'.format(df['Gender'].value_counts()))
            break
        except Exception:
            print("There is no gender information in this city.")    
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            print('\n The earliest birth is: {} \n '.format(df.sort_values(by = 'Birth Year')['Birth Year'].head(1)))
            print('\n The most recent birth is: {} \n'.format(df.sort_values(by = 'Birth Year',ascending=False)['Birth Year'].head(1)))
            print('\n The most common year of birth is: {} \n'.format(df['Birth Year'].mode()))
            break
        except Exception:
            print("There is no Birth Years information in this city.")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    display_raw = input('\n Would you like to see the raw data? Enter yes or no.\n')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n')
                if display_raw != 'yes':
                    print('Thank You')
                    break #breaking out of the for loop
            break
        except KeyboardInterrupt:
            print('Thank you.')
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()