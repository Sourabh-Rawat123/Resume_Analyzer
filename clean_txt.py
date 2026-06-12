import re

def clean_resume_text(text):

    # Remove non-breaking spaces
    text = re.sub(r'\xa0', ' ', text)

    # Normalize all whitespace
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove excessive blank lines
    text = re.sub(r'\n\s*\n+', '\n', text)

    # Remove page numbers
    text = re.sub(
        r'\bpage\s+\d+\b',
        '',
        text,
        flags=re.IGNORECASE
    )

    # Remove emails
    text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        '[EMAIL]',
        text
    )
            

    # Remove phone numbers
    text = re.sub(
        r'(\+?\d{1,3}[\s\-]?)?(\(?\d{2,5}\)?[\s\-]?)?\d{5}[\s\-]?\d{5}',
        '[PHONE]',
        text
    )
    # Remove LinkedIn and GitHub URLs
    text = re.sub(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b|https?://(?:www\.)?(?:linkedin\.com|github\.com)/\S+',
    '[PROFILE]',
    text,
    flags=re.IGNORECASE
    )

    return text.strip()