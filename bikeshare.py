import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ("all", "january", "february", "march", "april", "may", "june")
DAYS = ("all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    print('\n' + '-'*40 + '\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Name of the city you want to analyze: ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('--> Please choose {}, {} or {}'.format(*CITY_DATA.keys()))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Month you want to analyze, or type \"all\": ').lower()
        if month in MONTHS:
            break
        else:
            print('--> Please choose {}, {}, {}, {}, {}, {} or {}'.format(*MONTHS))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Day you want to analyze, or type \"all\": ').lower()
        if day in DAYS:
            break
        else:
            print('--> Please choose {}, {}, {}, {}, {}, {}, {} or {}'.format(*DAYS))

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
    df = pd.read_csv(CITY_DATA[city])

    # add day and month columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # month filter, ignored if "all" selected
    if month != 'all':
        df = df[df['month'] == MONTHS.index(month)]

    # day filter, ignored if "all" selected
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}.'.format(MONTHS[most_common_month].title()))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is {}.'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is {}.'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    trip = df['Start Station'].astype(str) + ' to ' + df['End Station'].astype(str)
    most_common_trip = trip.mode()[0]
    print("The most frequent combination of start station and end station trip is {}".format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total traval time is {} seconds".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean traval time is {} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_dict()
    for user_type in user_types:
        print('There is/are {} counts of the user type {}'.format(user_types[user_type], user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts().to_dict()
        for gender_type in gender_types:
            print('There is/are {} counts of {} user(s)'.format(gender_types[gender_type], gender_type))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        oldest_by = int(df['Birth Year'].min())
        youngest_by = int(df['Birth Year'].max())
        most_common_by = int(df['Birth Year'].mode()[0])
        print("The oldest user was born in {}.\nThe youngest user was born in in {}.\nThe most common year of birth among users is {}.".format(oldest_by, youngest_by, most_common_by))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40 + '\n')

def rawdata(df):
    """Shows raw data on request."""

    start = 0
    end = 5

    request_raw = input('Do you want to see the raw data? Enter yes or no.\n').lower()
    if request_raw == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end,:])
            start += 5
            end += 5

            continue_raw = input('Do you want to see more raw data? Enter yes or no.\n').lower()
            if continue_raw == 'no':
                print('-'*40)
                break

def main():
    print('-'*40 + '\n')
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('-'*40)
            break


if __name__ == "__main__":
	main()
