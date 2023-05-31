from swiplserver import PrologMQI, PrologThread

# A collection of all symptoms, whether the program has asked if the patient had the symptom yet, whether the patient has the symptom, and how that symptom is described when asking the patient whether they have it
symptoms = {
    "hFever" : [False, False, "high fever"],		
    "lFever" : [False, False, "low fever"],	
    "lTemp"	: [False, False, "lower body temperature than normal"],	

    "headache": [False, False, "headaches"],		
    "fatigue" : [False, False, "fatigue"],		
    "malaise" : [False, False, "malaise"],	

    "nausea" : [False, False, "nausea"],		
    "vomiting": [False, False, "vomiting"],		
    "diarrhea" : [False, False, "diarrhea"],	
    "dehydration": [False, False, "dehydration"],
    "sweat"	: [False, False, "heavy sweating"],	
    "nSweat" : [False, False, "night sweats"],	
    "chills" : [False, False, "chills"],		
    "rashes" : [False, False, "rashes"],	
    "bPain": [False, False, "pain in breathing"],		
    "sBreath": [False, False, "shortness of breath"], 		
    "sGlands": [False, False, "swollen glands"],		

    "pCough": [False, False, "cough with phlegm"],		
    "dCough": [False, False, "dry cough"],		
    "wheezing": [False, False, "wheezing"],		
    "sThroat": [False, False, "sore throat"],		

    "aPain" : [False, False, "abdominal pain"],	
    "mPain": [False, False, "muscle pain"],
    "cPain" : [False, False, "chest pain"],		
    "jPain"	: [False, False, "joint pain"],	
    "ePain": [False, False, "pain behind the eyes"],

    "aLoss" : [False, False, "apetite loss"],		
    "wLoss" : [False, False, "weight loss"],		

    "nBleed" : [False, False, "nose bleeds"],	
    "cBlood": [False, False, "coughing blood"],	

    "pale" : [False, False, "paleness"],	
    "jaundice" : [False, False, "jaundice"],	
    "rEyes"	: [False, False, "red eyes"],	
    "pBlood" : [False, False, "blood in urine"],
    "bSkin"	: [False, False, "blue skin"],
    "hallucinations" : [False, False, "hallucinations"],	
    "sunken": [False, False, "sunken eyes"],
    "lPressure": [False, False, "low blood pressure"],

    "hydrophobia" : [False, False, "hydrophobia"],
    "anxiety" : [False, False, "anxiety"],
    "agitation"	: [False, False, "agitation"],	

    "rabBite" : [False, False, "being bitten by a rabid animal"],		

    "flood" : [False, False, "being in contact with flood water"],
    "wound"	: [False, False, "having an open wound"],

    "unsafe" : [False, False, "drinking unsafe water"],	
    "unsanitary" : [False, False, "living in an unsanitary condition"],		

    "multiple" : [False, False, "having multiple sexual partners"],
    "partnerHBV" : [False, False, "having a partner that has Hepatitis B"],
    "shared" : [False, False, "sharing needles, syringes, or drug equipment"],
    "nhbv" : [False, False, "being unvaccinated with Hepatitis B"],
    "darkUrine" : [False, False, "having dark urine"]
}

class disease():
    # Required symptoms of a disease are symptoms that the patient MUST exhibit in order for the program to possibly diagnose them with that disease
    # Optional symptoms are symtoms where the disease may still be diagnosable even if the symptom is not present
    def __init__(self, requiredSymptoms, optionalSymptoms):
        self.requiredSymptoms = requiredSymptoms
        self.optionalSymptoms = optionalSymptoms

    def ask(self):
        # if we know the patient does not have at least 1 of the required symptoms, skip this disease
        for s in self.requiredSymptoms:
            if symptoms[s][0] == True and symptoms[s][1] == False:
                return 

        for s in self.requiredSymptoms:
            # if symptom not yet asked
            if symptoms[s][0] == False: 
                print(f"Have you experienced {symptoms[s][2]} recently? ", end="")
                symptoms[s][0] = True

                ans = input().rstrip()
                if ans.lower() == 'y' or ans.lower() == 'yes':
                    symptoms[s][1] = True
                else:
                    return
        
        for s in self.optionalSymptoms:
            if symptoms[s][0] == False: 
                print(f"Have you experienced {symptoms[s][2]} recently? ", end="")
                symptoms[s][0] = True

                ans = input().rstrip()
                if ans.lower() == 'y' or ans.lower() == 'yes':
                    symptoms[s][1] = True


