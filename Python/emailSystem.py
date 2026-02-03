import datetime  # To work with date and time for email timestamps

# --- Email Class ---
# Represents a single email message
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender      # The user sending the email
        self.receiver = receiver  # The user receiving the email
        self.subject = subject    # Email subject line
        self.body = body          # Content/body of the email
        self.timestamp = datetime.datetime.now()  # Time when the email was created
        self.read = False         # Email is unread by default

    # Mark the email as read
    def mark_as_read(self):
        self.read = True

    # Display all details of the email
    def display_full_email(self):
        self.mark_as_read()  # Automatically mark as read when displayed
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # Short representation of the email (used when listing inbox)
    def __str__(self):
        status = 'Read' if self.read else 'Unread'  # Show if email is read or unread
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

# --- Inbox Class ---
# Represents a user's collection of emails
class Inbox:
    def __init__(self):
        self.emails = []  # List to store all emails

    # Receive a new email and add it to the inbox
    def receive_email(self, email):
        self.emails.append(email)

    # List all emails in the inbox
    def list_emails(self):
        if not self.emails:  # Check if inbox is empty
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')  # Print each email using its __str__ method

    # Read a specific email by number (1-based index)
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1  # Convert to 0-based index
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    # Delete a specific email by number (1-based index)
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1  # Convert to 0-based index
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')

# --- User Class ---
# Represents a person using the email system
class User:
    def __init__(self, name):
        self.name = name      # User's name
        self.inbox = Inbox()  # Each user has their own inbox

    # Send an email to another user
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)  # Add email to receiver's inbox
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # Check inbox and list all emails
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")  # Personalized inbox header
        self.inbox.list_emails()           # Display emails

    # Read an email by its number through the User object
    def read_email(self, index):
        self.inbox.read_email(index)

    # Delete an email by its number through the User object
    def delete_email(self, index):
        self.inbox.delete_email(index)

# --- Main Function ---
# Demonstrates sending, reading, deleting, and checking emails
def main():
    # Create two users
    tory = User('Tory')
    ramy = User('Ramy')        
    
    # Send emails between users
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

    # --- Inbox Operations for Ramy ---
    # 1. Ramy checks his inbox
    ramy.check_inbox()

    # 2. Ramy reads the first email
    print("\nReading the first email...")
    ramy.read_email(1)  # Read email through User object

    # 3. Ramy deletes the first email
    print("Deleting the first email...")
    ramy.delete_email(1)  # Delete email through User object

    # 4. Ramy checks his inbox again to see the changes
    ramy.check_inbox()

# Run the program
if __name__ == '__main__':
    main()
