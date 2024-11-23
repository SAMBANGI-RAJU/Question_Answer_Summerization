
# **Question and Answer Summarization App**

This application processes uploaded PDF documents to extract and summarize Question-Answer (QA) pairs and generates a downloadable PDF.

---

## **Features**
- **PDF Upload**: Upload one or more PDF files for processing.
- **QA Extraction**: Automatically extracts QA pairs from the uploaded PDFs.
- **Answer Summarization**: Summarizes answers using a language model.
- **PDF Generation**: Creates a formatted PDF with bold questions and summarized answers.
- **Download Option**: Download the processed QA document as a PDF.

---

## **How to Use**
1. **Clone this repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
4. **Upload PDF files**: Upload your documents via the Streamlit interface.
5. **Download the PDF**: Once processed, download the summarized QA document.

---

## **Dependencies**
- **Streamlit**: Provides the interactive web interface.
- **PyPDF2**: Handles text extraction from PDFs.
- **PyMuPDF (fitz)**: Enables PDF manipulation.
- **Groq API**: Summarizes answers using a language model.
- **ReportLab**: Generates the formatted PDF.
- **NumPy**: Auxiliary data processing.

---

## **Project Structure**
- `app.py`: The main Streamlit application.
- `src/preprocess.py`: Handles QA pair extraction and transformation.
- `src/llm_groq.py`: Manages answer summarization using the Groq API.
- `src/convert_to_pdf.py`: Generates a PDF from processed QA data.

---

## **Example Workflow**
1. **Input**: A PDF document with QA pairs.
2. **Output**: A downloadable PDF with:
   - **Bold and larger font questions**.
   - **Summarized answers** in a clean format.

---

## **License**
This project is licensed under the MIT License.

---

**Enjoy using the app and simplifying your QA workflows!**
