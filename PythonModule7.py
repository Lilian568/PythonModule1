#Ex7.1
seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
try:
    month_number = int(input("Enter a month number: "))
except ValueError:
    print("Invalid input. Pleas enter a valid number: ")
    exit()
if 1 <= month_number <= 12:
    season_index = (month_number - 1) //3
    season = seasons [season_index]
    print(f"The season for month {month_number} is {season}.")
else:
    print("Invalid number. Please enter a valid month number. ")

#Ex7.2
names_set = set()
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    if name in names_set:
        print(f"Existing name: {name}")
    else:
        print(f"New name: {name}")
    names_set.add(name)
print("\nList of input name: ")
for name in names_set:
    print(name)

#Ex7.3
airport_data = {}
def add_airport():
    icao_code = input("Enter the ICAO code of the airport: "). strip().upper()
    airport_name = input("Enter the name of the airport: ").strip()
    airport_data[icao_code] = airport_name
    print(f"Airport '(airport_name)' with ICAO code '{icao_code}' has been added. \n")
def fetch_airport():
    icao_code = input("Enter the ICAO code if the airport to fetch information: ").strip().upper()
    if icao_code in airport_data:
        airport_name = airport_data[icao_code]
        print(f"The airport with ICAO code '{icao_code}' is '{airport_name}")
    else:
        print(f"No airport found with ICAO code '{icao_code}'.\n")
while True:
    print("Choose an option. ")
    print("1. Enter a new airport. ")
    print("2. Fetch airport information. ")
    print("3. Quit.")
    choice = input("Enter your choice: "). strip()
    if choice == '1':
        add_airport()
    elif choice == '2':
        fetch_airport()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. please choose a valid option")