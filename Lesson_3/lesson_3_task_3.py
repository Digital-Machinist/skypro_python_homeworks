from address import Address
from mailing import Mailing

mail = Mailing(Address('123321', 'Moscow', 'Pushkina', 12, 321), Address('321123', 'Kazan', 'Kolotushkina', 32, 21), 1050, '123post321')

print(mail.track, 'из', mail.from_address.index, mail.from_address.city, mail.from_address.street, mail.from_address.house, '-', mail.from_address.apart, 'в', mail.to_address.index, mail.to_address.city, mail.to_address.street, mail.to_address.house, '-', mail.to_address.apart,'.', 'Стоимость', mail.cost, 'Рублей')