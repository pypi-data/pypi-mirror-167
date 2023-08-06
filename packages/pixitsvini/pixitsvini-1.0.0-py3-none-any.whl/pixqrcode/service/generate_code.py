from pixqrcode.model.merchant_account import MerchantAccount
from pixqrcode.model.pix import Pix
from pixqrcode.utils.crc16 import crc16

class GenerateCode:
    def __init__(self):
        self.merchant = MerchantAccount()

    def left_zero(self, text: str):
        return str(len(text)).zfill(2)

    def generate(self, pix: Pix):
        sizesum = len(pix.mobile) + len(self.merchant.globally_unique_identifier) + 8
        qr = f"00020101021226{str(sizesum)}00{str(len(self.merchant.globally_unique_identifier))}{self.merchant.globally_unique_identifier}01{str(len(pix.mobile))}{pix.mobile}520400005303986540" \
        f"{len(pix.amount.__str__())}{pix.amount.__str__()}5802{pix.country_code}59{self.left_zero(pix.name)}" \
            f"{pix.name}60{self.left_zero(pix.city)}{pix.city}" \
            f"62{str(len(pix.reference_label) + 4).zfill(2)}05{self.left_zero(pix.reference_label)}" \
            f"{pix.reference_label}6304"
        return qr

    def crc16code(self, query: str) -> str:
        return hex(crc16(query.encode())).__str__()

    def format_code(self, pix: Pix):
        hash_payment = self.generate(pix)
        return f"{hash_payment}{self.crc16code(hash_payment).upper()[2:]}".strip()