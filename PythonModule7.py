#Ex7.1
seasons = ("Winter", "Spring", "Summer", " Fall")
month = int(input("enter a number of month: "))
def season_in_year():
    for number in seasons:
        if month == 12 or 1<= month <= 2:
            return seasons[0]
        elif 3 <= month <= 5:
            return seasons[1]
        elif 6 <= month <= 8:
            return seasons[2]
        elif 9 <= month <= 11:
            return seasons[3]
        else:
            print("Invalid number")
season_in_year()
print(f"month {month} is {season_in_year()}")

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