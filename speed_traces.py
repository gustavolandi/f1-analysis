import fastf1 as ff1
import pandas as pd
import input_args
import matplotlib.pyplot as plt

import fastf1.plotting


args =  input_args.input_args()

year = int(args['year'])

pilot_1 = args['pilot_1']
pilot_2 = args['pilot_2']


# Enable Matplotlib patches for plotting timedelta values and load
# FastF1's dark color scheme
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, misc_mpl_mods=False,
                          color_scheme='fastf1')

# load a session and its telemetry data
session = ff1.get_session(year, args['weekend'], args['session'])

session.load()

pilot_1_lap = session.laps.pick_driver(pilot_1).pick_fastest()
pilot_2_lap = session.laps.pick_driver(pilot_2).pick_fastest()

pilot_1_tel = pilot_1_lap.get_car_data().add_distance()
pilot_2_tel = pilot_2_lap.get_car_data().add_distance()


team_pilot_1_color = fastf1.plotting.get_team_color(pilot_1_lap['Team'], session=session)
team_pilot_2_color = fastf1.plotting.get_team_color(pilot_2_lap['Team'], session=session)

fig, ax = plt.subplots()
ax.plot(pilot_1_tel['Distance'], pilot_1_tel['Speed'], color=team_pilot_1_color, label=pilot_1)
ax.plot(pilot_2_tel['Distance'], pilot_2_tel['Speed'], color=team_pilot_2_color, label=pilot_2)

ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Fastest Lap Comparison \n "
             f"{session.event['EventName']} {session.event.year} {session.name}")

plt.show()