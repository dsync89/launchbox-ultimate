import os
import xml.etree.ElementTree as ET

def update_sort_title(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Find the <Name> element
    name_element = root.find(".//Name")
    if name_element is not None:
        name_value = name_element.text.strip()
        
        # Update the <SortTitle> element
        sort_title_element = root.find(".//SortTitle")
        if sort_title_element is not None:
            sort_title_element.text = f"zzz2 - {name_value}"
        
        # Write the changes back to the XML file
        tree.write(xml_file)

def process_xml_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith("Collection.xml"):
            xml_file_path = os.path.join(folder_path, filename)
            update_sort_title(xml_file_path)

# Example usage
folder_path = "."
process_xml_files(folder_path)
