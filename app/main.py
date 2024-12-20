from setup import *
import os


#CRUD FUNCTIONS
#Airline
def add_airline():
    name = input("Enter Airline Name: ").strip()
    email = input("Enter Airline Email: ").strip()
    phone_number = input("Enter Phone Number: ").strip()

    if not name:
        print("Airline name required.")
        return
    if not email:
        print("Airline email required.")
        return
    if not phone_number:
        print("Phone number required.")
        return

    airline = Airline(name=name, email=email, phone_number=phone_number)
    session.add(airline)
    session.commit()
    print("Airline added successfully.")

def view_airline():
    airlines = session.query(Airline).all()
    for airline in airlines:
        print(f"{airline.id} - {airline.name} - {airline.email} - {airline.phone_number}")

def update_airline():
    airline_id = int(input("Enter Airline ID to update: "))
    airline = session.query(Airline).filter_by(id=airline_id).first()
    if airline:
        airline.name = input(f"Enter new name (current: {airline.name}): ").strip() or airline.name
        airline.email = input(f"Enter new email (current: {airline.email}): ").strip() or airline.email
        airline.phone_number = input(f"Enter new Phone Number (current: {airline.phone_number}): ").strip() or airline.phone_number
        session.commit()
        print("Airline updated successfully.")
    else:
        print("Airline not found.")

def delete_airline():
    airline_id = int(input("Enter Airline ID to delete: "))
    airline = session.query(Airline).filter_by(id=airline_id).first()
    if airline:
        session.delete(airline)
        session.commit()
        print("Airline deleted successfully.")
    else:
        print("Airline not found.")

#Destination
def add_destination():
    city = input("Enter City Name: ").strip()
    country = input("Enter Country Name: ").strip()
    airport_code = input("Enter Airport Code: ").strip()
    
    if not city:
        print("City name required.")
        return
    
    destination = Destination(city=city, country=country, airport_code=airport_code)  

    session.add(destination)
    session.commit()
    print("Destination added successfully.")

def view_destinations():
    destinations = session.query(Destination).all()
    for destination in destinations:
        print(f"{destination.id} - {destination.city} - {destination.country} - {destination.airport_code}")

def update_destination():
    destination_id = int(input("Enter Destination ID to update: "))
    destination = session.query(Destination).filter_by(id=destination_id).first()
    
    if destination:
        destination.city = input(f"Enter new City (current: {destination.city}): ").strip() or destination.city
        destination.country = input(f"Enter new Country (current: {destination.country}): ").strip() or destination.country
        destination.airport_code = input(f"Enter new Airport Code (current: {destination.airport_code}): ").strip() or destination.airport_code

        session.commit()
        print("Destination updated successfully.")
    else:
        print("Destination not found.")

def delete_destination():
    destination_id = int(input("Enter Destination ID to delete: "))
    destination = session.query(Destination).filter_by(id=destination_id).first()
    
    if destination:
        session.delete(destination)
        session.commit()
        print("Destination deleted successfully.")
    else:
        print("Destination not found.")  

#Flights
def add_flight():
    flight_number = input("Enter Flight Number: ").strip()
    airline_id = input("Enter Airline ID: ").strip()
    base_location = input("Enter Base Location: ").strip()
    destination_id = input("Enter Destination ID: ").strip()
    flight_date = input("Enter Flight Date (YYYY-MM-DD): ").strip()
    departure_time = input("Enter Departure Time (HH:MM)(AM/PM): ").strip()
    arrival_time = input("Enter Arrival Time (HH:MM)(AM/PM): ").strip()

    if not flight_number:
        print("Flight number cannot be empty.")
        return
    if not airline_id:
        print("Airline ID cannot be empty.")
        return
    if not base_location:
        print("Base location cannot be empty.")
        return
    if not destination_id:
        print("Destination ID cannot be empty.")
        return
    if not flight_date:
        print("Flight date cannot be empty.")
        return
    if not departure_time:
        print("Departure time cannot be empty.")
        return
    if not arrival_time:
        print("Arrival time cannot be empty.")
        return

    flight = Flight(
        flight_number=flight_number,
        airline_id=int(airline_id),
        base_location=base_location,
        destination_id=int(destination_id),
        flight_date=flight_date,
        departure_time=departure_time,
        arrival_time=arrival_time
    )
    session.add(flight)
    session.commit()
    print("Flight added successfully.")

