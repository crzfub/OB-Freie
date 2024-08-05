import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import ControlBoundsPen
from xml.etree import ElementTree as ET


def extract_svg_per_character(font_path, output_folder, margin=10, scale_factor=1.0):
    font = TTFont(font_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print(f"Processing font: {font_path}")
    glyph_set = font.getGlyphSet()
    skipped_glyphs = []

    for glyph_name in font.getGlyphOrder():
        if glyph_name.startswith("uni") or glyph_name.startswith("gid"):
            continue

        def ntos(coord):
            return str(round(coord, 4))

        glyph = glyph_set[glyph_name]
        bounds_pen = ControlBoundsPen(glyph_set)
        glyph.draw(bounds_pen)
        bounds = bounds_pen.bounds

        if bounds is None:
            print(f"Skipping glyph '{glyph_name}' due to missing bounds")
            skipped_glyphs.append(glyph_name)
            continue

        xmin, ymin, xmax, ymax = bounds

        # Check if the glyph is empty (has zero area)
        if xmin == xmax or ymin == ymax:
            print(f"Skipping empty glyph '{glyph_name}'")
            skipped_glyphs.append(glyph_name)
            continue

        print(
            f"Processing glyph: {glyph_name}, bounds: ({xmin}, {ymin}, {xmax}, {ymax})"
        )

        width = (xmax - xmin) * scale_factor + 2 * margin
        height = (ymax - ymin) * scale_factor + 2 * margin

        translation_matrix = (
            scale_factor,
            0,
            0,
            -scale_factor,
            (-xmin * scale_factor) + margin,
            (ymax * scale_factor) + margin,
        )

        spen = SVGPathPen(glyph_set, ntos)
        pen = TransformPen(spen, translation_matrix)
        glyph.draw(pen)
        svg_path_data = spen.getCommands()

        # Skip if no path data (empty glyph)
        if not svg_path_data:
            print(f"Skipping empty glyph '{glyph_name}'")
            skipped_glyphs.append(glyph_name)
            continue

        svg_elem_attrib = {
            "xmlns": "http://www.w3.org/2000/svg",
            "width": str(width),
            "height": str(height),
            "viewBox": f"0 0 {width} {height}",
        }
        svg_elem = ET.Element("svg", attrib=svg_elem_attrib)
        path_elem = ET.SubElement(
            svg_elem, "path", attrib={"d": svg_path_data, "fill": "black"}
        )
        svg_filename = os.path.join(output_folder, f"{glyph_name}.svg")
        with open(svg_filename, "w") as svg_file:
            svg_file.write(ET.tostring(svg_elem, encoding="unicode"))
        print(f"Saved SVG for glyph '{glyph_name}' to '{svg_filename}'")

    font.close()

    # Print list of skipped glyphs
    print("\nSkipped glyphs:")
    for glyph_name in skipped_glyphs:
        try:
            codepoint = f"U+{ord(glyph_name):04X}"
        except TypeError:
            codepoint = "N/A"
        print(f"{glyph_name} (Codepoint: {codepoint})")

    return skipped_glyphs


# Usage
font_path = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBNLFreie-Light.ttf"
font_path2 = (
    "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBNLFreie-Regular.ttf"
)
font_path3 = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/build/OBNLFreie-Bold.ttf"
output_folder = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/svg/light"
output_folder2 = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/svg/regular"
output_folder3 = "/Users/corvin/things/OB-Freie/OB-Freie/OBFreie/svg/bold"

skipped_light = extract_svg_per_character(
    font_path, output_folder, margin=10, scale_factor=0.5
)
skipped_regular = extract_svg_per_character(
    font_path2, output_folder2, margin=10, scale_factor=0.5
)
skipped_bold = extract_svg_per_character(
    font_path3, output_folder3, margin=10, scale_factor=0.5
)

print("\nAll skipped glyphs:")
print("Light:", skipped_light)
print("Regular:", skipped_regular)
print("Bold:", skipped_bold)
