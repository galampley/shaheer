import mailbox
import re

def extract_email_addresses(mbox_path):
    # Initialize a set to store unique email addresses
    email_addresses = set()
    
    # Open the mbox file
    mbox = mailbox.mbox(mbox_path)
    
    # Regular expression pattern to match email addresses
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    for message in mbox:
        # Extract email addresses from the 'From' field
        from_field = message.get('from', '')
        email_addresses.update(re.findall(email_pattern, from_field))
        
        # Extract email addresses from the 'To' field
        to_field = message.get('to', '')
        email_addresses.update(re.findall(email_pattern, to_field))
        
        # Extract email addresses from the 'Cc' field
        cc_field = message.get('cc', '')
        email_addresses.update(re.findall(email_pattern, cc_field))
        
        # Extract email addresses from the 'Bcc' field
        bcc_field = message.get('bcc', '')
        email_addresses.update(re.findall(email_pattern, bcc_field))
        
    return email_addresses

# Path to the MBOX file
mbox_file_path = 'Navi_Attachment.mbo'

# Extract email addresses
unique_emails = extract_email_addresses(mbox_file_path)

# Print all unique email addresses
for email in unique_emails:
    print(email)
