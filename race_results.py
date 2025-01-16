import fastf1 as ff1
import pandas as pd

season_year = 2024
race_country = 'Brazil'

session = 'R'
columns_to_show = ['Position', 'DriverNumber','FullName','Time', 'Status','Points']

session = ff1.get_session(season_year, race_country, session)
session.load()

race_results = session.results
sorted_results = race_results[columns_to_show].sort_values(by='Position').head(20)

sorted_results.to_csv('race_results.csv', index=False)
race_results.to_csv('race_results_complete.csv', index=True)



