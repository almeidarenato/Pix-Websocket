import uuid
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self, base_dir=""):
        # creates payment on the bank institution
        bank_payment_id =  str(uuid.uuid4())  #generate random uuid object and convert to string

        # generates fake hash 
        hash_payment =  f'hash_payment_{bank_payment_id}'

        # generate qr code
        img = qrcode.make(hash_payment) # create imagem for qr_code
        #save image
        img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png") #save image to static folder


        return {"bank_payment_id": bank_payment_id,
                "qr_code_path":f"qr_code_payment_{bank_payment_id}"}