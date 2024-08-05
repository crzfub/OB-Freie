import xml.etree.ElementTree as ET
import sys

## Usage:
## python remove_unicode.py /path/to/font.ttx 1234


def remove_unicode(ttx_path, unicode_to_remove):
    tree = ET.parse(ttx_path)
    root = tree.getroot()

    namespaces = {
        "ttx": "http://www.w3.org/2000/svg"  # Define the namespace used in the TTX file
    }

    # Find and remove the cmap entry
    for cmap in root.findall(".//ttx:cmap_format_4", namespaces):
        for map_element in cmap.findall(".//ttx:map", namespaces):
            if map_element.attrib["code"] == hex(unicode_to_remove):
                print(f"Removing cmap entry for Unicode: {hex(unicode_to_remove)}")
                cmap.remove(map_element)

    # Find and remove the glyph entry
    glyph_removed = False
    for glyf in root.findall(".//ttx:glyf", namespaces):
        for glyph in glyf.findall(".//ttx:glyph", namespaces):
            if glyph.attrib.get("name") == f"uni{hex(unicode_to_remove)[2:].upper()}":
                print(f"Removing glyph: {glyph.attrib['name']}")
                glyf.remove(glyph)
                glyph_removed = True
                break
        if glyph_removed:
            break

    # Save the modified TTX file
    tree.write(ttx_path, encoding="utf-8", xml_declaration=True)
    print(f"Saved modified TTX file: {ttx_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_unicode.py <path_to_ttx> <unicode_to_remove>")
        sys.exit(1)

    ttx_path = sys.argv[1]
    unicode_to_remove = int(sys.argv[2], 16)  # Expecting Unicode value as hex string

    remove_unicode(ttx_path, unicode_to_remove)
