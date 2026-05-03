import qrcode

name=input("enter name:")
amount=int(input("enter amount:"))
note=input("enter note(optional):")

payment_data=f"upi://pay?pa={name}@bank&pn={name}&am={amount}&cu=PKR&tn={note}"
qr=qrcode.make(payment_data)
qr.save("qrcode.jpg")
