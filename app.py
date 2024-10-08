import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))
lung_cancer_model = pickle.load(open(f'{working_dir}/saved_models/lung_cancer_model.sav', 'rb'))
anaemia_model = pickle.load(open(f'{working_dir}/saved_models/anaemia_model.sav', 'rb'))
hyper_model = pickle.load(open(f'{working_dir}/saved_models/hyper_model.sav', 'rb'))



# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Anaemia Prediction', 'Hypertension Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person', 'lungs', 'droplet', 'thermometer'],
        default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # Page title
    st.title('Diabetes')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        # Check if any of the fields are empty
        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.error("Please enter the value for all fields.")
        else:
            try:
                # Convert inputs to float for prediction
                user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), 
                              float(SkinThickness), float(Insulin), float(BMI), 
                              float(DiabetesPedigreeFunction), float(Age)]

                # Make prediction using the model
                diab_prediction = diabetes_model.predict([user_input])

                # Display result based on prediction
                if diab_prediction[0] == 1:
                    diab_diagnosis = 'The person is diabetic'
                else:
                    diab_diagnosis = 'The person is not diabetic'

                st.success(diab_diagnosis)
            except ValueError:
                st.error("Please enter valid numeric values for all fields.")


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # Page title
    st.title('Heart Disease')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        # Change sex input to a dropdown for Male and Female
        sex = st.selectbox('Sex', ('Male', 'Female'))
        # Convert Male to 1 and Female to 0
        sex = 1 if sex == 'Male' else 0

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')

    with col3:
        # Change Fasting Blood Sugar input to a dropdown
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ('True', 'False'))
        # Convert "True" to 1 and "False" to 0
        fbs = 1 if fbs == 'True' else 0

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        # Change Exercise Induced Angina input to a dropdown
        exang = st.selectbox('Exercise Induced Angina', ('Yes', 'No'))
        # Convert "Yes" to 1 and "No" to 0
        exang = 1 if exang == 'Yes' else 0

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')

    with col1:
        # Change thal input to a dropdown for descriptive options
        thal = st.selectbox('Thalassemia', ('Normal', 'Fixed Defect', 'Reversible Defect'))
        # Convert to corresponding numeric values
        thal = 0 if thal == 'Normal' else 1 if thal == 'Fixed Defect' else 2

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # Check if any input field is empty
        if not all([age, cp, trestbps, chol, restecg, thalach, oldpeak, slope, ca]):
            st.error("Please enter the value for all fields.")
        else:
            try:
                # Convert input data to float before passing to the model
                user_input = [float(age), sex, float(cp), float(trestbps), float(chol),
                              fbs, float(restecg), float(thalach), exang,
                              float(oldpeak), float(slope), float(ca), thal]

                # Make prediction using the model
                heart_prediction = heart_disease_model.predict([user_input])

                # Display result based on prediction
                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person is having heart disease'
                else:
                    heart_diagnosis = 'The person does not have any heart disease'

                st.success(heart_diagnosis)
            except ValueError:
                st.error("Please enter valid numeric values where applicable.")


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # Page title
    st.title("Parkinson's Disease")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        # Check if all fields are filled
        if not all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, 
                    Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            st.error("Please enter the value for all fields.")
        else:
            try:
                # Convert input data to float before passing to the model
                user_input = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                              float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                              float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                              float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]

                # Make prediction using the model
                parkinsons_prediction = parkinsons_model.predict([user_input])

                # Display result based on prediction
                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"

                st.success(parkinsons_diagnosis)
            except ValueError:
                st.error("Please enter valid numeric values where applicable.")


# Lung Cancer Prediction Page
if selected == 'Lung Cancer Prediction':

    # page title
    st.title('Lung Cancer')

    col1, col2, col3 = st.columns(3)

    with col1:
        # Change gender input to a dropdown for Male and Female
        gender = st.selectbox('Gender', ('Male', 'Female'))
        # Convert Male to 1 and Female to 0
        gender = 1 if gender == 'Male' else 0

    with col2:
        age = st.text_input('Age')

    with col3:
        # Change smoking input to a dropdown for Yes and No
        smoking = st.selectbox('Smoking', ('Yes', 'No'))
        # Convert Yes to 1 and No to 0
        smoking = 1 if smoking == 'Yes' else 0

    with col1:
        yellow_fingers = st.text_input('Yellow Fingers')

    with col2:
        anxiety = st.text_input('Anxiety')

    with col3:
        peer_pressure = st.text_input('Peer Pressure')

    with col1:
        chronic_disease = st.text_input('Chronic Disease')

    with col2:
        fatigue = st.text_input('Fatigue')

    with col3:
        allergy = st.text_input('Allergy')

    with col1:
        wheezing = st.text_input('Wheezing')

    with col2:
        alcohol_consuming = st.text_input('Alcohol Consuming')

    with col3:
        coughing = st.text_input('Coughing')

    with col1:
        shortness_of_breath = st.text_input('Shortness of Breath')

    with col2:
        swallowing_difficulty = st.text_input('Swallowing Difficulty')

    with col3:
        chest_pain = st.text_input('Chest Pain')

    # code for Prediction
    lung_cancer_diagnosis = ''

    if st.button('Lung Cancer Test Result'):
        
        # Gather user inputs
        user_input = [gender, age, smoking, yellow_fingers, anxiety, peer_pressure,
                      chronic_disease, fatigue, allergy, wheezing, alcohol_consuming,
                      coughing, shortness_of_breath, swallowing_difficulty, chest_pain]

        try:
            # Attempt to convert inputs to float where necessary (e.g., for age and numeric features)
            user_input = [float(x) if x.isdigit() else x for x in user_input]

            # Predict based on model
            lung_cancer_prediction = lung_cancer_model.predict([user_input])

            if lung_cancer_prediction[0] == 1:
                lung_cancer_diagnosis = 'The person has lung cancer'
            else:
                lung_cancer_diagnosis = 'The person does not have lung cancer'

        except ValueError:
            st.error("Please ensure all fields are filled with valid numeric values where applicable.")

    st.success(lung_cancer_diagnosis)


