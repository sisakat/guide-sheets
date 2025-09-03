import sys
import numpy as np
import argparse
from fpdf import FPDF

def main():
    parser = argparse.ArgumentParser(
        description="Worksheet generator to generate blank worksheets."
    )
    parser.add_argument("output", type=str)
    parser.add_argument("--spacing", type=float, help="Spacing in mm", default=5)
    parser.add_argument("--width", type=float, help="Page width in mm", default=210)
    parser.add_argument("--height", type=float, help="Page height in mm", default=297)
    parser.add_argument("--margin-left", type=float, help="Left margin in mm", default=10)
    parser.add_argument("--margin-right", type=float, help="Right margin in mm", default=10)
    parser.add_argument("--margin-top", type=float, help="Top margin in mm", default=6)
    parser.add_argument("--margin-bottom", type=float, help="Bottom margin in mm", default=6)
    parser.add_argument("--calligraphy-angular-guides", help="Calligraphy angular guides", action="store_true", default=False)
    parser.add_argument("--calligraphy-angular-guides-angle", type=float, help="Calligraphy angular guides angle in deg", default=55)
    parser.add_argument("--calligraphy-angular-guides-spacing", type=float, help="Calligraphy angular guides spacing", default=None)
    parser.add_argument("--calligraphy-line-guides", help="Calligraphy line guides", action="store_true", default=False)
    parser.add_argument("--calligraphy-x-size", type=float, help="Calligraphy guides x size in mm", default=6)
    parser.add_argument("--calligraphy-x-ratio", type=float, help="Calligraphy x size ratio", default=2)
    parser.add_argument("--calligraphy-ascender-ratio", type=float, help="Calligraphy ascender ratio", default=3)
    parser.add_argument("--calligraphy-descender-ratio", type=float, help="Calligraphy descender ratio", default=3)
    parser.add_argument("--calligraphy-line-spacing", type=float, help="Calligraphy line guides spacing", default=5)
    parser.add_argument("--border", help="Border around worksheet", action="store_true", default=False)
    parser.add_argument("--mode", help="Worksheet style", choices=[
        "lines",
        "grid",
        "dots",
        "calligraphy"
    ], default="grid")
    args = parser.parse_args()

    pdf = FPDF(orientation="portrait", format=(args.width, args.height))
    pdf.add_page()

    grid_width = args.spacing # mm
    margin_l = args.margin_left # mm
    margin_r = args.margin_right # mm
    margin_t = args.margin_top # mm
    margin_b = args.margin_bottom # mm
    content_width = pdf.w - margin_l - margin_r
    content_height = pdf.h - margin_t - margin_b
    border_color = (200, 200, 200)
    grid_color = (200, 200, 200)

    if args.border:
        pdf.set_draw_color(border_color)
        pdf.line(margin_l, margin_t, pdf.w - margin_r, margin_t)
        pdf.line(margin_l, pdf.h - margin_b, pdf.w - margin_r, pdf.h - margin_b)
        pdf.line(margin_l, margin_t, margin_l, pdf.h - margin_b)
        pdf.line(pdf.w - margin_r, margin_t, pdf.w - margin_r, pdf.h - margin_b)

    xes = np.arange(content_width, step=grid_width)[1:]
    yes = np.arange(content_height, step=grid_width)[1:]

    pdf.set_draw_color(grid_color)
    if args.mode in ["lines", "grid"]:
        # horizontal lines
        for y in yes:
            pdf.line(margin_l, margin_t + y, pdf.w - margin_r, margin_t + y)
    if args.mode == "grid":
        # vertical lines
        for x in xes:
            pdf.line(margin_l + x, margin_t, margin_l + x, pdf.h - margin_b)

    if args.mode in ["dots"]:
        pdf.set_fill_color(grid_color)
        for x in xes:
            for y in yes:
                pdf.circle(margin_l + x, margin_t + y, 0.3, style="F")

    if args.mode == "calligraphy" and args.calligraphy_line_guides:
        # line guides (x line, ascender, descender)
        x_size_ratio = args.calligraphy_x_ratio
        x_size = args.calligraphy_x_size
        ascender_ratio = args.calligraphy_ascender_ratio
        descender_ratio = args.calligraphy_descender_ratio
        ascender_size = x_size * ascender_ratio / x_size_ratio
        descender_size = x_size * descender_ratio / x_size_ratio
        spacing = args.calligraphy_line_spacing
        yes = np.arange(content_height, step=(spacing + x_size + ascender_size + descender_size))[0:-1]
        for y in yes:
            y = y + ascender_size + x_size + spacing

            # x line
            pdf.line(margin_l, margin_t + y, pdf.w - margin_r, margin_t + y)
            pdf.line(margin_l, margin_t + y - x_size, pdf.w - margin_r, margin_t + y - x_size)

            # ascender and descender
            prev_line_width = pdf.line_width
            pdf.set_dash_pattern(dash=2, gap=3)
            pdf.line(margin_l, margin_t + y - x_size - ascender_size, pdf.w - margin_r, margin_t + y - x_size - ascender_size)
            pdf.line(margin_l, margin_t + y + descender_size, pdf.w - margin_r, margin_t + y + descender_size)
            pdf.set_line_width(prev_line_width)
            pdf.set_dash_pattern()

    if args.mode == "calligraphy" and args.calligraphy_angular_guides:
        # angular guides
        spacing = args.calligraphy_angular_guides_spacing if args.calligraphy_angular_guides_spacing else args.spacing
        arad = np.deg2rad(args.calligraphy_angular_guides_angle)
        min_x = -content_height / np.tan(arad)
        max_x = content_width
        xes = np.linspace(min_x, max_x, int((max_x - min_x) // spacing))
        yes = np.ones_like(xes) * content_height

        for i in range(len(xes)):
            a = (xes[i], 0)
            b = (xes[i] + content_height / np.tan(arad), yes[i])
            pdf.set_dash_pattern(dash=1, gap=2)
            with pdf.rect_clip(margin_l, margin_t, content_width, content_height):
                pdf.line(margin_l + a[0], margin_t + content_height - a[1], margin_l + b[0], margin_t + content_height - b[1])

    pdf.output(args.output)
    return 0

if __name__ == "__main__":
    sys.exit(main())
