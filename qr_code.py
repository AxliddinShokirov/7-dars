
import segno
def make_qr(link,name):
    qrcode=segno.make_qr(link)
    qrcode.save(
        name+'.png',
        scale=10,
        border=10,
    )


   