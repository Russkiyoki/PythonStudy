from ftplib import FTP

# Use a REAL public FTP server
my_ftp = FTP('ftp.gnu.org')  # GNU's public FTP
my_ftp.login()               # Anonymous login works here

my_ftp.cwd('/pub')           # Change to /pub directory
my_ftp.retrlines('LIST')     # List files

my_ftp.quit()
