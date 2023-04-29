import xml.etree.ElementTree as ET

# Set input and output file paths
input_path = "Novel.xml"
output_path = "NovelPut.txt"

# Parse the input XML file
tree = ET.parse(input_path)
root = tree.getroot()

# Open the output file for writing with UTF-8 encoding
with open(output_path, "w", encoding="utf-8") as f:

    # Iterate over each page element in the XML
    for page in root.findall("{http://www.mediawiki.org/xml/export-0.10/}page"):
        
        # Get the title and text elements of the page
        title = page.find("{http://www.mediawiki.org/xml/export-0.10/}title").text
        text = page.find("{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}text").text
        
        # Write the title and text to the output file
        f.write(f"{title}\n\n{text}\n\n")