# Initialize diseases
dengueFeverRequired = ["hFever", "nBleed", "pale", "malaise"]
dengueFeverOptional = ["jPain", "mPain", "aPain", "nausea", "vomiting", "rashes", "ePain", "sGlands"]

malariaRequired = ["hFever", "malaise", "chills", "sweat", "jaundice"]
malariaOptional = ["jPain", "mPain", "aPain", "nausea", "vomiting", "diarrhea"]

tubercolosisRequired = ["lFever", "fatigue", "chills", "nSweat", "cBlood", "cPain", "bPain"]
tubercolosisOptional = ["wLoss", "aLoss", "pCough", "dCough"]

leptospirosisRequired = ["wound", "flood", "hFever", "headache", "chills", "diarrhea", "vomiting", "rEyes", "rashes", "sBreath"]
leptospirosisOptional = ["mPain", "aPain", "cBlood", "pBlood", "jaundice"]

typhoidFeverRequired = ["hFever", "chills", "headache", "aPain"]
typhoidFeverOptional = ["jPain", "mPain", "diarrhea", "nausea", "vomiting", "dCough", "aLoss", "rashes"]

hepatitisBRequired = ["multiple", "partnerHBV", "shared", "nhbv", "lFever", "fatigue", "jPain"]
hepatitisBOptional = ["nausea", "vomiting", "aPain", "jaundice", "darkUrine", "wLoss", "aLoss"]

rabiesRequired = []
rabiesOptional = ["hFever", "fatigue", "headache", "rabBite", "hallucinations", "hydrophobia", "anxiety", "agitation"]

pneumoniaRequired = ["aLoss", "sBreath", "mPain", "cPain"]
pneumoniaOptional = ["pCough", "dCough", "hFever", "lFever", "lTemp", "chills", "fatigue", "malaise", "bSkin", "wheezing"]

influenzaRequired = ["lFever", "headache", "sThroat"]
influenzaOptional = ["dCough", "mPain", "jPain"]

choleraRequired = ["dehydration", "diarrhea"]
choleraOptional = ["unsafe", "unsanitary", "nausea", "vomiting", "sunken", "aPain", "lPressure"]

diseases = []
diseases.append(disease(dengueFeverRequired, dengueFeverOptional))
diseases.append(disease(malariaRequired, malariaOptional))
diseases.append(disease(tubercolosisRequired, tubercolosisOptional))
diseases.append(disease(leptospirosisRequired, leptospirosisOptional))
diseases.append(disease(typhoidFeverRequired, typhoidFeverOptional))
diseases.append(disease(hepatitisBRequired, hepatitisBOptional))
diseases.append(disease(rabiesRequired, rabiesOptional))
diseases.append(disease(pneumoniaRequired, pneumoniaOptional))
diseases.append(disease(influenzaRequired, influenzaOptional))
diseases.append(disease(choleraRequired, choleraOptional))


# start program
ln = "------------------------\n"
print(ln + "MEDICAL DIAGNOSIS SYSTEM\n" + ln)
print("The only valid answers to questions are 'y', 'yes', 'n', and 'no')\n")

# get patient's symptoms
finalSymptoms = ""
for d in diseases:
    d.ask()

for s in symptoms:
    if symptoms[s][1] == True:
        finalSymptoms += ', ' + s

if finalSymptoms != "":
    finalSymptoms = '[' + finalSymptoms[2:]
else:
    finalSymptoms = '[' 

finalSymptoms += ']'

# query knowledge base
print()

if finalSymptoms == '[]':
    print("DIAGNOSIS: YOU ARE HEALTHY")
else:
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread: 
            prolog_thread.query("consult('kb.pl').")
            result = prolog_thread.query("diagnose(" + finalSymptoms + ", Diseases).")


if finalSymptoms != '[]':
    if result == False:
        print("DIAGNOSIS: REFER TO A LARGE MEDICAL FACILITY")
    else:
        print("DIAGNOSIS: YOU HAVE ", end="")
        diagnosis = result[0]["Diseases"]
        if len(diagnosis) == 1:
            for word in diagnosis[0].upper().split('_'):
                print(word + " ", end="")
        else:
            for d in range(len(diagnosis) - 1):
                for word in diagnosis[d].upper().split('_')[:-1]:
                    print(word + ' ', end="")
                print(diagnosis[d].upper().split('_')[len(diagnosis[d].upper().split('_')) - 1], end = "")
                print(', ', end="")
            print('AND ', end="")
            for word in diagnosis[-1].upper().split('_'):
                print(word + ' ', end="")
