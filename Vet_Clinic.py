from Owner import Owner
from Animal import Animal

class VeterinaryClinic:
    CONSULT_PRICE = 50
    VACCINE_PRICE = 70
    GROOMING_PRICE = 30

    def __init__(self, name, address, phone_number, establishment_date, bank_account, animal_visits):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self._establishment_date = establishment_date
        self._bank_account = bank_account
        self.animal_visits = animal_visits

    def consult_animal(self, owner, animal):
        print(f"{owner.last_name} {owner.first_name} came with the animal {animal} for a routine check-up.")

    @classmethod
    def calculate_bill(cls, owner_name, Consult, Vaccine, Grooming):
        total_bill = Consult * cls.CONSULT_PRICE + Vaccine * cls.VACCINE_PRICE + Grooming * cls.GROOMING_PRICE
        print(f"The owner {owner_name} has to pay a bill of {total_bill} lei.")

    @staticmethod
    def restock_medicines():
        print("The stock of medicines has been restocked.")

Dr_Lungu = VeterinaryClinic('Dr.Lungu', 'Papucesti, Covasna County', '0723862785', '03.14.2017', 'ROXXXX4502', '3')
Owner_2 = Owner('Popescu', 'Maria', '05.15.2000', 'eu.am.mail@yahoo.com', '0758492010', 'Bucharest, Bucharest Street, No. 5')

Dr_Lungu.consult_animal(Owner_2, 'Azorel')

print(f"Bill for the owner {Owner_2.last_name}:")
Consult = 1  # Number of consultations
Vaccine = 1   # Number of vaccines
Grooming = 1  # Number of groomings
VeterinaryClinic.calculate_bill(Owner_2.last_name, Consult, Vaccine, Grooming)

VeterinaryClinic.restock_medicines()