def view_flight():
    flights = session.query(Flight).all()
    for flight in flights:
        print(f"{flight.id} - {flight.flight_number} - {flight.airline_id} - {flight.base_location} - "
              f"{flight.destination_id} - {flight.flight_date} - {flight.departure_time} - {flight.arrival_time}")

def update_flight():
    try:
        flight_id = int(input("Enter Flight ID to update: ").strip())
        flight = session.query(Flight).filter_by(id=flight_id).first()
        if not flight:
            print(f"No flight found with ID: {flight_id}")
            return

        updates = {
            'flight_number': input(f"Enter new flight number (current: {flight.flight_number}): ").strip() or flight.flight_number,
            'airline_id': int(input(f"Enter new airline ID (current: {flight.airline_id}): ").strip() or flight.airline_id),
            'base_location': input(f"Enter new base location (current: {flight.base_location}): ").strip() or flight.base_location,
            'destination_id': int(input(f"Enter new destination ID (current: {flight.destination_id}): ").strip() or flight.destination_id),
            'flight_date': input(f"Enter new flight date (current: {flight.flight_date}): ").strip() or flight.flight_date,
            'departure_time': input(f"Enter new departure time (current: {flight.departure_time}): ").strip() or flight.departure_time,
            'arrival_time': input(f"Enter new arrival time (current: {flight.arrival_time}): ").strip() or flight.arrival_time
        }

        if session.query(Flight).filter_by(flight_number=updates['flight_number'], flight_date=updates['flight_date']).filter(Flight.id != flight.id).first():
            print("Error: A flight with the same flight number and flight date already exists.")
            return

        for key, value in updates.items():
            setattr(flight, key, value)

        session.commit()
        print("Flight updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    

def delete_flight():
    flight_id = int(input("Enter Flight ID to delete: "))
    flight = session.query(Flight).filter_by(id=flight_id).first()
    if flight:
        session.delete(flight)
        session.commit()
        print("Flight deleted successfully.")
    else:
        print("Flight not found.")

#Main CLI App
def main():
    while True:
        os.system('clear')
        print("Welcome to JKIA Flight management")
        print("1. Manage Airline")
        print("2. Manage Destination")
        print("3. Manage Flights")
        main_menu_choice = input("Enter your Choice: ")

        if main_menu_choice == '1':
            while True:
                os.system('clear')
                print("1. Add Airline")
                print("2. View Airline")
                print("3. Update Airline")
                print("4. Delete Airline")
                print("5. Back to Main Menu")
                airline_menu_choice = input("Enter your Choice: ")
                if airline_menu_choice == '1':
                    add_airline()
                elif airline_menu_choice == '2':
                    view_airline()
                elif airline_menu_choice == '3':
                    update_airline()
                elif airline_menu_choice== '4':
                    delete_airline()
                elif airline_menu_choice == '5':
                    break
                input("Press Enter to continue...")
        
        elif main_menu_choice == '2':
            while True:
                os.system('clear')
                print("1. Add Destination")
                print("2. View Destination")
                print("3. Update Destination")
                print("4. Delete Destination")
                print("5. Back to Main Menu")
                destination_menu_choice = input("Enter your Choice: ")
                if destination_menu_choice == '1':
                    add_destination()
                elif destination_menu_choice == '2':
                    view_destinations()
                elif destination_menu_choice == '3':
                    update_destination()
                elif destination_menu_choice == '4':
                    delete_destination()
                elif destination_menu_choice == '5':
                    break
                input("Press Enter to continue...")
        
        elif main_menu_choice == '3':
            while True:
                os.system('clear')
                print("1. Add Flight")
                print("2. View Flight")
                print("3. Update Flight")
                print("4. Delete Flight")
                print("5. Back to Main Menu")
                flight_menu_choice = input("Enter your Choice: ")
                if flight_menu_choice == '1':
                    add_flight()
                elif flight_menu_choice == '2':
                    view_flight()
                elif flight_menu_choice == '3':
                    update_flight()
                elif flight_menu_choice== '4':
                    delete_flight()
                elif flight_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        else:
            print("Invalid choice! Please choose again.")
            input("Press Enter to continue...")


# Call the main function
main()    




