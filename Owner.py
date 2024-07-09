class Owner:
    def __init__(self, last_name, first_name, birth_date, email, phone_number, address):
        self.last_name = last_name
        self.first_name = first_name
        self.__birth_date = birth_date
        self.__email = email
        self.phone_number = phone_number
        self.__address = address

    def call_clinic(self):
        print(f"{self.last_name} {self.first_name} calls the clinic. Ring ring!")

    def schedule_animal(self, animal):
        print(f"The owner {self.last_name} {self.first_name} has scheduled the animal {animal}.")

    def pay_bill(self, bill):
        print(f"The owner {self.last_name} {self.first_name} pays the bill amounting to {bill} RON.")

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, new_birth_date):
        self.__birth_date = new_birth_date

    @birth_date.deleter
    def birth_date(self):
        self.__birth_date = None

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @address.deleter
    def address(self):
        self.__address = None

owner_1 = Owner('Lungu', 'Marius', '11.30.2007', 'nu.am.email@yahoo.com', '0723451674', 'Cristian City, Brasov County, Brasov Street, No. 4')

owner_1.call_clinic()
owner_1.schedule_animal(animal='Mitzy')
owner_1.pay_bill(100)

owner_1.email = 'acum.si.eu.am.mail@yahoo.com'
print(owner_1.email)