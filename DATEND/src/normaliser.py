import docx
from docx import Document
from docx.shared import Pt



doc = Document('sample.docx')

for para in doc.paragraphs:
    para.paragraph_format.line_spacing = 1.0
    para.paragraph_format.space_before = Pt(12)  # 12 points spacing before
    para.paragraph_format.space_after = Pt(12)

doc.save('modified.docx')
print('done')
