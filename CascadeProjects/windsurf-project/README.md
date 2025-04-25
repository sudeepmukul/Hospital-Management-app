# Hospital Management System

A command-line interface (CLI) based Hospital Management System designed for small hospitals and clinics to efficiently manage patients and appointments.

## Features

- Patient Management
  - Add new patients
  - Search patients by ID or name
  - Update patient information
  - Automatic critical patient tagging

- Appointment Management
  - Schedule new appointments
  - View daily appointments
  - Generate daily reports (top 10 appointments)

- AI-based Priority System
  - Automatic detection of critical symptoms
  - Priority level assignment
  - Care recommendations

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

## Project Structure

- `main.py`: Main application and CLI interface
- `patient.py`: Patient management functionality
- `appointment.py`: Appointment scheduling and reporting
- `ai_priority.py`: AI-based patient priority system
- `database.py`: Data storage and retrieval
- `utils.py`: Utility functions and validators
- `data/`: Directory for storing patient and appointment data

## Data Privacy

This system implements basic privacy principles aligned with:
- HIPAA guidelines
- India's DISHA framework
- Only necessary patient information is stored
- Data is stored locally in CSV format

## Dependencies

- tabulate: For formatted table output
- pandas: For data handling
- python-dateutil: For date validation
- colorama: For colored terminal output
- rich: For enhanced CLI interface

## Contributing

Feel free to submit issues and enhancement requests.
