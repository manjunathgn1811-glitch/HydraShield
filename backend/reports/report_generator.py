from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet

def create_report():

    doc = SimpleDocTemplate(
        "reports/HydraShield_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "HydraShield Security Report",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            "Generated automatically",
            styles["Normal"]
        )
    )

    doc.build(content)

    return True