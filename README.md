# Question_Answer_Summerization

PDF QA Processor - README
Overview
The PDF QA Processor is a Streamlit application designed to process PDF documents, extract Question-Answer (QA) pairs, and generate a summary in PDF format. It simplifies the task of analyzing and extracting structured information from PDFs, making it suitable for researchers, educators, and professionals dealing with extensive document processing.

Features
Multiple PDF Uploads: Upload multiple PDF files for simultaneous processing.
QA Pair Extraction: Automatically extract QA pairs from PDF content.
JSON Transformation: Ensure structured and well-formatted JSON data for QA pairs.
Summary Generation: Generate a summarized version of the QA pairs.
PDF Export: Download the processed QA pairs and summary as a PDF.
Requirements
To run the application, you need the following dependencies:

Python 3.7+
Streamlit: For the web-based interface.
PyPDF2: For reading and processing PDF files.
Scikit-learn: For text similarity computations.
NumPy: For numerical operations.
PyMuPDF (fitz): For PDF text extraction and processing.
Groq: For LLM-based text summarization.
Custom Scripts:
src/preprocess.py for QA pair extraction and transformation.
src/llm_groq.py for generating summaries.
src/convert_to_pdf.py for creating PDFs from JSON data.