# Anaemia Prediction Page
if selected == 'Anaemia Prediction':

    # Page title
    st.title('Anaemia Prediction')

    # Getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        Gender = st.selectbox('Gender', ('Male', 'Female'))
        # Convert Male to 1 and Female to 0
        Gender = 1 if Gender == 'Male' else 0

    with col2:
        Hemoglobin = st.text_input('Hemoglobin Level')

    with col1:
        MCH = st.text_input('Mean Corpuscular Hemoglobin (MCH)')

    with col2:
        MCHC = st.text_input('Mean Corpuscular Hemoglobin Concentration (MCHC)')

    with col1:
        MCV = st.text_input('Mean Corpuscular Volume (MCV)')

    # Code for Prediction
    anaemia_diagnosis = ''

    # Create a button for Prediction
    if st.button('Anaemia Test Result'):
        try:
            # Validate and convert user inputs
            Hemoglobin = float(Hemoglobin) if Hemoglobin else None
            MCH = float(MCH) if MCH else None
            MCHC = float(MCHC) if MCHC else None
            MCV = float(MCV) if MCV else None

            if None in (Hemoglobin, MCH, MCHC, MCV):
                st.error("Please fill all fields with valid numeric values.")
            else:
                user_input = [Gender, Hemoglobin, MCH, MCHC, MCV]
                input_data_as_numpy_array = np.asarray(user_input).reshape(1, -1)

                # Make prediction using the model
                prediction = anaemia_model.predict(input_data_as_numpy_array)

                # Interpret the prediction
                if prediction[0] == 1:
                    anaemia_diagnosis = 'The person has anaemia'
                else:
                    anaemia_diagnosis = 'The person does not have anaemia'

        except ValueError:
            st.error("Please ensure all fields are filled with valid numeric values where applicable.")

    st.success(anaemia_diagnosis)


# Hypertension Prediction Page
if selected == 'Hypertension Prediction':
    # Page title
    st.title('Hypertension Prediction')

    # Getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        Gender = st.selectbox('Gender', ('Male', 'Female'))
        Gender = 1 if Gender == 'Male' else 0

        age = st.text_input('Age')

        currentSmoker = st.selectbox('Current Smoker', ('Yes', 'No'))
        currentSmoker = 1 if currentSmoker == 'Yes' else 0

        cigsPerDay = st.text_input('Cigarettes Per Day')

        BPMeds = st.selectbox('On BP Medication', ('Yes', 'No'))
        BPMeds = 1 if BPMeds == 'Yes' else 0

    with col2:
        diabetes = st.selectbox('Diabetes', ('Yes', 'No'))
        diabetes = 1 if diabetes == 'Yes' else 0

        totChol = st.text_input('Total Cholesterol')

        sysBP = st.text_input('Systolic Blood Pressure (sysBP)')

        diaBP = st.text_input('Diastolic Blood Pressure (diaBP)')

        BMI = st.text_input('Body Mass Index (BMI)')

        heartRate = st.text_input('Heart Rate')

        glucose = st.text_input('Glucose Level')

    # Code for Prediction
    hyper_diagnosis = ''

    # Create a button for Prediction
    if st.button('Hypertension Test Result'):
        try:
            # Validate and convert user inputs
            age = float(age) if age else None
            cigsPerDay = float(cigsPerDay) if cigsPerDay else None
            totChol = float(totChol) if totChol else None
            sysBP = float(sysBP) if sysBP else None
            diaBP = float(diaBP) if diaBP else None
            BMI = float(BMI) if BMI else None
            heartRate = float(heartRate) if heartRate else None
            glucose = float(glucose) if glucose else None

            if None in (age, cigsPerDay, totChol, sysBP, diaBP, BMI, heartRate, glucose):
                st.error("Please fill all fields with valid numeric values.")
            else:
                # Input data for the model
                user_input = [Gender, age, currentSmoker, cigsPerDay, BPMeds, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]
                input_data_as_numpy_array = np.asarray(user_input).reshape(1, -1)

                # Make prediction using the model
                prediction = hyper_model.predict(input_data_as_numpy_array)

                # Interpret the prediction
                if prediction[0] == 1:
                    hyper_diagnosis = 'This person has hypertension.'
                else:
                    hyper_diagnosis = 'This person does not have hypertension.'

        except ValueError:
            st.error("Please ensure all fields are filled with valid numeric values where applicable.")

    st.success(hyper_diagnosis)