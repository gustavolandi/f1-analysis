import fastf1 as ff1
import pandas as pd
import input_args
import matplotlib.pyplot as plt
import re
import os


columns_to_show_race = ['Position','DriverNumber','FullName','TeamName','TotalTime','Time','Status','Points','GridPosition']
columns_to_show_sprint = ['Position','DriverNumber','FullName','TeamName','TotalTime','Time','Status','Points','GridPosition']
columns_to_show_qualifying = ['Position','DriverNumber','FullName','TeamName','Q1','Q2','Q3']
columns_to_show_sprint_qualifying = ['Position','DriverNumber','FullName','TeamName','Q1','Q2','Q3']
columns_to_show_free_practice = ['DriverNumber','FullName','TeamName']

def main():

    args =  input_args.input_args()
    year = int(args['year'])
    filter_results = '' if 'filter_results' not in args else args['filter_results']  
    export_excel = 'export_excel' in args and args['export_excel'] == 'True'
    excel_file_name = 'race_results' if 'excel_file_name' not in args else args['excel_file_name']
    export_csv = 'export_csv' in args and args['export_csv'] == 'True'
    csv_file_name = 'race_results' if 'csv_file_name' not in args else args['csv_file_name']

    session = ff1.get_session(year, args['weekend'], args['session'])
    session.load()

    race_results = session.results

    get_total_time(race_results,args['session'])

    filtered_results = get_filter_to_results(filter_results,race_results=race_results,args=args)
    
    sorted_results = filtered_results[columns_to_export_to_file(args['session'])].sort_values(by='Position').head(20)

    export_to_files(export_excel,export_csv,filtered_results,sorted_results,excel_file_name,csv_file_name)
    
    plot_table(sorted_results)

def export_to_files(export_excel,export_csv,filtered_results,sorted_results,excel_file_name,csv_file_name):
    if export_excel:
        excel_file_name = os.path.splitext(excel_file_name)[0]
        export_to_excel(sorted_results,excel_file_name,'Results')
        export_to_excel(filtered_results,f"{excel_file_name}-complete",'Results')
    if export_csv:
        csv_file_name = os.path.splitext(csv_file_name)[0]
        sorted_results.to_csv(f'{csv_file_name}.csv', index=False)
        filtered_results.to_csv(f'{csv_file_name}-complete.csv', index=False)

def get_filter_to_results(filter_results,race_results,args):
    if 'Top' in filter_results:
        filtered_results = race_results[race_results['Position'] <= filter_top_position(filter_results)]
    elif filter_results == 'Podium':
        filtered_results = race_results[race_results['Position'] <= 3]
    elif filter_results == 'Team':
        filtered_results = race_results[race_results['TeamName'] == args['team']]
    elif filter_results == 'Driver':
        filtered_results = race_results[filter_by_driver(race_results,args['driver'])]
    else:
        filtered_results = race_results
    return filtered_results

def columns_to_export_to_file(session):
    if session== 'R':
        columns_to_show = columns_to_show_race
    if session == 'Q':
        columns_to_show = columns_to_show_qualifying
    if session == 'S':
        columns_to_show = columns_to_show_sprint
    if session == 'SQ':
        columns_to_show = columns_to_show_sprint_qualifying
    if 'FP' in session:
        columns_to_show = columns_to_show_free_practice
    return columns_to_show

def filter_by_driver(race_results,driver):
    driver = str(driver).strip().upper()
    if re.fullmatch(r'\d+', driver): 
        return race_results['DriverNumber'] == driver
    elif re.fullmatch(r'[A-Z]{3}', driver):  
        return race_results['Abbreviation'] == driver
    
def filter_top_position(filter_results):
    match = re.fullmatch(r'Top(\d{1,2})', filter_results)
    
    if match:
        position = int(match.group(1))

        if 1 <= position <= 20:
            return position
        else:
            raise ValueError("The number must be between 1 and 20.")
    else:
        raise ValueError("The filter must start with 'Top' followed by a number between 1 and 2O.")
    
def get_total_time(race_results,session):
    if is_race_or_sprint(session):
        race_results["TotalTime"] = pd.to_timedelta(race_results["Time"]) 
        time_first_position = race_results.loc[race_results['Position'] == 1, "TotalTime"].values[0]
        race_results.loc[race_results["Position"] > 1, "TotalTime"] = race_results.loc[race_results["Position"] > 1, "TotalTime"] + time_first_position
    adjust_time(race_results,session)

def adjust_time(results,session):
    if is_race_or_sprint(session):
        results['Time'] = format_time(results,'Time')
        results['TotalTime'] = format_time(results,'TotalTime')
    if is_qualifying(session) :
        results['Q1'] = format_time(results,'Q1')
        results['Q2'] = format_time(results,'Q2')
        results['Q3'] = format_time(results,'Q3')
    if 'FP' in session:
        results['Time'] = format_time(results,'Time')

def is_race_or_sprint(session):
    return session == 'R' or session == 'S'

def is_qualifying(session):
    return session == 'Q' or session == 'SQ'

def format_time(results,field):
    results[field] = pd.to_timedelta(results[field])
    def format_timedelta(x):
            if pd.isna(x):
                return "NaT"
            
            hours = x.components.hours
            minutes = x.components.minutes
            seconds = x.components.seconds
            milliseconds = x.components.milliseconds
            
            if hours > 0:
                return f"{hours}:{minutes:02}:{seconds:02}.{milliseconds:03}"
            
            if minutes > 0:
                return f"+ {minutes}:{seconds:02}.{milliseconds:03}"
        
            return f"+ {seconds}.{milliseconds:03}"
    return results[field].apply(format_timedelta).astype(str)

def export_to_excel(results,excel_file_name,sheet_name):
    with pd.ExcelWriter(f'{excel_file_name}.xlsx', engine='xlsxwriter') as writer:
            results.to_excel(writer, index=False, sheet_name=sheet_name)

            workbook = writer.book
            worksheet = writer.sheets[sheet_name]

            header_format = workbook.add_format({'bold': True, 'text_wrap': True, 'valign': 'center', 'fg_color': '#D7E4BC', 'border': 1})
            for col_num, value in enumerate(results.columns.values):
                worksheet.write(0, col_num, value, header_format)

def plot_table(results):
    fig, ax = plt.subplots(figsize=(20, 15))
    ax.axis('tight')
    ax.axis('off')

    table = ax.table(cellText=results.values, colLabels=results.columns, loc='center', cellLoc='center')

    for key, cell in table.get_celld().items():
        if key[0] == 0:
            cell.set_facecolor("lightblue")  
            cell.set_text_props(color="black", weight="bold", size=50)
        else:
            cell.set_facecolor("white")  
            cell.set_text_props(color="darkblue", size=40) 

    plt.show()

if __name__ == "__main__":
    main()








