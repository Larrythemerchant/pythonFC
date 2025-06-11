from datetime import datetime, timedelta

# print(datetime.today())
tomorrow = datetime.today() + timedelta(days=30)
# print(tomorrow)

twoja_data_urodzin = input("podaj swoja date urodzin:")
# print(twoja_data_urodzin)
# print(type(twoja_data_urodzin))
data_urodzin_obiekt = datetime.strptime(twoja_data_urodzin, "%d-%m-%Y")
# print(data_urodzin_obiekt)
format_amerykanski = "%m/%d/%Y %H:%M:%S"

obiekt_w_formacie_amerykanskim = datetime.strptime(
    "12/22/2022 12:01:02", format_amerykanski
)
# print(obiekt_w_formacie_amerykanskim)

twoja_data_urodzin_po_amerykansku = datetime.strftime(
    data_urodzin_obiekt, format_amerykanski
)
print(twoja_data_urodzin_po_amerykansku)

# isd_format = datetime.fromisoformat(twoja_data_urodzin)
