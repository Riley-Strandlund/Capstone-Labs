def get_location():
    city, country = '',''
    while len(city) == 0:
        city = input('Enter the city: ')
    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ')
    location = f'{city},{country}'
    return location