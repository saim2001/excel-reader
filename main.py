import pandas as pd

def load_excel(file_path):
    # Load the Excel file into a pandas DataFrame, using the second row (index 1) as the header
    df = pd.read_excel(file_path, header=1)
    df.columns = df.columns.str.strip()
    return df

def query_excel(df, name, day, time):
    try:
        # Filter the DataFrame based on the name and day
        filtered_df = df[(df['Name'] == name) & (df['Day'] == day)]
        print(filtered_df)
        
        # If the filtered DataFrame is empty, return an error message
        if filtered_df.empty:
            return f"No data found for name: {name} and day: {day}"
        
        # Get the value corresponding to the provided time
        value = filtered_df[time].values[0]
        return value
    except KeyError:
        return f"Invalid time: {time}"

def main():
    # Load the Excel file
    file_path = 'TENTATIVE INDIVIDUAL TIMETABLES UPDATED ON 26-2-24.xlsx'  # Replace with the path to your Excel file
    df = load_excel(file_path)
    # print(df['11.10-12.10PM'])
    
    # Input values
    name = 'Dr. D. Durga Bhavani'
    day = 'WEDNESDAY'
    time = '10-11AM'
    
    # Query the DataFrame
    result = query_excel(df, name, day, time)
    print(f"The value for {name} on {day} at {time} is: {result}")

if __name__ == "__main__":
    main()
