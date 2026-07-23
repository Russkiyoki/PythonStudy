# AI GENERATED
from ftplib import FTP
import os

# Connect to your web host
ftp = FTP('yourwebsite.com')
ftp.login('your_username', 'your_password')

# Go to where your website lives
ftp.cwd('/public_html')  # Common folder for websites

# Upload ALL your website files
files_to_upload = ['index.html', 'style.css', 'script.js', 'about.html']

for file in files_to_upload:
    with open(file, 'rb') as f:
        ftp.storbinary(f'STOR {file}', f)
        print(f'Uploaded: {file}')

# Upload an entire folder (images)
ftp.mkd('/public_html/images')  # Create folder
ftp.cwd('/public_html/images')

for image in os.listdir('local_images/'):
    with open(f'local_images/{image}', 'rb') as f:
        ftp.storbinary(f'STOR {image}', f)
        print(f'Uploaded image: {image}')

ftp.quit()
print('Website deployed successfully!')
