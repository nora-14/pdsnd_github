import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

#list that links month numbers to names

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Which US city would you like to see data for: Chicago, Washington, or New York?\n").lower()
        except:
            print("Invalid input. Try again.\n")
            #for any error
        if city not in CITY_DATA:
            print("Try again. The only valid city options are: Chicago, Washington, or New York.\n")
            #if user inputs string that doesn't match cities
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Which month? Specify a month between January to June or type 'all' to select all of these months.\n").title()
        except:
            print("Error. Please try again.\n")
            #for any error
        if month not in month_list:
            print("Invalid input. Please try again.\n")
            #if user inputs invalid options
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day = input("Which day? Choose one specific day (Monday, Tuesday, etc.) or type 'all' if you want to see results for all days.\n").title()
            day_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
        except:
            print("Invalid input. Please try again.\n")
            #for any error
        if day not in day_of_week:
            print("Invalid string. Please try again.\n")
            #if user inputs string that doesn't match days of week
        else:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        #filter by month to create the new dataframe
        df = df[df['month'] == (month_list.index(month) + 1)]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = month_list[df['month'].mode()[0] - 1]
    print("The most common month is:", common_month)

    # TO DO: display the most common day of week
    print("The most common day of the week is:", df['day_of_week'].mode()[0])

    # TO DO: display the most common start
    print("The most common start hour is:", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station is:", (df['Start Station'] + " and " + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is:", df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("The mean travel time is:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts by user type are:\n", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print("\nThe counts by gender are:\n", df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nThe earliest year of birth is:", df['Birth Year'].min())
    print("The most recent year of birth is:", df['Birth Year'].max())
    print("The most common year of birth is:", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Offer option to user for viewing raw data."""
    row_start = 0
    row_end = 5
    answer = input("\nDo you want to see a snippet of the raw data? Yes or No?\n").lower()
    while answer == "yes" and row_end <= len(df.index):
        print(df.iloc[row_start:row_end])
        row_start += 5
        row_end += 5
        answer = input("Do you want to see more data? Yes or No?\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if 'Gender' and 'Birth Year' in df:
            user_stats(df)
        else:
            print('Gender and Birth Year stats cannot be calculated because these columns do not appear in the dataframe')

        raw_data(df)
        """User can exit the raw data preview and restart if they do not answer yes."""
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
