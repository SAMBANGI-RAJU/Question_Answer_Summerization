import streamlit as st
import os
from groq import Groq
from PyPDF2 import PdfReader
import numpy as np
import tempfile
import json
import fitz

from src.preprocess import get_qa_pairs, transform_data, fix_json_structure
from src.llm_groq import generate_summary
from src.convert_to_pdf import create_pdf_from_json

st.title("PDF QA Processor")
st.write("Upload your PDF documents, and we'll extract and process the QA pairs.")

# Directory to temporarily store uploaded PDFs
upload_dir = "uploaded_pdfs"
os.makedirs(upload_dir, exist_ok=True)

# File uploader for multiple PDFs
uploaded_files = st.file_uploader(
    "Upload PDF files", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    qa_list = []
    for uploaded_file in uploaded_files:
        # Save uploaded files to the directory
        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Process the uploaded PDF
        doc = fitz.open(file_path)
        st.write(f"Processing: {uploaded_file.name}")

        # Extract and process QA pairs
        qa_pairs = get_qa_pairs(doc)
        updated_json = fix_json_structure(qa_pairs)
        qa_list.append(updated_json)

    # Transform the data after all PDFs are processed
    final_data = transform_data(qa_list)

    # # Save the transformed data to a JSON file
    # json_file_path = "final_check_transform1.json"
    # with open(json_file_path, "w") as file:
    #     json.dump(final_data, file, indent=4)

    final_json = generate_summary(final_data)
    pdf = create_pdf_from_json(final_json)
    st.success("Processing complete!")
    st.download_button(
        label="Download PDF File",
        data=pdf,
        file_name="questions_answers.pdf",
        mime="application/pdf",
    )
