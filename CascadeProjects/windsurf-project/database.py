import csv
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.data_dir = "data"
        self.patients_file = os.path.join(self.data_dir, "patients.csv")
        self.appointments_file = os.path.join(self.data_dir, "appointments.csv")
        self._initialize_data_files()

    def _initialize_data_files(self):
        """Initialize data directory and files if they don't exist."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        # Initialize patients.csv
        if not os.path.exists(self.patients_file):
            with open(self.patients_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'name', 'age', 'gender', 'contact', 'address', 'medical_history', 'symptoms', 'is_critical'])

        # Initialize appointments.csv
        if not os.path.exists(self.appointments_file):
            with open(self.appointments_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'patient_id', 'date', 'time', 'doctor', 'purpose', 'status'])

    def save_patient(self, patient_data):
        """Save patient data to CSV."""
        with open(self.patients_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                patient_data['id'],
                patient_data['name'],
                patient_data['age'],
                patient_data['gender'],
                patient_data['contact'],
                patient_data['address'],
                patient_data['medical_history'],
                patient_data['symptoms'],
                patient_data['is_critical']
            ])

    def get_patient(self, patient_id=None, name=None):
        """Retrieve patient data by ID or name."""
        with open(self.patients_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if (patient_id and row['id'] == patient_id) or \
                   (name and row['name'].lower() == name.lower()):
                    return row
        return None

    def save_appointment(self, appointment_data):
        """Save appointment data to CSV."""
        with open(self.appointments_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                appointment_data['id'],
                appointment_data['patient_id'],
                appointment_data['date'],
                appointment_data['time'],
                appointment_data['doctor'],
                appointment_data['purpose'],
                appointment_data['status']
            ])

    def get_daily_appointments(self, date):
        """Get all appointments for a specific date."""
        appointments = []
        with open(self.appointments_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['date'] == date:
                    appointments.append(row)
        return appointments

    def update_patient(self, patient_id, updated_data):
        """Update patient information."""
        rows = []
        updated = False
        with open(self.patients_file, 'r') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            for row in reader:
                if row['id'] == patient_id:
                    row.update(updated_data)
                    updated = True
                rows.append(row)

        if updated:
            with open(self.patients_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(rows)
        return updated
