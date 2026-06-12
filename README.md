# AI Resume Analyzer

AI Resume Analyzer is a small Streamlit app that uploads a PDF resume, extracts its text, cleans sensitive or noisy content, and sends it to Gemini for ATS-focused feedback.

## Features

- Upload a PDF resume through a web UI
- Extract text from PDF files
- Clean common resume noise such as extra whitespace, emails, phone numbers, and profile links
- Generate an ATS-oriented prompt for analysis
- Return structured feedback from the Gemini model

## Project Structure

- `pdf_input.py` - Streamlit UI and end-to-end workflow
- `pdf_reader.py` - PDF text extraction
- `clean_txt.py` - Resume text cleanup helpers
- `prompt.py` - Prompt generation for the model
- `ai_analysis.py` - Gemini client wrapper for resume analysis

## Requirements

- Python 3.10 or later
- A Google Gemini API key

## Installation

Install the Python dependencies:

```bash
pip install streamlit pypdf python-dotenv google-genai
```

The app also uses the `genai` package listed in `package.json`.

## Configuration

Create a `.env` file in the project root and add your API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

## Run the App

Start the Streamlit app with:

```bash
streamlit run pdf_input.py
```

## How It Works

1. Upload a resume PDF.
2. Enter the target job title.
3. The app extracts and cleans the resume text.
4. A structured prompt is generated for ATS analysis.
5. Gemini returns resume feedback in JSON format.

## Notes

- The app expects a valid PDF resume.
- Analysis quality depends on the quality of the extracted text and the target job title provided by the user.
- If you extend the app, consider adding explicit error handling around model responses and JSON parsing.