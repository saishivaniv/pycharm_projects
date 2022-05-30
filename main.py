import pyqrcode

def qr_code():
    s = 'This is Python Programming'
    d = pyqrcode.create(s)
    d.png('my_img.png',scale=8)
    print('EXECUTED!!!!')

if __name__ == '__main__':
    qr_code()