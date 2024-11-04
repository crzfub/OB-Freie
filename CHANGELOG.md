# Changelog

All notable changes to this project will be documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [2.0.0] - 2024-11-04

This update brings improved glyph placement and bigger glyphs as well
as technical updates to improve compliancy with the OSL.

It sees two added signs: ABZL084 Šulgi X PUA U+F0055 , ABZL215 UMUM 𒌣 U+12323 and one deletion: 𒇹 U+121F9. Which was previously an extra assignment for the glyph 𒐂 U+12402.

### Added
#### Mergers
- ABZL211 AŠ2 𒀾 U+1203E mirrored to 𒍩 U+12369
- ABZL417 TUG2 𒌆 mirrored to 𒉇 U+12247
- ABZL297 IM 𒅎 mirrored to 𒉎 U+1224E
- ABZL420 ŠE3 𒂠 mirrored to 𒍥 U+12365
- ABZL025 BAD 𒁁 mirrored to 𒅂 U+12142 and 𒌀 U+12300
- ABZL008 ĠIR2 𒄉 mirrored to 𒄈 U+12108
- ABZL277 HI 𒄭 mirrored to 𒊹 U+122B9
- ABZL415 KU 𒆪 mirrored to 𒂉 U+12089
- ABZL143 PA 𒉺 mirrored to 𒑐 U+12450
- ABZL474 U+1235D 𒍝 = 𒍝 U+12409
    1. removed the 𒐼 U+1243C mirror in 𒍝 U+12409
    2. added the U+1235D 𒍝 mirror to 𒍝 U+12409
#### New Signs
- ABZL084 Šulgi X variant added as ŠIM@ġxPI in PUA U+F0055
- ABZL215 UMUM variant added as UMUM 𒌣 U+12323 (the glyph DE2 𒌤 that was assigned this codepoint in 1.2.0 was moved to U+12324)

### Changed

#### Glyph Placement
The glyphs were lowered significantly and consequently scaled.
They should now fill the EM-box, more pleasingly and align
with Latin fonts.

This will see further improvements in future updates as well.

#### PUA Remaps
These remaps follow the private use area remaps as in OSL now rather
than just being put in the first PUA chars.

- ABZL200 LUG2-ġ-š U+E005 -> U+F005D
- ABZL219a AGA U+E004 -> U+F005C
- ABZL130 ABxA U+E002 -> U+F004E
- ABZL133 SUKUD U+E003 -> U+F005B
- ABZL103 ĠA2xŠU2 U+E001 -> U+F005A
- ABZL095 ĠA2xNU U+E000 -> U+F0059

ABZL084 is now moved into the PUA and the Šulgi X Form is added as well.

- ABZL084 ŠIMxX2 𒋆𒂵 -> U+F00FE
	removed the ligature and moved the glyph to PUA U+F005E
	 (see Added ABZL084 Šulgi X Form added as ŠIM@ġxPI in PUA U+F0055)

#### Other Moves/Remaps
- ABZL215 DE2 U+12323 -> U+12324
- ABZL084 SZIMxX.liga -> U+5005E

#### Features
- ABZL022 SZESZxNA.liga -> SZESZxKI.liga
	changed ligature:
	`U+122C0 U+1223E -> U+122C0 U+121AO`

- ABZL341 SZIBIR.liga
	changed ligature:
	`U+1210b U+1230b -> U+1230b U+12099`

#### Glyph Improvements
- ABZL189 EREN 𒂞 U+1209E - improved weight balance to fit with better with the other glyphs; partial redraw
- ABZL401a TUN3 𒂅 U+12085 - essential fixes to dying horizontal wedge; some minor redraws

#### Sign List PDF
The sign list was updated to reflect the changes. For now it does not list
double encodings/mergers.
### Removed

- Removed double encoding U+121F9

### Fixed

- Removed empty codepoints

### Additional Note

In [91f1f55](https://github.com/oracc/osl/commit/91f1f55d310170985e6d125b12bdd76a9f01300c) Tinney recommends moving 'extra 4' HIxGAD 𒄲
U+12132 to *ss01*/*salt*. However as it is part of the glyph composition
ABZL423 KEŠ3 𒋙𒀭𒄲 it is kept to maintain graphic feedback - rather
than having to ship an empty glyph.

This follows the concept of including non-ABZL glyphs ZI:ZI and LAL2 as part of their ligatures.
