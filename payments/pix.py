import uuid
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        # creates payment on the bank institution
        bank_payment_id =  uuid.uuid4()  #generate random 

        # generates fake hash 
        hash_payment =  f'hash_payment_{bank_payment_id}'

        # generate qr code
        img = qrcode.make(hash_payment) # create imagem for qr_code
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png") #save image to static folder


        return {"payment_bank_id": "",
                "qr_code_path":f"qr_code_payment_{bank_payment_id}"}