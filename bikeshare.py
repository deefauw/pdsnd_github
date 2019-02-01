import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Choose a city between Chicago, New York City and Washington: ').lower()

    while city not in ['chicago', 'new york city', 'washington']:
        print('That is not a valid city. Please try again.')
        city = input('Choose a city between Chicago, New York City and Washington: ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Choose a month between January and June. If you would like to see all months, please enter all: ').lower()

    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('That is not a valid month. Please try again.')
        month = input('Choose a month between January and June. If you would like to see all months, please enter all: ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Choose a day of the week. If you would like the full week, please enter all: ').lower()

    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('That is not a valid day. Please try again.')
        day = input('Choose a day of the week. If you would like the full week, please enter all: ').lower()


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
    # this was taken from Practice Solution 3 - I don't believe this is plagiarism because in Udacity's definition of plagiarism, it states "Copying code or using code that has been provided for you and approved for use in your project by Udacity without attribution" is not plagiarism. Please let me know if I am mistaken.
    try:
        df = pd.read_csv(CITY_DATA[city])
    except Exception as e:
        print(e)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month is {}'.format(popular_month))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day: ', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common starting station was: ', common_start)


    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station was: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    # got help from Udacity mentor on this problem
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    most_frequent_trip = df['trip'].mode()[0]
    print('The most common combination of start station and end station trip was: ', most_frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time was {} seconds.'.format(total_travel))


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time was {} seconds.'.format(mean_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # used Udacity Student Hub to get started
    user_type = df['User Type'].value_counts()
    print(user_type)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_type = df['Gender'].value_counts()
        print(gender_type)
    else:
        print('No gender data for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    # used Udacity Student Hub for support
    if 'Birth Year' in df:
        earliest_yob = df['Birth Year'].min()
        print('The earliest year of birth is: ', earliest_yob)
    else:
        print('No birth year data for this city.')

    if 'Birth Year' in df:
        most_recent_yob = df['Birth Year'].max()
        print('The most recent year of birth is: ', most_recent_yob)
    else:
        print('No birth year data for this city.')

    if 'Birth Year' in df:
        most_common_yob = df['Birth Year'].mode()
        print('The most common year of birth is: ', most_common_yob)
    else:
        print('No birth year data for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays five consecutive rows of data."""
    # got help from Udacity mentor in writing this code

    line_number = 0

    all_data = input('\nWould you like to see the raw data? Please enter yes or no.\n')

    while all_data not in ['yes', 'no']:
        print('Please enter yes or no')
        all_data = input('\nWould you like to see the raw data? Please enter yes or no.\n')

    if all_data == 'no':
        return
    elif all_data == 'yes':
        print(df.iloc[line_number])

    keep_going = input('\nDo you want to see more data? Enter yes or no.\n').lower()

    if keep_going == 'no':
        return
    while keep_going == 'yes':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            keep_going = input('\nDo you want to see more data? Enter yes or no.\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
