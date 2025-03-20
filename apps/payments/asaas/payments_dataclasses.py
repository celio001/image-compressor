from dataclasses import dataclass
from typing import Optional

@dataclass
class CreditCard:
    holderName: str
    number: str
    expireMonth: str
    expiryYear: str
    ccv: str

    def __post_init__(self):
        self.validate_number()
        self.validate_ccv()

    def validate_ccv(self):
        if len(self.ccv) != 3:
            raise ValueError('CCV inválido, deve conter 3 digitos')


@dataclass
class CreditCardHolderInfo:
    name: str
    email: str
    cpfCnpj: str
    postalCode: str
    addressNumber: str
    phone: str
    addressComplement: Optional[str] = ''
    mobilePhone: Optional[str] = ''

    def __post_init__(self):
        self.validate_cpfCnpj()

    def validate_cpfCnpj(self):
        if len(self.cpfCnpj) != 11 and len(self.cpfCnpj) != 14:
            raise ValueError('CPF/CNPJ inválido')