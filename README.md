# Guide Sheet Generator

Small python script to generate guide sheets (lined, dotted, grid, calligraphy). Uses fpdf2 to generate PDF.

## Usage

```
Worksheet generator to generate blank worksheets.

positional arguments:
  output

options:
  -h, --help            show this help message and exit
  --spacing SPACING     Spacing in mm
  --width WIDTH         Page width in mm
  --height HEIGHT       Page height in mm
  --margin-left MARGIN_LEFT
                        Left margin in mm
  --margin-right MARGIN_RIGHT
                        Right margin in mm
  --margin-top MARGIN_TOP
                        Top margin in mm
  --margin-bottom MARGIN_BOTTOM
                        Bottom margin in mm
  --calligraphy-angular-guides
                        Calligraphy angular guides
  --calligraphy-angular-guides-angle CALLIGRAPHY_ANGULAR_GUIDES_ANGLE
                        Calligraphy angular guides angle in deg
  --calligraphy-angular-guides-spacing CALLIGRAPHY_ANGULAR_GUIDES_SPACING
                        Calligraphy angular guides spacing
  --calligraphy-line-guides
                        Calligraphy line guides
  --calligraphy-x-size CALLIGRAPHY_X_SIZE
                        Calligraphy guides x size in mm
  --calligraphy-x-ratio CALLIGRAPHY_X_RATIO
                        Calligraphy x size ratio
  --calligraphy-ascender-ratio CALLIGRAPHY_ASCENDER_RATIO
                        Calligraphy ascender ratio
  --calligraphy-descender-ratio CALLIGRAPHY_DESCENDER_RATIO
                        Calligraphy descender ratio
  --calligraphy-line-spacing CALLIGRAPHY_LINE_SPACING
                        Calligraphy line guides spacing
  --border              Border around worksheet
  --mode {lines,grid,dots,calligraphy}
                        Worksheet style
```
