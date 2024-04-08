import python_weather
import asyncio
import os


async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    # user_weather = input("Enter a city: ")
    # weather = await client.get(user_weather)
    user_weather = input("Enter a city: ")
    weather = await client.get(user_weather)
    format_weather = f"{user_weather} : {weather.temperature}°F - {weather.description}"
    print(format_weather)
    # returns the current day's forecast temperature (int)
    return format_weather
  
  
  
  
  
    

if __name__ == '__main__':
  
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())
  