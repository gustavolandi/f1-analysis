from matplotlib import pyplot as plt

import fastf1 as ff1
import fastf1.plotting
import input_args


args =  input_args.input_args()
year = int(args['year'])

session = ff1.get_session(year, args['weekend'], args['session'])
session.load()
laps = session.laps

drivers = session.drivers

drivers = [session.get_driver(driver)["Abbreviation"] for driver in drivers]

stints = laps[["Driver", "Stint", "Compound", "LapNumber"]]
stints = stints.groupby(["Driver", "Stint", "Compound"])
stints = stints.count().reset_index()

stints = stints.rename(columns={"LapNumber": "StintLength"})

fig, ax = plt.subplots(figsize=(5, 10))

for driver in drivers:
    driver_stints = stints.loc[stints["Driver"] == driver]

    previous_stint_end = 0
    for idx, row in driver_stints.iterrows():
        # each row contains the compound name and stint length
        # we can use these information to draw horizontal bars
        compound_color = fastf1.plotting.get_compound_color(row["Compound"],
                                                            session=session)
        plt.barh(
            y=driver,
            width=row["StintLength"],
            left=previous_stint_end,
            color=compound_color,
            edgecolor="black",
            fill=True
        )

        previous_stint_end += row["StintLength"]
    
plt.title(f"{year} {args['weekend']} Grand Prix Strategies")
plt.xlabel("Lap Number")
plt.grid(False)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()