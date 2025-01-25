from Smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi", "(+79991234567)"),
    Smartphone("Samsung", "S33", "(+79113332211)"),
    Smartphone("Iphone","17 pro max", "(+79009876543)")
]

for Smartphone in catalog:
    print(f"{Smartphone.stamp} - {Smartphone.model}. {Smartphone.nummer}")