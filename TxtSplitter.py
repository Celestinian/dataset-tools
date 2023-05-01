import os

# Define the input file path and the chunk size in bytes
input_file = 'GutenbergBooksDataset.txt'
chunk_size = 2 * 1024 * 1024 * 1024  # 2GB in bytes

# Get the total size of the input file in bytes
file_size = os.path.getsize(input_file)

# Open the input file for reading in binary mode
with open(input_file, 'rb') as infile:

    # Loop through the file, reading and writing chunks until the end of the file is reached
    chunk_number = 1
    while True:
        # Read a chunk of data from the input file
        chunk_data = infile.read(chunk_size)
        # If the chunk is empty, we've reached the end of the file
        if not chunk_data:
            break
        # Define the output file name and path for the current chunk
        output_file = f'./chunk_{chunk_number}.txt'
        # Open the output file for writing in binary mode
        with open(output_file, 'wb') as outfile:
            # Write the chunk data to the output file
            outfile.write(chunk_data)
        # Increase the chunk number for the next iteration
        chunk_number += 1

print(f'The file has been split into {chunk_number-1} chunks.')
