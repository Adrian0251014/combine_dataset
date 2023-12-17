import pandas as pd

def process_intervals(file_path, output_path, duration):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Function to merge overlapping intervals
    def merge_overlapping_intervals(data):
        merged = []
        current_start = data.iloc[0]['Begin Time - ss.msec']
        current_end = data.iloc[0]['End Time - ss.msec']

        for index, row in data.iterrows():
            if row['Begin Time - ss.msec'] <= current_end:
                current_end = max(current_end, row['End Time - ss.msec'])
            else:
                merged.append([current_start, current_end])
                current_start = row['Begin Time - ss.msec']
                current_end = row['End Time - ss.msec']

        merged.append([current_start, current_end])
        return pd.DataFrame(merged, columns=['Begin Time - ss.msec', 'End Time - ss.msec'])

    # Sort the data by the beginning time
    sorted_data = data.sort_values(by='Begin Time - ss.msec')

    # Merge overlapping intervals
    merged_intervals = merge_overlapping_intervals(sorted_data)

    # Create new intervals with specified duration
    interval_list = []
    for index, row in merged_intervals.iterrows():
        start_time = row['Begin Time - ss.msec']
        end_time = row['End Time - ss.msec']

        while start_time + duration <= end_time:
            interval_list.append([start_time, start_time + duration])
            start_time += duration

        if start_time < end_time:
            interval_list.append([start_time, end_time])

    # Create dataframe from interval list
    interval_df = pd.DataFrame(interval_list, columns=['Begin Time - ss.msec', 'End Time - ss.msec'])
    interval_df['Duration'] = duration

    # Extracting additional columns from the original data
    additional_columns = data.columns[4:]
    additional_data = data[additional_columns]

    # Merge additional data with new intervals
    merged_data = pd.DataFrame(columns=['Begin Time - ss.msec', 'End Time - ss.msec', 'Duration'] + list(additional_columns))

    for index, row in interval_df.iterrows():
        start_time = row['Begin Time - ss.msec']
        end_time = row['End Time - ss.msec']

        overlapping_rows = data[(data['Begin Time - ss.msec'] < end_time) & (data['End Time - ss.msec'] > start_time)]
        if not overlapping_rows.empty:
            merged_row = overlapping_rows[additional_columns].fillna(' ').agg(' '.join).replace('  ', ' ')
            new_row = pd.Series([start_time, end_time, duration] + merged_row.tolist(), index=merged_data.columns)
            merged_data = merged_data.append(new_row, ignore_index=True)

    # Save the merged data to a CSV file
    merged_data.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Interactive input in the terminal
    input_file_path = input("Input CSV file path: ")
    output_file_path = input("Input modified CSV file path: ")
    duration_input = float(input("Input duration value: "))

    process_intervals(input_file_path, output_file_path, duration_input)
