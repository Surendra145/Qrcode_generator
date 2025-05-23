import qrcode
import os  # <-- Add this

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()

# Automatically add .png if user forgets
if not filename.lower().endswith('.png'):
    filename += '.png'

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)

print(f'QR code saved as {filename}')

# Automatically open the QR code image
os.startfile(filename)  # <-- Add this
