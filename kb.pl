% Dengue fever
has_disease(Symptoms, dengue_fever) :-
  member(hFever, Symptoms),
  ((member(jPain, Symptoms) ; member(mPain, Symptoms) ; member(aPain, Symptoms))),
  member(nBleed, Symptoms),
  member(pale, Symptoms),
  member(malaise, Symptoms),
  (member(nausea, Symptoms) ; member(vomiting, Symptoms)),
  (member(rashes, Symptoms) ; member(ePain, Symptoms) ; member(sGlands, Symptoms)).

% Malaria
has_disease(Symptoms, malaria) :-
  member(hFever, Symptoms),
  (member(jPain, Symptoms) ; member(mPain, Symptoms) ; member(aPain, Symptoms)),
  (member(nausea, Symptoms) ; member(vomiting, Symptoms) ; member(diarrhea, Symptoms)),
  member(malaise, Symptoms),
  member(chills, Symptoms),
  member(sweat, Symptoms),
  member(jaundice, Symptoms).

% Tuberculosis
has_disease(Symptoms, tuberculosis) :-
  member(lFever, Symptoms),
  member(fatigue, Symptoms),
  member(chills, Symptoms),
  member(sweat, Symptoms),
  ((member(wLoss, Symptoms) ; member(aLoss, Symptoms)) ; member(pCough, Symptoms) ; member(dCough, Symptoms)),
  member(cBlood, Symptoms),
  member(cPain, Symptoms),
  member(bPain, Symptoms).

% Leptospirosis
has_disease(Symptoms, leptospirosis) :-
  member(wound, Symptoms),
  member(flood, Symptoms),
  member(hFever, Symptoms),
  member(headache, Symptoms),
  member(chills, Symptoms),
  (member(mPain, Symptoms) ; member(aPain, Symptoms)),
  member(diarrhea, Symptoms),
  member(vomiting, Symptoms),
  member(rEyes, Symptoms),
  member(rashes, Symptoms),
  member(sBreath, Symptoms),
  (member(cBlood, Symptoms) ; member(pBlood, Symptoms) ; member(jaundice, Symptoms)).

% Typhoid Fever
has_disease(Symptoms, typhoid_fever) :-
  member(hFever, Symptoms),
  member(chills, Symptoms),
  member(headache, Symptoms),
  member(aPain, Symptoms),
  (member(jPain, Symptoms) ; member(mPain, Symptoms)),
  (member(diarrhea, Symptoms) ; member(nausea, Symptoms) ; member(vomiting, Symptoms)),
  (member(dCough, Symptoms) ; member(aLoss, Symptoms) ; member(rashes, Symptoms)).

% Hepatitis B
has_disease(Symptoms, hepatitis_B) :-
  member(multiple, Symptoms), 
  member(multiple, Symptoms), 
  member(partnerHBV, Symptoms),
  member(shared, Symptoms),
  member(nhbv, Symptoms),
  member(lFever, Symptoms),
  member(fatigue, Symptoms),
  member(jPain, Symptoms),
  (member(nausea, Symptoms) ; member(vomiting, Symptoms) ; member(aPain, Symptoms)),
  (member(jaundice, Symptoms) ; member(darkUrine, Symptoms) ; member(wLoss, Symptoms) ; member(aLoss, Symptoms)).

% Rabies
has_disease(Symptoms, rabies) :- member(rabBite, Symptoms).
has_disease(Symptoms, rabies) :-
  member(hFever, Symptoms),
  member(fatigue, Symptoms),
  member(headache, Symptoms),
  (member(hallucinations, Symptoms) ; member(hydrophobia, Symptoms) ; member(anxiety, Symptoms) ; member(agitation, Symptoms)).

% Pneumonia
has_disease(Symptoms, pneumonia) :-
  (member(pCough, Symptoms) ; member(dCough, Symptoms)),
  (member(hFever, Symptoms) ; member(lFever, Symptoms) ; member(lTemp, Symptoms)),
  (member(chills, Symptoms) ; member(fatigue, Symptoms) ; member(malaise, Symptoms)),
  member(aLoss, Symptoms),
  member(sBreath, Symptoms),
  member(mPain, Symptoms),
  member(cPain, Symptoms),
  (member(bSkin, Symptoms) ; member(wheezing, Symptoms)).

% Influenza
has_disease(Symptoms, influenza) :-
  member(lFever, Symptoms),
  member(headache, Symptoms),
  member(sThroat, Symptoms),
  (member(dCough, Symptoms) ; member(mPain, Symptoms) ; member(jPain, Symptoms)).

% Cholera
has_disease(Symptoms, cholera) :-
  (member(unsafe, Symptoms) ; member(unsanitary, Symptoms)),
  member(dehydration, Symptoms),
  member(diarrhea, Symptoms),
  (member(nausea, Symptoms); member(vomiting, Symptoms)),
  (member(sunken, Symptoms) ; member(aPain, Symptoms) ; member(lPressure, Symptoms)).

diagnose(Symptoms, Diseases) :-
  setof(Disease, has_disease(Symptoms, Disease), Diseases).