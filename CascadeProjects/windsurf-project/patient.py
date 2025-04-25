from database import Database
from utils import (
    validate_name, validate_age, validate_contact,
    print_success, print_error, display_table, generate_id
)

class PatientManager:
    def __init__(self):
        self.db = Database()

    def add_patient(self):
        """Add a new patient to the system."""
        print("\n=== Add New Patient ===")
        
        # Get and validate patient information
        name = input("Enter patient name: ")
        if not validate_name(name):
            print_error("Invalid name format")
            return

        age = input("Enter patient age: ")
        if not validate_age(age):
            print_error("Invalid age")
            return

        gender = input("Enter gender (M/F/O): ").upper()
        if gender not in ['M', 'F', 'O']:
            print_error("Invalid gender")
            return

        contact = input("Enter contact number: ")
        if not validate_contact(contact):
            print_error("Invalid contact number")
            return

        address = input("Enter address: ")
        medical_history = input("Enter medical history (or N/A): ")
        symptoms = input("Enter current symptoms: ")

        patient_data = {
            'id': generate_id(),
            'name': name,
            'age': age,
            'gender': gender,
            'contact': contact,
            'address': address,
            'medical_history': medical_history,
            'symptoms': symptoms,
            'is_critical': 'No'  # Will be updated by AI module
        }

        self.db.save_patient(patient_data)
        print_success(f"Patient added successfully with ID: {patient_data['id']}")

    def search_patient(self):
        """Search for a patient by ID or name."""
        print("\n=== Search Patient ===")
        search_term = input("Enter patient ID or name: ")

        # Try searching by ID first, then by name
        patient = self.db.get_patient(patient_id=search_term)
        if not patient:
            patient = self.db.get_patient(name=search_term)

        if patient:
            headers = ['Field', 'Value']
            data = [[k, v] for k, v in patient.items()]
            display_table(headers, data, f"Patient Information - {patient['name']}")
        else:
            print_error("Patient not found")

    def update_patient(self):
        """Update patient information."""
        print("\n=== Update Patient ===")
        patient_id = input("Enter patient ID: ")
        
        patient = self.db.get_patient(patient_id=patient_id)
        if not patient:
            print_error("Patient not found")
            return

        print("\nCurrent patient information:")
        headers = ['Field', 'Value']
        data = [[k, v] for k, v in patient.items()]
        display_table(headers, data, f"Patient Information - {patient['name']}")

        print("\nEnter new information (press Enter to keep current value):")
        updates = {}
        
        name = input(f"Name [{patient['name']}]: ")
        if name and validate_name(name):
            updates['name'] = name

        age = input(f"Age [{patient['age']}]: ")
        if age and validate_age(age):
            updates['age'] = age

        contact = input(f"Contact [{patient['contact']}]: ")
        if contact and validate_contact(contact):
            updates['contact'] = contact

        address = input(f"Address [{patient['address']}]: ")
        if address:
            updates['address'] = address

        medical_history = input(f"Medical History [{patient['medical_history']}]: ")
        if medical_history:
            updates['medical_history'] = medical_history

        if updates:
            if self.db.update_patient(patient_id, updates):
                print_success("Patient information updated successfully")
            else:
                print_error("Failed to update patient information")
        else:
            print_warning("No changes made")
