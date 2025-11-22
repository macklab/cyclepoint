# This code saves out significant cluster coordinates

import subprocess


files = [
    'zstat1',
    'zstat2',
    'zstat3',
    'zstat4',
    'zstat5',
    'zstat6',
    'zstat7',
    'zstat8',
]

def transpose(arr):
    return [list(row) for row in zip(*arr)]

outputs = []
headers = []

for filename in files:
    bash_command = f"fsl-cluster --in={filename}_cyclepoint_pvalue --thresh=0.999 --minextent=29"
    
    try:
        result = subprocess.run(bash_command, shell=True, check=True, text=True, capture_output=True)

        # Get the output
        output = result.stdout

        # Split the output into lines
        lines = output.strip().split('\n')

        # Parse each line by splitting on the tab delimiter
        parsed_data = [line.split('\t') for line in lines]

        # Print or process the parsed data
        counter = 0
        
        for row in parsed_data:
            headers.append(f'{filename}_{counter + 1}')
            if counter > 0: # skip header row
                print(f'{row[3]} ,  {row[4]},  {row[5]}')
                maxx = row[3]
                maxy = row[4]
                maxz = row[5]
                
                outputs.append([f'{filename}_{counter}', maxx, maxy, maxz])
            counter += 1
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred on file {filename}: {e}")
print('---------------')

import csv
output_file = 'process_coordinates_output.csv'

# Open the CSV file in write mode
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write each row to the CSV file
    writer.writerows(outputs)

print(f"Data has been written to {output_file}")

        

        
