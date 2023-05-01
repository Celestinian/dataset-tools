import os

# Define the name of the output file
output_file = 'merged_files.txt'

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:

    # Loop through all the directories and files in the current directory
    for dirpath, dirnames, filenames in os.walk('.'):

        # Loop through all the files in the current directory
        for filename in filenames:

            # Check if the file is a text file
            if filename.endswith('.txt'):

                # Open the file and read its contents
                with open(os.path.join(dirpath, filename), 'r', encoding='utf-8') as infile:
                    contents = infile.read()

                # Write the contents of the file to the output file
                outfile.write(contents)

# Print a message indicating that the files have been merged
print('All files have been merged into ' + output_file)
