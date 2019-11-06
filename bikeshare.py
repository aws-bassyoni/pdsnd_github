import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("""\nChoose which city you would like to explore its bikeshare data? 
            Newyork, Chicago or Washington!\n""").lower()
            
            #Check input validity
            if city.replace(' ','').isalpha():
                if (city.replace(' ','') in CITY_DATA):
                    break
                else:
                    print('\nInvalid input, check spelling or city name \n')
                    continue
            else:
                print('\nInvalid input, please enter city name \n')
                continue
        except (ValueError, KeyboardInterrupt) as e:
            print('\nError encountered : {} \n'.format(e))
            print('\nInvalid Input, try again!! \n')
            continue
            
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        try:
            print('\nWhich month you want to explore;')
            month = input('Choose months from January to June, enter "all" to include all data \n').lower()
            
            #Check input validity
            if month.isalpha():
                if (month in months) or (month == 'all'):
                    break
            else:
                print('\nInvalid input, please try again\n')
                continue
        except (ValueError, KeyboardInterrupt) as e:
            print('\nError encountered : {} \n'.format(e))
            print('\nInvalid Input, try again!! \n')
            continue
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nWhich day of the week you wish to explore; Enter as Monday, Tuesday..etc, enter "all" to  include all\n').lower()
            
            #Check input validity
            if day.isalpha():
                if (day in days) or (day == 'all'):
                    break
            else:
                print('\nInvalid input, please try again\n')
                continue
        except (ValueError, KeyboardInterrupt) as e:
            print('Error encountered : {} \n'.format(e))
            print('Invalid Input, try again!! \n')
            continue


    print('-'*60)
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
    #The code here was similar to the practice Qs,
    #Some were adapted from the practice Qs code.
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
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

    # TO DO: display the most common month
    
    # find the most common month (Jan to June)
    popular_month = df['month'].mode()[0]
    
    # find count of popular month
    month_count = df['month'].value_counts()[popular_month]
    
    print('\nMost Frequent Month:\n', months[popular_month-1].title(), '\n Count: ', month_count)


    # TO DO: display the most common day of week
    
    # find the most common day_of_week
    
    popular_day_of_week = df['day_of_week'].mode()[0]
    
    # find popular day of the week count
    popular_day_of_week_count = df['day_of_week'].value_counts()[popular_day_of_week]
    
    print('\nMost Frequent Day:\n', popular_day_of_week, '\n Count: ', popular_day_of_week_count)
    
    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    
    # find count of popular hour
    popular_hour_count = df['hour'].value_counts()[popular_hour]
    
    print('\nMost Frequent Start Hour:\n', popular_hour, '\n Count: ', popular_hour_count)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['Most Common Start Station'] = df['Start Station']
    
    # find most common Start Station
    popular_start_station = df['Most Common Start Station'].mode()[0]
    
    # find most common Start Station count
    popular_start_station_count = df['Most Common Start Station'].value_counts()[popular_start_station]
    
    print('\nMost Frequent Start Station: \n', popular_start_station, '\n Count: ', popular_start_station_count)
    
    # TO DO: display most commonly used end station
    
    df['Most Common End Station'] = df['End Station']
    
    # find most common End Station
    popular_end_station = df['Most Common End Station'].mode()[0]
    
    # find most common End Station count
    popular_end_station_count = df['Most Common End Station'].value_counts()[popular_end_station]
    
    print('\nMost Frequent End Station: \n', popular_end_station, '\n Count: ', popular_end_station_count)

    # TO DO: display most frequent combination of start station and end station trip
    
    # Create a new "Route Combination" coulmn to merge Start & End to ease counting
    df['Route Combination'] = df['Start Station'] + '   -AND-   ' + df['End Station']
    
    # find most common combination of Routes
    popular_trip = df['Route Combination'].mode()[0]
    
    # count the iteration of the popular route
    popular_trip_count = df['Route Combination'].value_counts()[popular_trip]
    
    print('\nMost Frequent Trip/Route: \n', popular_trip, '\n Count: ', popular_trip_count)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    #Sum the trip duration column
    total_travel_time = df['Trip Duration'].sum()
    
    #print total travel time
    print(str(total_travel_time) + ' seconds')
    
    #find travel time in hh:mm:ss
    #Algorthim was adopted from here:
    #https://www.w3resource.com/python-exercises/python-basic-exercise-65.php
  
    if total_travel_time >= 86400:
        total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time%86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time%86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time%86400)%3600)% 60)) +
                         's')
    else:
        total_travel_time = (str(int(total_travel_time//3600)) + 'h ' 
                         + str(int((total_travel_time%3600)//60)) + 'm ' 
                         + str(int((total_travel_time%3600)%60)) + 's')
    
    print('Travel time (based on filters) is: ', total_travel_time)


    # TO DO: display mean travel time
    total_travel_time_mean = df['Trip Duration'].mean()
    
    #print mean travel time
    print(str(total_travel_time_mean) + ' seconds')
    
    #Calculation procedure was adopted from here:
    #https://www.w3resource.com/python-exercises/python-basic-exercise-65.php
    #Below we check if mean < 3600 or > 3600 seconds
    #And display proper 'readble' output
    if total_travel_time_mean < 3600:
        total_travel_time_mean = (str(int(total_travel_time_mean//60)) + 'm ' 
                                  + str(int(total_travel_time_mean%60)) + 's')
    else:
        total_travel_time_mean = (str(int(total_travel_time_mean//3600)) + 'h ' 
                         + str(int((total_travel_time_mean%3600)//60)) + 'm ' 
                         + str(int((total_travel_time_mean%3600)%60)) + 's')

    print('Mean travel time (based on filters) is: ', total_travel_time_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    #Counts each user type, if none is given, they are replaced by 'Not Specified'
    user_types_count = df['User Type'].fillna('Not Specified').value_counts()
    
    print('\n-----------------\n')
    print(user_types_count)


    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if (city.replace(' ','').isalpha()) and (city.replace(' ','') != 'washington'):
        
        #Counts the gender types, if none is given, they are replaced by 'Not Specified'
        gender_count = df['Gender'].fillna('Not Specified').value_counts()
        
        print('\n-----------------\n')
        print(gender_count)
        #find earliest birth year
        earliest_YOB = int(df['Birth Year'].min())
        print('\n-----------------\n')
        print('\n Earliest birth year is... ',earliest_YOB)
        print('\n-----------------\n')
        #find most recent birth year
        recent_YOB = int(df['Birth Year'].max())
        print('\n Most recent birth year is... ',recent_YOB)
        print('\n-----------------\n')
        #find frequent birth year
        common_YOB = int(df['Birth Year'].mode()[0])
        print('\n Most common birth year is... ', common_YOB)
        print('\n-----------------\n')
        
    else:
        
        print('\n{} does not contain gender info'.format(CITY_DATA[city].upper()))
        print('\n{} does not contain Birth Date data'.format(CITY_DATA[city].upper()))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def raw_data(df):
    """ This function displays raw data upon user approval """
    #Ask user if to display raw data
    try:
        answer = input('\nwould you like to view raw data?\n')
    except KeyboardInterrupt as e:
        print('\nInvalid input {}, Exiting raw_data() function!'.format(e))
        return None
    
    start = 0
    
    if (answer.lower() != 'yes'):
        
        return None
    else:
        #iterate through the index of df
        #print 5 rows at each iteration
        for i in range(len(df.index)):
            print('\n')
            print(df.iloc[start : start + 5].to_string())
            start +=5
            print('\n')
            
            try:
                x = input('\nContinue printing raw data?\n')
                
            except KeyboardInterrupt as e:
                
                print('\nInvalid input {}, Exiting raw_data() function!'.format(e))
                return None
                
            if x != 'yes':
                
                break
            else:
                
                continue
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        try:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except KeyboardInterrupt as e:
            print('\nError encountered : {} \n Exiting the Program!'.format(e))
            break


if __name__ == "__main__":
	main()
