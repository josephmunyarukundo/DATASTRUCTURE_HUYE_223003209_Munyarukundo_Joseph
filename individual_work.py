from collections import deque

class CarRentalSystem:
    def __init__(self):
        self.available_cars = ['Toyota Corolla','Honda Civic','Ford Focus']    
        self.rental_requests = deque() 
        self.undo_stack = []          


    def request_rental(self, customer_name, car):
        if car in self.available_cars:
            self.rental_requests.append((customer_name, car))
            print(f"Rental request from {customer_name} for car: {car}")
        else:
            print(f"Car {car} is not available.")

    def process_rental_request(self):
        if self.rental_requests:
            customer_name, car = self.rental_requests.popleft()
            self.available_cars.remove(car) 
            self.undo_stack.append((customer_name, car))
            print(f"{customer_name} rented car: {car}")
        else:
            print("No rental requests to process.")

    def undo_rental(self):
        if self.undo_stack:
            customer_name, car = self.undo_stack.pop()
            self.available_cars.append(car) 
            print(f"Rental undone: {customer_name} returned car: {car}")
        else:
            print("No rentals to undo.")

    def show_available_cars(self):
        print("Available cars:", self.available_cars)

    def show_rental_requests(self):
        print("Rental Requests:")
        for request in self.rental_requests:
            print(request)

if __name__ == "__main__":
    rental_system = CarRentalSystem()

    def menu():
        while True:
            print("\n1. Show available Cars.")
            print("2. Rental_request.")
            print("3. show process rental request.")
            print("4. returned car.")
            print("5. show remain car.")
            print("6. EXIT.")
            choice=input("\nChoose an option (1 up to 6):")
            if choice=='1':
                rental_system.show_available_cars()
            elif choice=='2':
                try:
                    customer_name = input("Enter your name: ")
                    car=input("Enter car you want to rent: ")
                    rental_system.request_rental( customer_name, car)
                except ValueError:
                    print("Invalid input. please try again.")
            elif choice=='3':
                rental_system.process_rental_request()
            elif choice=='4':
                rental_system.undo_rental()
            elif choice=='5':
                rental_system.show_available_cars()
            elif choice=='6':
                print("\nExiting the system. Good byeee..!!!")
                break
            else:
                print("\nInvalid option. Please select a valid option.")
    menu()