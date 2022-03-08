import datetime

# Set up constants
days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# Loop to get year from user
while True:
    print('Enter the year for the calendar: ')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numerica year, like 2023.')
    continue

# Loop to get a month from user
while True:
    print('Enter a month, 1-12': )
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

def getCalendarFor(year, month):
    calText = '' # will contain the string fo our calendar

    # put month and year at top of calendar
    calText += (' ' * 34) + months[month - 1] + ' ' + str(year) + '\n'

    # add days of the week labels to the calendar:
    # try changing to abbreviations: SUN, MON, TUE
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that separates weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The bank rows have ten spaces in between the | days separators:
    blankRow = ('|          ' * 7) + '|\n'

    

