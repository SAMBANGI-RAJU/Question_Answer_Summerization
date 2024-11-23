import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT
from io import BytesIO


def create_pdf_from_json(json_data):
    # Set up the PDF document
    buffer = BytesIO()
    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
    )

    # Define styles
    styles = getSampleStyleSheet()
    question_style = styles["Heading2"]
    question_style.fontName = "Helvetica-Bold"
    question_style.fontSize = 14
    question_style.leading = 16

    answer_style = styles["BodyText"]
    answer_style.fontName = "Helvetica"
    answer_style.fontSize = 11
    answer_style.leading = 14
    answer_style.alignment = TA_LEFT

    elements = []

    for question, answer in json_data.items():
        # Add the question
        elements.append(Paragraph(question, question_style))
        elements.append(Spacer(1, 12))  # Spacer between question and answer

        # Add the answer
        elements.append(Paragraph(answer, answer_style))
        elements.append(Spacer(1, 20))  # Spacer between entries

    pdf.build(elements)
    buffer.seek(0)
    return buffer


# # Load JSON data
# json_file = r"D:\My Downloads\final.json"# Replace with your file path
# output_pdf = "questions_answers.pdf"

# with open(json_file, "r") as file:
#     json_data = json.load(file)

# # Create the PDF
# create_pdf_from_json(json_data, output_pdf)

# print(f"PDF generated successfully: {output_pdf}")
