import bz2
import re

input_file = r"C:\Users\zehmi\Downloads\enwiki-20230401-pages-articles-multistream.xml.bz2"
output_file = r"./Wikipedia.txt"
max_line_length = 350

with bz2.BZ2File(input_file, "r") as f, open(output_file, "w", encoding="utf-8") as output:
    # Define regex pattern to extract text from XML tags
    pattern = re.compile(r'<.*?>')

    for line in f:
        # Decode bytes to string
        line = line.decode("utf-8")

        # Remove XML tags and whitespace
        line = re.sub(pattern, "", line).strip()

        # Split line into segments with maximum length of 350 characters
        segments = [line[i:i+max_line_length] for i in range(0, len(line), max_line_length)]

        # Write segments to output file
        for segment in segments:
            output.write(segment + "\n")
