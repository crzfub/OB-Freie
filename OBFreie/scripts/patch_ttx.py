import xml.etree.ElementTree as ET


def replace_name_records(ttx_file_path, new_records_file_path):
    # Parse the TTX and new name records XML files
    ttx_tree = ET.parse(ttx_file_path)
    ttx_root = ttx_tree.getroot()

    new_records_tree = ET.parse(new_records_file_path)
    new_records_root = new_records_tree.getroot()

    name_elem = ttx_root.find("name")
    if name_elem is None:
        raise ValueError("No <name> element found in the TTX file.")

    # Iterate over new name records and update or add them to the TTX file
    for new_record in new_records_root:
        nameID = new_record.get("nameID")
        platformID = new_record.get("platformID")
        platEncID = new_record.get("platEncID")
        langID = new_record.get("langID")

        # Find the existing record
        existing_record = None
        for record in name_elem.findall("namerecord"):
            if (
                record.get("nameID") == nameID
                and record.get("platformID") == platformID
                and record.get("platEncID") == platEncID
                and record.get("langID") == langID
            ):
                existing_record = record
                break

        if existing_record is not None:
            name_elem.remove(existing_record)

        # Add the new record
        name_elem.append(new_record)

    # Write the modified TTX file back to the same path
    ttx_tree.write(ttx_file_path, encoding="UTF-8", xml_declaration=True)


# Paths to the TTX and new name records XML files
ttx_file_path1 = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBFreie-Light.ttx"
)
ttx_file_path2 = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBFreie-Regular.ttx"
)
ttx_file_path3 = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBFreie-Bold.ttx"

ttx_file_path4 = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBNLFreie-Light.ttx"
)
ttx_file_path5 = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBNLFreie-Regular.ttx"
)
ttx_file_path6 = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBNLFreie-Bold.ttx"
)

new_records_file_path = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/scripts/namerecords.xml"
)
new_records_file_path2 = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/scripts/namerecords_obnl.xml"
)

# OB_Freie
replace_name_records(ttx_file_path1, new_records_file_path)
replace_name_records(ttx_file_path2, new_records_file_path)
replace_name_records(ttx_file_path3, new_records_file_path)

# OBNL
replace_name_records(ttx_file_path4, new_records_file_path2)
replace_name_records(ttx_file_path5, new_records_file_path2)
replace_name_records(ttx_file_path6, new_records_file_path2)
