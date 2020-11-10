import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xhtml2pdf import pisa # import python module
# Define your data
webinar_code = {
    
'nwaoparaao@yahoo.com':'GER/EDO/WEB/20/HOST',

'lordrichado@gmail.com': 'GER/EDO/WEB/20/18',
'daodurichard55@gmail.com': 'GER/EDO/3401',

}
webinar_full_name= {
    'nwaoparaao@yahoo.com':'Prof Anthony Nwaopara',
'tzdollypatty@gmail.com':'Dolapo patience Ajidagba',
'tosinadewole84@gmail.com':'Oluwatosin Catherine Adewole',
'akinroakintunde@gmail.com':'Akintunde Akolawole Akinro',
'revdoh@gmail.com':'Donatus Osiokha Anokhaoya',
'olubukolaolotu@gmail.com':'Catherine Olubukunola Olotu',
'faithtambari@gmail.com':'Faith Tambari Nkiinu',
'lovethanosike1@gmail.com':'NNENNA LOVETH ANOSIKE',
'rukevweomeru@gmail.com':'OGHENERUKEVWE PERETOMODE',
'vc@edouniversity.edu.ng':'Engr. Prof. E. O. Aluyor',
'chukwujemima1@gmail.com':'Jemima Adanna Chukwu',
'mathiaskennedy8@gmail.com':'Ebhojaye Kennedy',
'egbeiyonstella@gmail.com':'Stella Egbeiyon',
'peace.omofonmwan01@gmail.com':'Peace Ebuwa Omofonmwan',
'nancydominic22@gmail.com':'NANCY AIROBOMA OGBIDI',
'tolulanguyz@gmail.com':'Tolulope Samuel Oladele',
'oyewale.abdulwaheed@kasu.edu.ng':'Abdulwaheed A. Oyewale',
'marshallakinola@gmail.com':' Emmanuel Taiwo Akinola',

'lordrichado@gmail.com': 'Richard Olumide Daodu',
'daodurichard55@gmail.com': 'Richard Daodu'


}


for emails in webinar_code.keys():
    source_html = """<html>
    <head>
        <link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>

        <link href="http://fonts.googleapis.com/css?family=Tangerine" rel="stylesheet" type="text/css" />
        <title>Gersep Cert</title>
        <style type="text/css">
            body {
                font-weight: 200;
                font-size: 14px;

            }
            .header {
                font-size: 20px;
                font-weight: 100;
                text-align: center;
                color: #007cae;
            }
            .title {
                font-size: 22px;
                font-weight: 100;
               /* text-align: right;*/
               padding: 10px 20px 0px 20px;
            }
            .title span {
                color: MediumSeaGreen;
            }
            .details {
                padding: 10px 20px 0px 20px;
                text-align: left !important;
                /*margin-left: 40%;*/
            }
            .hrItem {
                border: none;
                height: 1px;
                /* Set the hr color */
                color: #333; /* old IE */
                background-color: #fff; /* Modern Browsers */
            }
            .head {

           padding: 10px;
           margin: 20px;
           margin-top: 60px;
           border-radius: 25px;
            border-style: solid;
    border-color: Purple;
            }
    #footer {
    position:absolute;
    bottom:0;
    width:100%;
    height:60px;   /* Height of the footer */
    background:#6cf;
    margin: 50px
    }

        </style>
    </head>
    <body >
        <div  class='wrapper'>
            <div class='header'>
                <img src="https://gersep.pythonanywhere.com/static/images/GERSEP.jpg" alt="logo" style="height :50px; width: 50px; margin: 5px">
                <img src="https://gersep.pythonanywhere.com/static/images/isref.png" alt="logo" style="height :50px; width: 50px;  margin: 5px">
                <img src="https://gersep.pythonanywhere.com/static/images/isscir.jpg" alt="logo" style="height :50px; width: 50px,  margin: 5px">

                <div class="head" style="padding-top: 60px;" >
                    <p class='title' style="color: Black; text-align: center; font-size: 40px; font-family: 'Tangerine', serif;">Graduate Employment and Research Skill Enhancement Project <br> (GERSEP)</p>
                </div>
            </div>
        <div>

            <div id="footer"> <div class='details'>
                <h5 style="text-align: center">This is to certify that <strong style="font-size: 20px"> """+webinar_full_name.get(emails).upper()+""" </strong> participated in the webinar titled <span style='color: Grey'>'DEMYSTIFYING UNEMPLOYMENT FOR A NEW NARRATIVE'</span>.</h5>
                <p style="text-align: center">This day, the 24th of October, 2020</p>
                <br><br> <br><br>
                <p style="text-align: center; font-weight: 1"><span style="font-size: 30px; text-color:Grey; padding-left:20px; margin:20px; "><i style="font-family: Sans-Serif, Arial"><strike>O</strike><i style="font-size: 50px;  "><u>l</u></i><strike>u</strike></i> </span> <br>..................................................<br> Mr. Richard Olumide Daodu <br> <strong>Webinar Coordinator</strong></p>

            <hr class='hrItem' />
                <p style="font-size: 10px"> <a href="">intern@anrescentpub.com </a></p><p style="text-align: right ;font-size: 10px">"""+webinar_code.get(emails) +"""</p>
        </div>
                </div>
        </div>
            </div>

        </body>

        </html>"""
    output_filename = "gersep_webinar.pdf"
    # Utility function
    def convert_html_to_pdf(source_html, output_filename):
        # open output file for writing (truncated binary)
        result_file = open(output_filename, "w+b")
        # convert HTML to PDF
        pisa_status = pisa.CreatePDF(
        source_html, # the HTML to convert
        dest=result_file) # file handle to recieve result
        # close output file
        result_file.close() # close output file
        # return False on success and True on errors
        return pisa_status.err
    # Main program
    if __name__ == "__main__":
        pisa.showLogging()
        convert_html_to_pdf(source_html, output_filename)
        print('pdf done for '+ emails)


    subject = "Gersep Participation Certificate and Materials"
    body = "Kindly find attachment. Cheers."
    sender_email = "management.isscir@gmail.com"
    receiver_email = emails
    password = "jo1r1ch1"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = "intern@anrescentpub.com"  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "gersep_webinar.pdf"  # In same directory as script
    filename1= "first_presentation.pdf"
    filename2= "second_presentation.pptx"

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    with open(filename1, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part1 = MIMEBase("application", "octet-stream")
        part1.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part1)

    # Add header as key/value pair to attachment part
    part1.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename1}",
    )
    with open(filename2, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part2 = MIMEBase("application", "octet-stream")
        part2.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part2)

    # Add header as key/value pair to attachment part
    part2.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename2}",
    )



    # Add attachment to message and convert message to string
    message.attach(part)
    message.attach(part1)
    message.attach(part2)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        print('email sent for '+emails )