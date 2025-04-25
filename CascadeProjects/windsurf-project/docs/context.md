🧠 WindSurf Project Context Prompt:

You are helping me build a Command-Line Interface (CLI)-based Hospital Management System in Python. This system is intended for a small hospital or clinic to manage patients and appointments efficiently. Here's everything you need to know:

🏥 Project Overview: Build a CLI-based app that allows hospital staff to:

Add, view, update, and search patient records

Schedule appointments

Tag critical patients based on symptoms

Generate a daily report of 10 scheduled appointments

Validate all inputs (no blanks, proper name/date formats)

Display clean, readable output (tables or sections)

📁 Project Modules:

main.py: CLI flow

patient.py: Add, view, update, search patient records

appointment.py: Schedule & report appointments

ai_priority.py: Tag critical patients using symptom keywords or AI logic

utils.py: Validators for names, age, date, etc.

database.py: Handle SQLite or CSV storage

data/: Folder for patient and appointment data

🧠 AI Use:

Optionally use AI or keyword rules to auto-tag patients as “Critical” based on symptom inputs like “chest pain”, “difficulty breathing”, etc.

🔐 Privacy & Best Practices:

Implement basic privacy principles (e.g., only necessary fields stored)

Reference international standards like HIPAA and India’s DISHA framework for privacy documentation

📐 Design/UI Inspiration: Follow the layout and structure from the screenshot I’ve provided. Use it as a reference for how the CLI should flow or how the final UI might look in a future version.

💡 Guidelines:

Use readable prompts for CLI input

Output in clean tables (tabulate preferred)

All actions should return confirmation or appropriate feedback

Be modular—functions should be reusable across modules

When I give you tasks (like “add appointment scheduler”), break them into logical functions and help with clean, readable Python code.

Let me know if you need more clarification or when I upload a design reference.

Feel free to adapt this if your screenshot shows more UI features—like color or layout cues. If you'd like, I can also write a specific WindSurf command example like:

"Based on this project context, generate a function in patient.py to search patients by name or ID from a CSV file and return their info in table format."