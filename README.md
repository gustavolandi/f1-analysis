# Formula One Analysis with FastF1

## Description

Project using FastF1 with analyses from races from Formula One.

---

## How to Run

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

## Running Race Results Example
1. Copy the code from the file `race_results.py` [click here](https://github.com/gustavolandi/f1-analysis/blob/main/race_results.py).

2. Create a new notebook and paste the copied code before.

3. Finishing the execution from this script, two files named `race_results.csv` and `race_results_complete.csv` will have been created.

### Example from race_results.csv:
```csv
Position,DriverNumber,FullName,Time,Status,Points
1.0,1,Max Verstappen,0 days 02:06:54.430000,Finished,26.0
2.0,31,Esteban Ocon,0 days 00:00:19.477000,Finished,18.0
3.0,10,Pierre Gasly,0 days 00:00:22.532000,Finished,15.0
4.0,63,George Russell,0 days 00:00:23.265000,Finished,12.0
5.0,16,Charles Leclerc,0 days 00:00:30.177000,Finished,10.0
6.0,4,Lando Norris,0 days 00:00:31.372000,Finished,8.0
7.0,22,Yuki Tsunoda,0 days 00:00:42.056000,Finished,6.0
8.0,81,Oscar Piastri,0 days 00:00:44.943000,Finished,4.0
9.0,30,Liam Lawson,0 days 00:00:50.452000,Finished,2.0
10.0,44,Lewis Hamilton,0 days 00:00:50.753000,Finished,1.0
11.0,11,Sergio Perez,0 days 00:00:51.531000,Finished,0.0
12.0,50,Oliver Bearman,0 days 00:00:57.085000,Finished,0.0
13.0,77,Valtteri Bottas,0 days 00:01:03.588000,Finished,0.0
14.0,14,Fernando Alonso,0 days 00:01:18.049000,Finished,0.0
15.0,24,Guanyu Zhou,0 days 00:01:19.649000,Finished,0.0
16.0,55,Carlos Sainz,,Accident,0.0
17.0,43,Franco Colapinto,,Accident,0.0
18.0,23,Alexander Albon,,Withdrew,0.0
19.0,18,Lance Stroll,,Withdrew,0.0
20.0,27,Nico Hulkenberg,,Disqualified,0.0
```csv

---

## Notice

Please ensure you have Python 3.7 or higher installed before running this project. You can verify your Python version by running:
```bash
python --version
```
If you're using macOS or Linux, you might need to use `python3` instead of `python`. 
