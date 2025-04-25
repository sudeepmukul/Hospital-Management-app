import re
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

def validate_name(name):
    """Validate that name contains only letters and spaces."""
    if not name or not re.match(r'^[A-Za-z\s]+$', name):
        return False
    return True

def validate_age(age):
    """Validate age is a number between 0 and 150."""
    try:
        age = int(age)
        return 0 <= age <= 150
    except ValueError:
        return False

def validate_contact(contact):
    """Validate contact number format."""
    if not contact or not re.match(r'^\+?[\d\s-]{10,}$', contact):
        return False
    return True

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_time(time_str):
    """Validate time format (HH:MM)."""
    try:
        datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def display_table(headers, data, title):
    """Display data in a formatted table using Rich."""
    table = Table(title=title)
    
    # Add headers
    for header in headers:
        table.add_column(header, style="cyan")
    
    # Add rows
    for row in data:
        table.add_row(*[str(item) for item in row])
    
    console.print(table)

def generate_id():
    """Generate a unique ID based on timestamp."""
    return datetime.now().strftime('%Y%m%d%H%M%S')

def print_success(message):
    """Print success message in green."""
    console.print(f"✓ {message}", style="green")

def print_error(message):
    """Print error message in red."""
    console.print(f"✗ {message}", style="red")

def print_warning(message):
    """Print warning message in yellow."""
    console.print(f"! {message}", style="yellow")
