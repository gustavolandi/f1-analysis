# Formula One Analysis with FastF1

## Description

Project using FastF1 with analyses from races from Formula One.

---

## How to Run

Please ensure you have Python 3.7 or higher installed before running this project. You can verify your Python version by running:
```bash
python --version
```
If you're using macOS or Linux, you might need to use `python3` instead of `python`. 

If you want to run this project in a virtual environment, I recommend you create and activate it by running the following commands:

### Windows
```cmd
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

After activating the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

To run the project in a Jupyter Notebook:
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open the notebook file (.ipynb) in the Jupyter interface.

To deactivate the virtual environment when you're done:
```bash
deactivate
```

---

## Running Race Results Example

### Using notebook runscripts
1. Open the notebook runscripts.ipynb
2. Execute the command
```bash
%run race_results.py year=2024 weekend='Brazil' session='R' export_excel='True' excel_file_name='results_race_excel'
```
The following parameters are necessary:
   - year;
   - weekend;
   - session:
      
      - 'R' for Races
      - 'Q' for Qualifying
      - 'S' for Sprint
      - 'SQ' for Sprint Qualifying

If you desire to export in excel or csv, you can use the following parameters:
   For excel:
      export_excel='True'
      excel_file_name='WRITE_YOUR_DESIRED_FILE_NAME'
   For csv:
      export_csv='True'
      csv_file_name='WRITE_YOUR_DESIRED_FILE_NAME'

If you desire to filter results, you can filter them by adding the parameter filter_results with the following values:

   - 'Top' followed by a number between 1 and 20 to get the first n positions. 
      
      Example: 'Top10' to get the first 10 positions
      
   - 'Podium' to get the first 3 positions
   - 'Team' to get the results of a team
      - Add parameter 'team' with the name of the Team 
   - 'Driver' to get the results of a driver
      - Add parameter 'driver' with the Driver Abbreviation or Number

In the example, the script is getting data from 2024 São Paulo Grand Prix and saving a file named results_race_excel.xlsx. And it's going to plot the data in the following image:

![](assets/race_results_example.png)

Other examples:
```bash

#plot table with results from Qualifying from Ferrari Team
%run race_results.py year=2024 weekend='Brazil' session='Q' filter_results='Team' team='Ferrari'

#plot table with results from Race from Max Verstappen
%run race_results.py year=2024 weekend='Brazil' session='R' filter_results='Driver' driver='VER'

#plot table with results from Sprint Race from Lando Norris and export to both csv and excel
%run race_results.py year=2024 weekend='Brazil' session='S' filter_results='Driver' driver='4' export_csv='True' csv_file_name='results_race_norris' export_excel='True' excel_file_name='results_race_norris'
```
---

## Filters

### 2024

#### Team

| Team            | 
|-----------------|
| McLaren         |    
| Ferrari         | 
| Red Bull Racing | 
| Mercedes        |
| RB              |
| Williams        |
| Alpine          |
| Haas F1 Team    |
| Kick Sauber     |

#### DriverNumber and Abbreviation

| DriverNumber | Abbreviation |
|--------------|--------------|
| 1            | VER          |
| 4            | NOR          |
| 10           | GAS          |
| 11           | PER          |
| 14           | ALO          |
| 16           | LEC          |
| 18           | STR          |
| 22           | TSU          |
| 23           | ALB          |
| 24           | ZHO          |
| 27           | HUL          |
| 30           | LAW          |
| 31           | OCO          |
| 43           | COL          |
| 44           | HAM          |
| 50           | BEA          |
| 55           | SAI          |
| 63           | RUS          |
| 77           | BOT          |
| 81           | PIA          |


## Notice

This project is unofficial and is not associated in any way with the Formula 1 companies. F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V.
