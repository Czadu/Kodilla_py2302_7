from faker import Faker
from faker.providers.phone_number import Provider
faker = Faker('pl_PL')


class BaseContact:
   def __init__(self, name, surname, contact, priv_number):
      self.name = name
      self.surname = surname
      self.contact = contact
      self.priv_number = priv_number
   def __str__(self):
      return f"I'm choosing: {self.priv_number} and calling {self.name} {self.surname}"
   @property
   def label_length(self):
      return len(self.name) + len(self.surname)
   

class BusinessContact(BaseContact):
   def __init__(self, job, company, business_number, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.job = job
      self.company = company
      self.business_number = business_number
   def __str__(self):
      return f"I'm choosing: {self.business_number} and calling {self.name} {self.surname}"
   

def create_contacts(type, quantity):
   contacts = []
   for i in range (quantity):
      if type == "personal":   
         name = faker.first_name()
         surname = faker.last_name()
         contact = faker.email()
         priv_num = faker.phone_number()
         person =  {"name": name, "surname": surname, "contact": contact, "private number": priv_num}
         contacts.append(person)
      elif type == "business":
         company = faker.company()
         job = faker.job()
         bus_num = faker.phone_number()
         work =  {"company": company, "job": job, "business number": bus_num}
         contacts.append(work)
   return contacts


private_contacts = create_contacts("personal", 5)
business_contacts = create_contacts("business", 10)

private_dict = dict(zip(range(len(private_contacts)), private_contacts))
business_dict = dict(zip(range(len(business_contacts)), business_contacts))


bc_1 = BusinessContact(name = private_dict[0]["name"], surname = private_dict[0]["surname"], contact = private_dict[0]["contact"], priv_number = private_dict[0]["private number"], job = business_dict[0]["job"], company = business_dict[0]["company"], business_number= business_dict[0]["business number"])

print(bc_1)
print(bc_1.label_length)

