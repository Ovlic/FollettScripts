
import xmltodict, json, os
import lxml.etree as etree

folder_path = 'path/to/folder'



def to_json_and_export(fpath, fname):
    tree = etree.parse(fpath)
    xml_data = tree.getroot()
    #here you can change the encoding type to be able to set it to the one you need
    xmlstr = etree.tostring(xml_data, encoding='utf-8', method='xml')


    print("Parsing file...", end='')
    d = xmltodict.parse(xmlstr)
    print(" Done.")

    print("Converting to JSON...", end='')
    j = json.dumps(d, indent=4)
    print(" Done.")

    print("Writing to file...", end='')
    with open(fname, 'w') as fil:
        fil.write(j)
    print(" Done.")



def pretty_print_xml(fpath, add_header=False):
    print("Parsing file...", end='')
    x = etree.parse(fpath)
    print("     Done.")

    print("Pretty printing...", end='')
    new_x = '<?xml version="1.0" encoding="UTF-8"?>\n' + etree.tostring(x, pretty_print=True).decode()
    print(" Done.")

    # Replace current file with pretty printed version
    print("Writing to file...", end='')
    with open(fpath, 'w') as fil:
        fil.write(new_x)
    print(" Done.")


# Loop through files in folder 'extract_site'
for filename in os.listdir(folder_path):
    if filename.endswith('.xml'):
        print("Current file: ", filename)
        fpath = os.path.join(folder_path, filename)
        new_fpath = os.path.join(folder_path, "json", filename.replace('.xml', '.json'))
        print("Path: ", fpath)
        print("New Path: ", new_fpath)
        
        # pretty_print_xml(fpath, add_header=True)
        to_json_and_export(fpath, new_fpath)
        print("---------------------")

exit()


fpath = 'path/to/file'
f = ''

print("Reading file...", end='')
with open(fpath, 'r') as fil:
    f = fil.read()
print(" Done.")

# Pretty print
print("Parsing file...", end='')
x = etree.parse(fpath)
print(" Done.")

print("Pretty printing...", end='')
new_x = etree.tostring(x, pretty_print=True).decode()
print(" Done.")

print("Writing to file...", end='')
with open('extracted_site_formatted.xml', 'w') as fil:
    fil.write(new_x)
print(" Done.")


"""
print("Parsing file...", end='')
d = xmltodict.parse(f)
print(" Done.")

print("Converting to JSON...", end='')
j = json.dumps(d, indent=4)
print(" Done.")

print("Writing to file...", end='')
with open('extracted_site.json', 'w') as fil:
    fil.write(j)
print(" Done.")

"""