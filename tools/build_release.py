#!/usr/bin/env python3
"""Local release tooling only. Never include this script in the Skill ZIP."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACK = 'Automate Your Workflow'
ENTRANT = 'Jiayi Guan'


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


def proposal_parts(source):
    sections = re.split(r'^## (\d+\. .+)$', source, flags=re.M)
    pairs = [(sections[i], sections[i + 1].split('\n---')[0].strip())
             for i in range(1, len(sections), 2)]
    if len(pairs) != 10:
        raise ValueError('proposal must contain exactly ten numbered responses')
    return pairs


def render_pdf(path, source):
    import reportlab
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    fonts = Path(reportlab.__file__).parent / 'fonts'
    pdfmetrics.registerFont(TTFont('Vera', str(fonts / 'Vera.ttf')))
    pdfmetrics.registerFont(TTFont('Vera-Bold', str(fonts / 'VeraBd.ttf')))
    styles = {
        'title': ParagraphStyle('title', fontName='Vera-Bold', fontSize=18,
                                leading=22, textColor=colors.HexColor('#183D43'), spaceAfter=12),
        'heading': ParagraphStyle('heading', fontName='Vera-Bold', fontSize=10.5,
                                  leading=14, spaceBefore=12, spaceAfter=4, keepWithNext=True),
        'body': ParagraphStyle('body', fontName='Vera', fontSize=10.1,
                              leading=13.2, alignment=TA_LEFT),
        'note': ParagraphStyle('note', fontName='Vera', fontSize=8.1,
                              leading=10.5, textColor=colors.HexColor('#455A64')),
    }
    story = [Paragraph('Trip Wrap-Up', styles['title']),
             Paragraph('UGREEN Hackathon 2026', styles['heading']),
             Paragraph(TRACK, styles['note']),
             Paragraph(f'Submitted by: {ENTRANT}', styles['note']),
             Spacer(1, 6)]
    pairs = proposal_parts(source)
    for index, (question, answer) in enumerate(pairs):
        if index == 5:
            story.extend([PageBreak(), Paragraph('Trip Wrap-Up', styles['heading'])])
        story.extend([Paragraph(escape(question), styles['heading']),
                      Paragraph(escape(answer).replace('\n', '<br/>'), styles['body'])])
    disclosure = source.split('\n---\n', 1)[1].strip()
    story.extend([Spacer(1, 16), Paragraph('Tools and AI assistance', styles['heading'])])
    for paragraph in disclosure.split('\n\n'):
        story.extend([Paragraph(escape(paragraph), styles['note']), Spacer(1, 5)])
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Vera', 8)
        canvas.setFillColor(colors.HexColor('#455A64'))
        canvas.drawString(42, 25, 'UGREEN Hackathon 2026 | Trip Wrap-Up')
        canvas.drawRightString(A4[0] - 42, 25, str(doc.page))
        canvas.restoreState()
    SimpleDocTemplate(str(path), pagesize=A4, leftMargin=42, rightMargin=42,
                      topMargin=35, bottomMargin=42, title='Trip Wrap-Up',
                      author=ENTRANT).build(story, onFirstPage=footer, onLaterPages=footer)


def render_docx(path, source):
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor

    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Inches(8.27), Inches(11.69)
    section.top_margin = section.bottom_margin = Inches(0.55)
    section.left_margin = section.right_margin = Inches(0.65)
    normal = doc.styles['Normal']
    normal.font.name, normal.font.size = 'Calibri', Pt(11)
    normal.paragraph_format.space_after = Pt(7)
    normal.paragraph_format.line_spacing = 1.1
    for name in ['Title', 'Heading 2']:
        style = doc.styles[name]
        style.font.name = 'Calibri'
        style.font.color.rgb = RGBColor.from_string('000000')
    heading = doc.styles['Heading 2']
    heading.font.size, heading.font.bold = Pt(11), True
    heading.paragraph_format.space_before = Pt(10)
    heading.paragraph_format.space_after = Pt(4)
    heading.paragraph_format.keep_with_next = True
    doc.add_paragraph('Trip Wrap-Up', style='Title')
    doc.add_paragraph(f'UGREEN Hackathon 2026 · {TRACK}')
    doc.add_paragraph(f'Submitted by: {ENTRANT}')
    for index, (question, answer) in enumerate(proposal_parts(source)):
        p = doc.add_paragraph(question, style='Heading 2')
        if index == 5:
            p.paragraph_format.page_break_before = True
        for line in answer.splitlines():
            numbered = re.match(r'^\d+\.\s+(.+)$', line)
            if numbered:
                doc.add_paragraph(numbered.group(1), style='List Number')
            elif line.strip():
                doc.add_paragraph(line)
    doc.add_paragraph('Tools and AI assistance', style='Heading 2')
    for paragraph in source.split('\n---\n', 1)[1].strip().split('\n\n'):
        p = doc.add_paragraph(paragraph)
        for run in p.runs:
            run.font.size = Pt(9)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer.add_run('Trip Wrap-Up · ').font.size = Pt(9)
    page = OxmlElement('w:fldSimple')
    page.set(qn('w:instr'), 'PAGE')
    footer._p.append(page)
    doc.core_properties.title = 'Trip Wrap-Up'
    doc.core_properties.subject = 'UGREEN Hackathon 2026 proposal'
    doc.core_properties.author = ENTRANT
    doc.save(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kit', type=Path, required=True,
                        help='official extracted uliya-skill-kit directory; not redistributed')
    parser.add_argument('--version', default='0.2.1', help='new release version, such as 0.2.1')
    args = parser.parse_args()
    if not re.fullmatch(r'\d+\.\d+\.\d+', args.version):
        raise SystemExit('Version must have the form major.minor.patch.')
    version = args.version
    package = ROOT / 'trip-wrap-up'
    release = ROOT / f'proposal/releases/v{version}'
    if release.exists():
        raise SystemExit(f'Release v{version} already exists; existing releases are preserved.')
    source_path = ROOT / f'proposal/proposal-v{version}-review.md'
    source = source_path.read_text()
    words = sum(len(answer.split()) for _, answer in proposal_parts(source))
    if words > 500:
        raise SystemExit(f'Proposal exceeds 500 words: {words}')
    checked = subprocess.run(['node', str(args.kit / 'scripts/check-skill.mjs'), str(package)],
                             text=True, capture_output=True, check=True)
    check_data = json.loads(checked.stdout)
    if check_data['status'] != 'static-pass':
        raise SystemExit(checked.stdout)
    math = subprocess.run([sys.executable, str(ROOT / 'tools/verify_settlement.py')],
                          text=True, capture_output=True, check=True)
    math_data = json.loads(math.stdout)
    assert math_data['status'] == 'pass'
    files = sorted(p for p in package.rglob('*') if p.is_file())
    assert 1 <= len(files) <= 100
    assert all(p.suffix == '.md' and not p.is_symlink() for p in files)
    assert all(p.stat().st_size <= 1024 * 1024 for p in files)
    assert sum(p.stat().st_size for p in files) <= 10 * 1024 * 1024
    skill = (package / 'SKILL.md').read_text()
    for p in files:
        if p.name != 'SKILL.md':
            assert f']({p.relative_to(package).as_posix()})' in skill, p
    release.mkdir(parents=True)
    archive = release / f'trip-wrap-up-v{version}.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in files:
            # Stable archive metadata makes repeated builds from identical sources reproducible.
            info = zipfile.ZipInfo('trip-wrap-up/' + p.relative_to(package).as_posix(),
                                   date_time=(2026, 11, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, p.read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for p in files:
            assert z.read('trip-wrap-up/' + p.relative_to(package).as_posix()) == p.read_bytes()
    assert archive.stat().st_size <= 10 * 1024 * 1024
    pdf = release / f'trip-wrap-up-proposal-v{version}-review.pdf'
    render_pdf(pdf, source)
    assert pdf.stat().st_size <= 1024 * 1024
    docx = release / 'trip-wrap-up-proposal.docx'
    render_docx(docx, source)
    write_json(release / 'static-check.json', check_data)
    write_json(release / 'math-check.json', math_data)
    evidence = {
        'status': 'pass', 'version': version, 'kit_version': '0.7.7',
        'catalog_version': '2.2.0', 'file_count': len(files),
        'uncompressed_bytes': sum(p.stat().st_size for p in files),
        'zip_bytes': archive.stat().st_size,
        'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
        'zip_sources_identical': True,
        'proposal_answer_words_whitespace': words,
        'proposal_pdf_bytes': pdf.stat().st_size,
        'proposal_pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'proposal_docx_bytes': docx.stat().st_size,
        'proposal_docx_sha256': hashlib.sha256(docx.read_bytes()).hexdigest(),
        'nas_runtime_validated': False,
        'proposal_status': 'proposal revision; original and earlier releases preserved',
        'source_files': {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in files},
    }
    write_json(release / 'package-check.json', evidence)
    print(json.dumps(evidence, indent=2))


if __name__ == '__main__':
    main()
