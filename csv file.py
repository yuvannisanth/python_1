import csv


# Patient class definition
class Patient:
    def __init__(self, patient_id, name, age, gender, address, phone, email, medical_history, appointments, file_path):
        self.patient_id = patient_id

        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email
        self.medical_history = medical_history
        self.appointments = appointments
        self.file_path = file_path

    def print_details(self):
        # Print patient details to console
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print("Medical History:")
        print(f"  Conditions: {', '.join(self.medical_history['conditions'])}")
        print(f"  Allergies: {', '.join(self.medical_history['allergies'])}")
        print(f"  Medications: {', '.join(self.medical_history['medications'])}")
        print("Appointments:")
        for appt in self.appointments:
            print(f"  Date: {appt['date']}, Time: {appt['time']}, Doctor: {appt['doctor']}")

        # Save patient details to a CSV file
        try:
            # Ensure the directory exists

            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Field', 'Value'])
                writer.writerow(['Name', self.name])
                writer.writerow(['Age', self.age])
                writer.writerow(['Gender', self.gender])
                writer.writerow(['Address', self.address])
                writer.writerow(['Phone', self.phone])
                writer.writerow(['Email', self.email])
                writer.writerow(['Conditions', ', '.join(self.medical_history['conditions'])])
                writer.writerow(['Allergies', ', '.join(self.medical_history['allergies'])])
                writer.writerow(['Medications', ', '.join(self.medical_history['medications'])])
                for appt in self.appointments:
                    writer.writerow(
                        [f"Appointment on {appt['date']}", f"Time: {appt['time']}, Doctor: {appt['doctor']}"])
            print(f"CSV file created at {self.file_path}")
        except PermissionError:
            print(f"Permission denied: Unable to write to {self.file_path}.")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}.")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")


# Patient database
patient_database = {
    'patient_001': {
        'name': 'John Doe',
        'age': 45,
        'gender': 'Male',
        'address': '123 Elm Street, Springfield',
        'phone': '555-1234',
        'email': 'john.doe@example.com',
        'medical_history': {
            'conditions': ['Hypertension', 'Diabetes'],
            'allergies': ['Penicillin'],
            'medications': ['Lisinopril', 'Metformin']
        },
        'appointments': [
            {'date': '2024-09-15', 'time': '10:00', 'doctor': 'Dr. Smith'},
            {'date': '2024-10-01', 'time': '11:00', 'doctor': 'Dr. Adams'}
        ]
    },
    'patient_002': {
        'name': 'Jane Smith',
        'age': 34,
        'gender': 'Female',
        'address': '456 Oak Avenue, Springfield',
        'phone': '555-5678',
        'email': 'jane.smith@example.com',
        'medical_history': {
            'conditions': ['Asthma'],
            'allergies': ['None'],
            'medications': ['Albuterol']
        },
        'appointments': [
            {'date': '2024-09-20', 'time': '14:00', 'doctor': 'Dr. Lee'}
        ]
    }
}


def main():
    user_detail = input("ENTER THE PATIENT ID: ").strip()

    # Check if patient_id exists in the database
    if user_detail in patient_database:
        patient_data = patient_database[user_detail]
        file_path = r'E:\csvfile.txt'  # Update the path as needed
        try:
            patient = Patient(
                patient_id=user_detail,
                name=patient_data['name'],
                age=patient_data['age'],
                gender=patient_data['gender'],
                address=patient_data['address'],
                phone=patient_data['phone'],
                email=patient_data['email'],
                medical_history=patient_data['medical_history'],
                appointments=patient_data['appointments'],
                file_path=file_path
            )
            patient.print_details()
        except TypeError as e:
            print(f"Missing data in the patient record: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Patient ID not found in the database.")
main()
