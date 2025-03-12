from Address import Address
from Mailing import Mailing

ot = Address(666666, "Воркута", "Ленина", 4, 15)
do = Address(555555, "Курск", "Мира", 13, 11)

package = Mailing(ot,do, 1000, 12345553)

print(package)
