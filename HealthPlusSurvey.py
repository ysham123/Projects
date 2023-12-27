import sys

class HealthPlus:
    def __init__(self):
        self.agreement_accepted = False
        self.user_info = {"First_name": None,
            "Second_name": None,
            "Date_of_Birth": None,
            "Past_History": None,
            "Family_History": None,
            "Accidents": None,
            "Criminal_Records": None,
            "Phone_Number": None,
            "Email_Address": None,
            "Emergency_Contact": None,
            "Current_Address": None,
            "Permanent_Address": None,
            "Allergies": None,
            "Current_Medications": None,
            "Blood_Type": None,
            "Immunization_Records": None,
            "Chronic_Diseases": None,
            "Mental_Health_History": None,
            "Dietary_Habits": None,
            "Exercise_Habits": None,
            "Smoking_and_Alcohol": None,
            "Sleep_Patterns": None,
            "Insurance_Provider": None,
            "Policy_Number": None,
            "Coverage_Details": None,
            "Primary_Care_Physician": None,
            "Preferred_Hospital": None,
            "Previous_Surgeries": None,
            "Surgical_Dates": None,
            "Surgical_Outcomes": None,
            "Recent_Blood_Tests": None,
            "Diagnostic_Test_Results": None,
            "Medication_Allergies": None,
            "Vaccination_History": None}  # Same as before
        self.symptoms = {"fever": {
        "common cold": ["mild fever", "runny nose", "sore throat"],
        "flu": ["high fever", "body aches", "fatigue"],
        "pneumonia": ["high fever", "productive cough", "chest pain"],
        "COVID-19": ["fever", "loss of taste or smell", "breathing difficulties"],
        "malaria": ["cyclical fever", "chills", "sweating"]
    },
    "headache": {
        "migraine": ["throbbing pain", "nausea", "light sensitivity"],
        "tension headache": ["constant dull ache", "pressure around forehead"],
        "cluster headache": ["severe pain around one eye", "tearing", "nasal congestion"],
        "sinusitis": ["pain around forehead", "nasal discharge", "loss of smell"],
        "dehydration": ["general headache", "dizziness", "dry mouth"]
    },
    "cough": {
        "common cold": ["mild cough", "runny nose", "sore throat"],
        "bronchitis": ["productive cough", "wheezing", "fatigue"],
        "pneumonia": ["persistent cough", "fever", "chest pain"],
        "asthma": ["dry cough", "wheezing", "shortness of breath"],
        "COVID-19": ["dry cough", "fever", "breathing difficulties"]
    },
    "fatigue": {
        "anemia": ["chronic tiredness", "pale skin", "shortness of breath"],
        "thyroid issues": ["tiredness", "weight changes", "mood swings"],
        "sleep disorders": ["daytime sleepiness", "irregular breathing or movement during sleep"],
        "chronic fatigue syndrome": ["prolonged fatigue", "sore throat", "enlarged lymph nodes"],
        "depression": ["persistent fatigue", "feelings of sadness", "loss of interest"]
    },
    "nausea": {
        "food poisoning": ["sudden onset of nausea", "vomiting", "diarrhea"],
        "gastroenteritis": ["nausea", "abdominal cramps", "fever"],
        "pregnancy": ["morning nausea", "vomiting", "food aversions"],
        "migraine": ["nausea", "sensitivity to light and sound", "throbbing headache"],
        "motion sickness": ["nausea", "dizziness", "vomiting during travel"]
    },
    "shortness of breath": {
        "asthma": ["wheezing", "cough", "difficulty in breathing"],
        "COPD": ["persistent cough", "wheezing", "mucus production"],
        "heart failure": ["trouble breathing", "fatigue", "swelling in legs"],
        "pulmonary embolism": ["sudden breathlessness", "chest pain", "coughing up blood"],
        "COVID-19": ["difficulty breathing", "fever", "cough"]
    },
    "chest pain": {
        "heart attack": ["severe chest pain", "nausea", "shortness of breath"],
        "angina": ["chest discomfort", "pain spreading to arms", "nausea"],
        "pneumonia": ["sharp chest pain", "fever", "cough"],
        "gastroesophageal reflux disease (GERD)": ["burning chest pain", "acid taste", "swallowing difficulty"],
        "muscle strain": ["localized pain", "increases with movement or breathing", "muscle tenderness"]
    },
    "abdominal pain": {
        "appendicitis": ["sharp pain in lower right abdomen", "fever", "nausea"],
        "gastroenteritis": ["cramping", "nausea", "vomiting"],
        "irritable bowel syndrome (IBS)": ["cramp-like pain", "bloating", "changes in bowel habits"],
        "ulcers": ["burning stomach pain", "heartburn", "nausea"],
        "kidney stones": ["severe pain in side and back", "nausea", "urination pain"]
    },
    "dizziness": {
        "vertigo": ["spinning sensation", "balance issues", "nausea"],
        "dehydration": ["lightheadedness", "dry mouth", "thirst"],
        "low blood sugar": ["shakiness", "sweating", "hunger"],
        "anemia": ["lightheadedness", "weakness", "pale skin"],
        "migraine": ["spinning sensation", "nausea", "light sensitivity"]
    },
    "rash": {
        "eczema": ["itchy skin", "red patches", "dry skin"],
        "allergic reaction": ["itchy hives", "swelling", "redness"],
        "psoriasis": ["red skin patches with silvery scales", "dry skin", "itching"],
        "ringworm": ["circular rash", "itchiness", "red patches"],
        "measles": ["red or brown blotches", "fever", "cough"]
        },}  # Same as before

    def show_terms_and_services(self):
        print("""
            Hello! Welcome to Virtual Check-in. Before we get started, please read through our terms and services:
            [By using HealthPlus, you agree to be bound by these terms and all applicable laws and regulations. If you do not agree with any part of these terms, you are prohibited from using or accessing this service.

Privacy Policy: Your privacy is important to us. Our Privacy Policy explains how we collect, use, and protect your personal information. Please read it carefully.

User Responsibilities: You are responsible for providing accurate and current information. Any misuse of the service or provision of false information may result in termination of your access.

Service Usage: HealthPlus is intended for personal, non-commercial use. You agree not to misuse the service or help anyone else do so.

Limitations: In no event shall HealthPlus or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the HealthPlus services.

Revisions and Errata: The materials appearing on HealthPlus could include technical, typographical, or photographic errors. We do not warrant that any of the materials on HealthPlus are accurate, complete, or current. We may make changes to the materials contained on HealthPlus at any time without notice.

Links: HealthPlus has not reviewed all of the sites linked to its website and is not responsible for the contents of any such linked site. The inclusion of any link does not imply endorsement by HealthPlus. Use of any such linked website is at the user's own risk.

Modifications of Terms of Service: We may revise these terms of service for HealthPlus at any time without notice. By using this website, you are agreeing to be bound by the then-current version of these terms of service.

Governing Law: Any claim relating to HealthPlus shall be governed by the laws of the jurisdiction in which the service provider is based without regard to its conflict of law provisions. ]
            Please respond with 'Agree' or 'Disagree']
        """)

    def accept_agreement(self):
        user_response = input("Please respond with 'Agree' or 'Disagree': ").strip().lower()
        if user_response == "agree":
            self.agreement_accepted = True
        else:
            print("We can still help you but there will be restrictions")

    def gather_information(self):
        if not self.agreement_accepted:
            print("Agreement not accepted. Unable to proceed with gathering information.")
            return
        
        for key in self.user_info.keys():
            self.user_info[key] = input(f"Enter your {key.replace('_', ' ')}: ")

    def reason_for_visit(self):
        if not self.agreement_accepted:
            print("Agreement not accepted. Unable to proceed with assessing the reason for visit.")
            return None, None

        reason = input("What is your reason for the visit today? ")
        pain_scale = input("Please rank your pain from a scale of 1-10: ")
        return reason, pain_scale

    def severity_of_patient(self, pain_scale):
        if not self.agreement_accepted:
            print("Agreement not accepted. Unable to assess pain severity.")
            return "Unknown"

        try:
            scale = int(pain_scale)
            if 1 <= scale <= 5:
                return "Bearable"
            elif 6 <= scale <= 8:
                return "Pretty Unbearable"
            else:
                return "Unbearable"
        except ValueError:
            print("Invalid input for pain scale. Please enter a number between 1 and 10.")
            return "Invalid Input"

    def breakdown_symptoms(self, user_symptoms):
        if not self.agreement_accepted:
            print("Agreement not accepted. Unable to process symptom breakdown.")
            return

        matched_diseases = []
        for symptom, diseases in self.symptoms.items():
            if symptom in user_symptoms:
                for disease, symptoms in diseases.items():
                    if user_symptoms.issubset(symptoms):
                        matched_diseases.append(disease)

        if matched_diseases:
            print("Based on your symptoms, you may have the following condition(s):")
            for disease in set(matched_diseases):
                print(f"- {disease}")
        else:
            print("We could not match your symptoms to a specific condition.")

    def save_patient_info(self, file_name, user_symptoms):
        if not self.agreement_accepted:
            print("Agreement not accepted. Unable to save patient information.")
            return

        try:
            with open(file_name, 'w') as file:
                file.write("User Information:\n")
                for key, value in self.user_info.items():
                    file.write(f"{key.replace('_', ' ')}: {value}\n")
                file.write("\nDiagnosis based on symptoms:\n")
                for symptom in user_symptoms:
                    file.write(f"- {symptom}\n")
        except IOError as e:
            print(f"Error saving file: {e}")

def main():
    health_app = HealthPlus()
    health_app.show_terms_and_services()
    health_app.accept_agreement()

    if health_app.agreement_accepted:
        health_app.gather_information()
        reason, pain_scale = health_app.reason_for_visit()
        pain_severity = health_app.severity_of_patient(pain_scale)

        user_input = input("What symptoms are you feeling? Please separate them with commas.\n").lower()
        user_symptoms = {symptom.strip() for symptom in user_input.split(',')}
        
        health_app.breakdown_symptoms(user_symptoms)
        health_app.save_patient_info('user_health_report.txt', user_symptoms)
    else:
        print("User did not agree to the terms. Exiting program.")

if __name__ == "__main__":
    main()
