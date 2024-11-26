class Apartment:
    def __init__(self, name, is_available=True):
        self.name = name
        self.is_available = is_available

    def __str__(self):
        return f"{self.name} (Available: {self.is_available})"

class RentalSystem:
    def __init__(self):
        self.apartments = []
        self.applications = []

    def add_apartment(self, name):
        """Add a new apartment to the system."""
        apartment = Apartment(name)
        self.apartments.append(apartment)
        print(f"Apartment {name} added successfully.")

    def show_available_apartments(self):
        """Display all available apartments."""
        print("\nAvailable Apartments:")
        for apartment in self.apartments:
            if apartment.is_available:
                print(apartment)
        print()

    def apply(self, applicant_name):
        """Allow a user to apply for the first available apartment."""
        for apartment in self.apartments:
            if apartment.is_available:
                apartment.is_available = False
                self.applications.append((applicant_name, apartment.name))
                print(f"{applicant_name} successfully applied for {apartment.name}.")
                return
        print("No apartments available!")

    def process_application(self):
        """Process the next application in the queue."""
        if not self.applications:
            print("No applications to process.")
            return
        applicant_name, apartment_name = self.applications.pop(0)
        print(f"Processed application: {applicant_name} rented {apartment_name}.")

    def display_menu(self):
        """Display the menu options."""
        print("\n--- Apartment Rental System ---")
        print("1. Add Apartment")
        print("2. Show Available Apartments")
        print("3. Apply for Apartment")
        print("4. Process Application")
        print("5. Exit")
        print("--------------------------------")

def main():
    system = RentalSystem()
    
    while True:
        system.display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            apartment_name = input("Enter apartment name: ").strip()
            system.add_apartment(apartment_name)

        elif choice == "2":
            system.show_available_apartments()

        elif choice == "3":
            applicant_name = input("Enter your name: ").strip()
            system.apply(applicant_name)

        elif choice == "4":
            system.process_application()

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
