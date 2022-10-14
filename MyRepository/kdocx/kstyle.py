#########################################################################################
# The initial intention was to create a standard to ".docx" files with pre-defined styles.
# It still needs to be implemented.
#########################################################################################

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Pt
from docx.shared import RGBColor
from docx.shared import Cm


def estilos(document):
    styles = document.styles

    font = "Times New Roman"
    color = RGBColor(0, 0, 0)

    # Style Paragraph
    p = styles.add_style("Paragraph", WD_STYLE_TYPE.PARAGRAPH)
    p.font.name = font
    p.font.size = Pt(12)

    p_format = p.paragraph_format
    p_format.left_indent = Cm(0.5)
    p_format.first_line_indent = Cm(0.0)
    p_format.space_before = Pt(0)
    p_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Style Heading1
    h1 = styles.add_style("H1", WD_STYLE_TYPE.PARAGRAPH)
    h1.base_style = styles["Heading1"]
    h1.font.name = font
    h1.font.size = Pt(14)
    h1.font.color.rgb = color
    h1.font.bold = True

    h1_format = h1.paragraph_format
    h1_format.space_before = Pt(0)
    h1_format.space_after = Pt(0)
    h1_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h1.ListLevelNumber = 1

    # Style Heading2
    h2 = styles.add_style("H2", WD_STYLE_TYPE.PARAGRAPH)
    h2.base_style = styles["Heading2"]
    h2.font.name = font
    h2.font.size = Pt(13)
    h2.font.color.rgb = color
    h2.font.bold = True

    h2_format = h1.paragraph_format
    h2_format.space_before = Pt(0)
    h2_format.space_after = Pt(0)
    h2_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h2.ListLevelNumber = 2

    # Style Heading3
    h3 = styles.add_style("H3", WD_STYLE_TYPE.PARAGRAPH)
    h3.base_style = styles["Heading3"]
    h3.font.name = font
    h3.font.size = Pt(12)
    h3.font.color.rgb = color
    h3.font.bold = True

    h3_format = h1.paragraph_format
    h3_format.space_before = Pt(0)
    h3_format.space_after = Pt(0)
    h3_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h3.ListLevelNumber = 3
