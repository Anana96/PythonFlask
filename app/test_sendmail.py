import app.send
import app.pdata

def test():
    sender = app.send.Sender()
    html_text = """
           <html>
               <body>
                    <h1>Test</h1>
                </body>
            </html>"""

    sender.send_via_smtp(email_from_smtp=app.pdata.from_smtp,
                         key= app.pdata.from_key,
                         email_from= app.pdata.from_email,
                         email_to=app.pdata.to_email,
                         subject="письмо из flask",
                         html_text=html_text,
                         plain_text="TEST TEST TEST",
                         cid_images=[],
                         attachments=[])

    app.send.test()


if __name__ == '__main__':
    test()