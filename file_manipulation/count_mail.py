name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# find all lines starting with "From" and capture the email address in the list 'emails'
emails = list()
for line in handle:
    if line.startswith('From '):
        emails.append(line.split(' ')[1])
#print(emails)

# from the list 'emails',  capture the email and the number of times in the dictionary "email counts"
email_counts = dict()
for email in emails:
    email_counts[email] = email_counts.get(email, 0) + 1
#print(email_counts)

# find the most times an email is seen
big_email = None
big_count = None

for email,count in email_counts.items():
    if big_email is None or count > big_count:
        big_email = email
        big_count = count

print(big_email, big_count)