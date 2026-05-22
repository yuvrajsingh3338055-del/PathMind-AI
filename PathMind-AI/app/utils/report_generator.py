from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    skills,
    ats_score
):

    pdf_file = "PathMind_Report.pdf"

    document = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "PathMind AI Career Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    score = Paragraph(
        f"ATS Score: {ats_score}%",
        styles['Heading2']
    )

    elements.append(score)

    elements.append(
        Spacer(1, 20)
    )

    skill_title = Paragraph(
        "Detected Skills",
        styles['Heading2']
    )

    elements.append(skill_title)

    for skill in skills:

        skill_text = Paragraph(
            f"• {skill}",
            styles['BodyText']
        )

        elements.append(skill_text)

    document.build(elements)

    return pdf_file