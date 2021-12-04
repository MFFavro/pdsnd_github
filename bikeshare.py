import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - the month to filter by, or "all" for no month filter
        (str) day - the day of week to filter by, or "all" for no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Please select a city: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Please select a city: ").lower()

    months = ['all', 'january', 'february', 'march', 'april',
              'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
    month = input("Please enter month: ").lower()
    while month not in months:
        month = input("Please enter month: ").lower()

    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday']
    day = input('Please enter day of week: ').lower()
    while day not in days:
        day = input('Please enter day of week: ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the the city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - the month to filter by, or "all" for no month filter
        (str) day - the day of week to filter by, or "all" for no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['all', 'january', 'february', 'march', 'april',
                  'may', 'june', 'july', 'august', 'september',
                  'october', 'november', 'december']
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print("The most common month is ", common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print("The most common day is ", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is ", df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is ", df['Start Station'].mode())

    print("The most common end station is ", df['End Station'].mode())

    most_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most common trip is ", most_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum() / 3600
    print('Total time traveled ', total_trip_time)

    # TO DO: display mean travel time
    mean_trip_time = df['Trip Duration'].mean() / 3600
    print('Average time traveled ', mean_trip_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except KeyError:
        print("No gender data")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        oldest = int(df['Birth Year'].min())
        print("The earliest birth year is ", oldest)
    except KeyError:
        print("No birth year data")
    try:
        youngest = int(df['Birth Year'].max())
        print("The most recent birth year is ", youngest)
    except KeyError:
        print("No birth year data")
    try:
        most_common = int(df['Birth Year'].mode())
        print("The most common birth year is ", most_common)
    except KeyError:
        print("No birth year data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    extra_data = input('\nWould you like to see more data? Enter yes or no.\n')
    row = 1
    while extra_data == 'yes':
        print(df[row:row+5])
        row += 5
        extra_data = input('\nWould you like to see more data? Enter yes or no.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
