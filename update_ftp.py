import ftplib
f = open("../prettify.ai.txt", "r")
raw = f.read()
lines = raw.split("\n")
server_address = lines[0]
username = lines[1]
password = lines[2]
print(server_address, username, password)


print("Making FTP object")
session = ftplib.FTP(server_address, username, password)
print("Reading file")
file = open('html/index.html','rb')                  # file to send
print("Changing directory")
session.cwd("public_html")
print("In directory: \t", session.pwd())
print("Sending file")
return_code = session.storbinary('STOR index.html', file, blocksize=10, callback=print('DONE'))     # send the file
print("Return Code: ", return_code)
print("DONE!")
file.close()                                    # close file and FTP
session.quit()

#print(lines)
