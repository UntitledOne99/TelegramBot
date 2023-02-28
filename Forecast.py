import pyowm
import test

owm = pyowm.OWM("2921429c42bc140ec123eafbb77f33d8")

snowflake = '\U00002744'
hot = '\U0001F525'
clear_sky = '\U00002600'
cloud = '\U00002601'


def weather():
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f"{test.city}")
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    status = (w.detailed_status).capitalize()
    rain = w.rain
    if temperature < 0:
        message = f'The weather for today is:\n{status}\n   {temperature} {snowflake} \n{test.city}'
    elif temperature > 0 and status == 'Clear sky':
        message = f'The weather for today is:\n{status}\n   {temperature} {clear_sky} \n{test.city}'
    elif temperature > 0 and status == 'Hot':
        message = f'The weather for today is:\n{status}\n   {temperature} {hot} \n{test.city}'
    else:
        message = f'The weather for today is:\n{status}\n   {temperature} {cloud} \n{test.city}'
    test.city = 'Mins'
    return message
