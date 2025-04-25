from database import Database
from utils import (
    validate_date, validate_time, print_success,
    print_error, display_table, generate_id
)
from datetime import datetime

class AppointmentManager:
    def __init__(self):
        self.db = Database()

    def schedule_appointment(self):
        """Schedule a new appointment."""
        print("\n=== Schedule Appointment ===")
        
        patient_id = input("Enter patient ID: ")
        patient = self.db.get_patient(patient_id=patient_id)
        if not patient:
            print_error("Patient not found")
            return

        date = input("Enter appointment date (YYYY-MM-DD): ")
        if not validate_date(date):
            print_error("Invalid date format")
            return

        time = input("Enter appointment time (HH:MM): ")
        if not validate_time(time):
            print_error("Invalid time format")
            return

        doctor = input("Enter doctor name: ")
        purpose = input("Enter appointment purpose: ")

        appointment_data = {
            'id': generate_id(),
            'patient_id': patient_id,
            'date': date,
            'time': time,
            'doctor': doctor,
            'purpose': purpose,
            'status': 'Scheduled'
        }

        self.db.save_appointment(appointment_data)
        print_success("Appointment scheduled successfully")

    def view_daily_appointments(self, specific_date=None):
        """View appointments for a specific date."""
        if specific_date is None:
            date = input("Enter date to view appointments (YYYY-MM-DD) or press Enter for today: ")
            if not date:
                date = datetime.now().strftime('%Y-%m-%d')
            elif not validate_date(date):
                print_error("Invalid date format")
                return
        else:
            date = specific_date

        appointments = self.db.get_daily_appointments(date)
        if appointments:
            headers = ['Time', 'Patient ID', 'Doctor', 'Purpose', 'Status']
            data = [
                [apt['time'], apt['patient_id'], apt['doctor'], apt['purpose'], apt['status']]
                for apt in appointments
            ]
            display_table(headers, data, f"Appointments for {date}")
        else:
            print_warning(f"No appointments scheduled for {date}")

    def generate_daily_report(self):
        """Generate a report of today's appointments."""
        today = datetime.now().strftime('%Y-%m-%d')
        print("\n=== Daily Appointments Report ===")
        print(f"Date: {today}")
        
        appointments = self.db.get_daily_appointments(today)
        if appointments:
            # Sort appointments by time
            appointments.sort(key=lambda x: x['time'])
            
            # Take only first 10 appointments
            appointments = appointments[:10]
            
            headers = ['Time', 'Patient ID', 'Doctor', 'Purpose', 'Status']
            data = [
                [apt['time'], apt['patient_id'], apt['doctor'], apt['purpose'], apt['status']]
                for apt in appointments
            ]
            display_table(headers, data, f"Today's Appointments ({today})")
        else:
            print_warning("No appointments scheduled for today")
