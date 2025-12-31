import markdown2
from fpdf import FPDF

# Ler o conteúdo do e-book em markdown
with open('..\\outputs\\ebook_gerado.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Converter markdown para HTML
html_content = markdown2.markdown(md_content)

# Função para converter HTML simples em texto para PDF
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
text_lines = []
for elem in soup.find_all(['h1','h2','h3','h4','h5','h6','p','li']):
    text = elem.get_text().strip()
    if text:
        text_lines.append(text)

# Criar PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)
for line in text_lines:
    pdf.multi_cell(0, 10, line)
    pdf.ln(1)

pdf.output('..\\outputs\\ebook_gerado.pdf')
print('PDF gerado em src/outputs/ebook_gerado.pdf')
