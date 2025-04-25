from rich.console import Console
from rich.panel import Panel
from patient import PatientManager
from appointment import AppointmentManager
from ai_priority import PriorityAnalyzer

console = Console()

class HospitalManagementSystem:
    def __init__(self):
        self.patient_manager = PatientManager()
        self.appointment_manager = AppointmentManager()
        self.priority_analyzer = PriorityAnalyzer()

    def display_menu(self):
        """Display the main menu of the system."""
        console.print(Panel.fit(
            "[bold cyan]Hospital Management System[/bold cyan]\n\n"
            "1. Add New Patient\n"
            "2. Search Patient\n"
            "3. Update Patient Information\n"
            "4. Schedule Appointment\n"
            "5. View Daily Appointments\n"
            "6. Generate Daily Report\n"
            "7. Exit",
            title="Main Menu",
            border_style="blue"
        ))

    def run(self):
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-7): ")

            if choice == '1':
                self.patient_manager.add_patient()
            elif choice == '2':
                self.patient_manager.search_patient()
            elif choice == '3':
                self.patient_manager.update_patient()
            elif choice == '4':
                self.appointment_manager.schedule_appointment()
            elif choice == '5':
                self.appointment_manager.view_daily_appointments()
            elif choice == '6':
                self.appointment_manager.generate_daily_report()
            elif choice == '7':
                console.print("\n[green]Thank you for using Hospital Management System![/green]")
                break
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")

            input("\nPress Enter to continue...")

if __name__ == "__main__":
    hospital_system = HospitalManagementSystem()
    hospital_system.run()
