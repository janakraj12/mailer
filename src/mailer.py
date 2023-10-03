import imaplib
import email
def get_unread_emails(imap_server, username, password):
    # Connect to the IMAP server
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, password)
    # Select the inbox folder
    imap.select("Inbox")
    # Search for unread emails
    status, email_ids = imap.search(None, "UNSEEN")
    # Fetch the unread emails
    unread_emails = []
    for email_id in email_ids[0].split():
        status, email_data = imap.fetch(email_id, "(RFC822)")
        unread_emails.append(email.message_from_bytes(email_data[0][1]))
    # Close the connection
    imap.close()
    return unread_emails