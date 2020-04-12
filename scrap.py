import bs4, requests, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
dictionary={}
table=""
avaliable=False


for i in range(1):     # Number of pages plus one
    getPage = requests.get("https://www.freshercooker.in/category/courses/btech-be/internship/page/"+str(i)+"/")
    getPage.raise_for_status()
    menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
    n=menu.find_all("h3",{"class":["entry-title"]})
    for i in n:
        lol=(i.findChildren("a"))
        for link in lol:
            name=link.get('title').split(" ")[0].lower()

            dictionary[name]=link.get('href')
            avaliable=True

    getPage = requests.get('https://www.offcampusjobs4u.com/category/internship/')
    getPage.raise_for_status()
    menu = bs4.BeautifulSoup(getPage.text,'html.parser')
    n=menu.find_all("h3",{"class":["entry-title"]})

    for i in n:
        lol=(i.findChildren("a"))

        lol=(i.findChildren("a"))
        for link in lol:
            name=link.get('title').split(" ")[0].lower()
            dictionary[name]=link.get('href')
            avaliable=True
    
for a in dictionary:
    table+="<tr> <td>"+a+"</td>"+"<td>"+dictionary[a]+"</td></tr>"

message = MIMEMultipart("alternative")

reciever = "mharsh301@gmail.com"
sender = "mharsh6896@gmail.com.com"

message['Subject'] = "Link"
message['From'] = reciever
message['To'] = sender

text = """\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!"""

# write the HTML part
html = """\
<html>
    <head></head>
        <body><table border="1">+"""+table+"""
         </table>
        </body>
</html>
"""
# convert both parts to MIMEText objects and add them to the MIMEMultipart message

part1=MIMEText(text,'plain')
part2 = MIMEText(html, 'html')
message.attach(part1)
message.attach(part2)


if avaliable == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.ehlo()
    conn.login('useremailid@gmail.com', 'yourpassword')
    conn.sendmail(sender,reciever,message.as_string())
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
else:
    print('not sented.')
