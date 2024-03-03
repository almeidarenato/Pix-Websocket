# add all folders of the root of the project
import sys
sys.path.append("..") # previous folder

from payments.pix import Pix
import pytest
import os 
 

def test_pix_create_payment():
    pix_instance = Pix()

    # create a payment
    payment_info = pix_instance.create_payment(base_dir="../")

    print(payment_info)

    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info

    qr_code_path = payment_info["qr_code_path"]
    
    assert os.path.isfile(f"../static/img/{qr_code_path}.png")