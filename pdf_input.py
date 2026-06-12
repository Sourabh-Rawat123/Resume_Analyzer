import streamlit as st
import json
from pdf_reader import extract_text
from clean_txt import clean_resume_text
from prompt import generate_prompt
from ai_analysis import analyze_resume
def pdf_input():
    st.header("AI Resume Analyzer")

    file = st.file_uploader(
        "Please upload your PDF resume for analysis",
        type=["pdf"]
    )

    if file is not None:
        st.success("File uploaded successfully")
        job_title=st.text_area("Enter the job title you are targeting")
        if st.button("Analyze File"):
            st.write("Analyzing PDF...")
            text=extract_text(file)
            if text:
                cleaned_text=clean_resume_text(text)
                if cleaned_text:
              
                  system_prompt, user_prompt=  generate_prompt(cleaned_text,job_title)
                  if system_prompt and user_prompt:
                    analysis_results=analyze_resume(system_prompt, user_prompt)
                    if analysis_results:
                        st.success("Analysis completed successfully")
                        text=json.loads(analysis_results.text)
                        st.subheader("Resume Analysis Results")
                        st.json(text)
                    else:
                        st.error("Failed to analyze the resume.")
                else:
                    st.error("Failed to clean the resume text.")
            else:
                st.error("Failed to extract text from the PDF file.")

                pass

    else:
        st.info("Please upload a PDF file.")

if __name__ == "__main__":
    pdf_input()