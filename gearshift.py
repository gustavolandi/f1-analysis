import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps
from matplotlib.collections import LineCollection

import fastf1
import input_args
import importlib

def main():

    importlib.reload(input_args)
    args =  input_args.input_args()
    year = int(args['year'])

    session = fastf1.get_session(year, args['weekend'], args['session'])
    session.load()

    drivers = args['drivers'].strip('[]').split(',') if 'drivers' in args else session.drivers

    laps = session.laps.pick_drivers(drivers)

    laps = laps.dropna(subset=['LapTime'])

    fastest_laps = laps.loc[laps.groupby('Driver')['LapTime'].idxmin()]

    for _, lap in fastest_laps.iterrows():
        telemetry = lap.get_telemetry()

        x = np.array(telemetry['X'].values)
        y = np.array(telemetry['Y'].values)

        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        gear = telemetry['nGear'].to_numpy().astype(float)

        cmap = colormaps['Paired']
        lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
        lc_comp.set_array(gear)
        lc_comp.set_linewidth(4)

        plt.gca().add_collection(lc_comp)
        plt.axis('equal')
        plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

        title = plt.suptitle(
            f"Fastest Lap Gear Shift Visualization\n"
            f"{lap['Driver']} - {session.event['EventName']} {session.event.year}"
        )

        cbar = plt.colorbar(mappable=lc_comp, label="Gear",
                            boundaries=np.arange(1, 10))
        cbar.set_ticks(np.arange(1.5, 9.5))
        cbar.set_ticklabels(np.arange(1, 9))


        plt.show()

if __name__ == "__main__":
    main()