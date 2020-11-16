import time
import pandas as pd
import numpy as np
import datetime
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nEnter the name of the desired city (chicago, new york city, or washington):')
    city = input().lower()
    while city not in CITY_DATA:
        print('\nOops, something went wrong. Please try again (chicago, new york city, or washington):')
        city = input()

    # get user input for month (all, january, february, ... , june)
    print('\nEnter the name of the desired month (form January to June) or all.')
    month = input().lower()
    while month not in months and month != 'all':
        print('\nOops, something went wrong. Please try again:')
        month = input().lower()
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nEnter the name of the desired day of the week, or all:')
    day = input().lower()
    while day not in days and day != 'all':
        print('\nOops, something went wrong. Please try again:')
        day = input().lower()

    #prompt to choose what stats to look at.
    print('''
What statistics would you like to know more about (enter the number of the desired option or all)?
        1. time stats     2 station stats
        3. trip stats     4. user stats''')
    categ = str(input())
    while categ not in ['1', '2', '3', '4', 'all']:
        print('\nOops, something went wrong. Please try again:')
        categ = str(input())

    print('-'*40)
    return city, month, day, categ


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# display the most common month
    # creates a new dictionary ordered my most reaccuring (common) month in start time
    mcm = df['Start Time'].dt.month.value_counts()
    # mcm_key becomes the first item in mcm which is the most common month
    mcm_key = mcm.index[0]
    # mcm_value is the count of mcm_key
    mcm_value = mcm.loc[mcm_key]
    # converts the month number into the name using the month list at the top of the page
    print('The most common month to travel is {} with {} uses.'.format(months[(mcm_key-1)].title(), mcm_value))

# display the most common day of week
    mcd = df['Start Time'].dt.weekday.value_counts()
    mcd_key = mcd.index[0]
    mcd_value = mcd.loc[mcd_key]
    print('The most common day of the week is {} with {} uses.'.format(days[(mcd_key-1)].title(), mcd_value))

# display the most common start hour
    mch = df['Start Time'].dt.hour.value_counts()
    mch_key = mch.index[0]
    mch_value = mch.loc[mch_key]
    print('The most common hour of travel is {} with {} uses.'.format(mch_key, mch_value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mcss = df['Start Station'].value_counts()
    mcss_key = mcss.index[0]
    mcss_value = mcss.loc[mcss_key]
    print('Most commonly used starting station: {}\nWas used {} times.'.format(mcss_key, mcss_value))


    # display most commonly used end station
    mces = df['End Station'].value_counts()
    mces_key = mces.index[0]
    mces_value = mces.loc[mces_key]
    print('Most commonly used ending station: {}\nWas used {} times.'.format(mces_key, mces_value))

    # display most frequent combination of start station and end station trip
    start_st = df['Start Station']
    end_st = df['End Station']

    #start_end = np.add(start_st, end_st)

    df['trip_path'] = start_st + ' to ' + end_st

    pop_st = df['trip_path'].value_counts()
    pop_st_key = pop_st.index[0]
    pop_st_value = pop_st.loc[pop_st_key]
    print('The most common trip: {} \nwas completed {} times.'.format(pop_st_key, pop_st_value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

<<<<<<< HEAD
# display total travel time
    # converts 'Trip Duration' column to numpy and finds the sum of trip durations 
    total_travel = np.sum(df['Trip Duration'].to_numpy())
    # converts the seconds of travel into months, days, hours, seconds
    travel_time_mod = datetime.timedelta(seconds= int(total_travel))
    # prints the travel time
    print('The total traviel time:\n', travel_time_mod)


<<<<<<< HEAD
# display mean travel time
    # converts Trip Duration column to numpy 
    numpy_time = df['Trip Duration'].to_numpy()
    # finds the mean trip duration
    mean_time = np.mean(numpy_time)
    # converts the seconds of travel into months, days, hours, seconds. Then prints the result
    print('The mean travel time:', datetime.timedelta(seconds= int(mean_time)))

# finds difference between the start time and current time to determine total work time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    ut = df['User Type'].value_counts()
    ut_list = ut.to_frame()
    print('\nUser types and counts:\n')
    print(ut_list)


    # Display counts of gender
    try:
        gt = df['Gender'].value_counts().to_frame()
        print('\nGender counts:\n')
        print(gt)


        # Display earliest, most recent, and most common year of birth

        eby = df['Birth Year'].min()
        print('\nThe earliest year of birth:\n', int(eby))

        mrby = df['Birth Year'].max()
        print('\nThe most recent year of birth:\n', int(mrby))
       
        mcby = df['Birth Year'].value_counts()
        mcby_key = mcby.index[0]
        mcby_value = mcby.loc[mcby_key]
        print('\nThe most common birth year:\n{} occurred {} times.'.format(int(mcby_key), mcby_value))
    except KeyError as syner:
        print('\nSorry, Washington does not have age and gender data.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day, categ = get_filters()
        df = load_data(city, month, day)

        if categ == '1':
            time_stats(df)
        elif categ == '2':
            station_stats(df)
        elif categ == '3':
            trip_duration_stats(df)
        elif categ == '4':
            user_stats(df)
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
