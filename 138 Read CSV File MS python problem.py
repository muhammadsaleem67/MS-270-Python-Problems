def read_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            # Read lines and strip out the trailing \n characters
            lines = file.readlines()
            
            for line in lines:
                # Split by comma to recreate the list
                row = line.strip().split(',')
                data.append(row)
        return data
    except FileNotFoundError:
        return []
print(read_csv('python.csv'))