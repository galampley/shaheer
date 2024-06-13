import streamlit as st
import mailbox
import re
import tempfile
from email.utils import parsedate_to_datetime
import streamlit.components.v1 as components

def extract_email_addresses_and_dates(mbox_path):
    emails_data = {}
    mbox = mailbox.mbox(mbox_path)
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    for message in mbox:
        date = message.get('date', '')
        if date:
            date = parsedate_to_datetime(date)
        
        from_field = message.get('from', '')
        from_emails = re.findall(email_pattern, from_field)
        for email in from_emails:
            emails_data[email] = date

        to_field = message.get('to', '')
        to_emails = re.findall(email_pattern, to_field)
        for email in to_emails:
            emails_data[email] = date
        
        cc_field = message.get('cc', '')
        cc_emails = re.findall(email_pattern, cc_field)
        for email in cc_emails:
            emails_data[email] = date
        
        bcc_field = message.get('bcc', '')
        bcc_emails = re.findall(email_pattern, bcc_field)
        for email in bcc_emails:
            emails_data[email] = date
        
    return emails_data

# Streamlit app
st.title("Shaheer's Email Tool")

st.write("Scroll thru the below for step-by-step guide.")

# Embed Scribe snippet
scribe_embed_code = '<iframe src="https://scribehow.com/embed/How_to_get_relevant_file_for_Shaheers_Email_Tool__513TAW_OTTmR9fE8DWvogQ?as=scrollable" width="100%" height="640" allowfullscreen frameborder="0"></iframe>'

components.html(scribe_embed_code, height=400)

uploaded_file = st.file_uploader("Choose an MBOX file", type="mbox")

if uploaded_file is not None:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name
    
    # Extract email addresses and dates
    emails_data = extract_email_addresses_and_dates(temp_file_path)
    
    # Display the unique email addresses and dates
    st.write(f"Found {len(emails_data)} unique email addresses with dates:")
    for email, date in emails_data.items():
        st.write(f"{email} - Sent on: {date}")


