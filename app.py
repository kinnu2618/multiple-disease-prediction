import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

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
alzheimers_model = pickle.load(open(f'{working_dir}/saved_models/alzheimers_model.sav', 'rb'))


# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Anaemia Prediction', 'Alzheimer\'s Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person', 'lungs', 'droplet', 'brain'],
        default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes')

    # getting the input data from the user
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

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
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

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == 'Lung Cancer Prediction':

    # page title
    st.title('Lung Cancer')

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.text_input('Gender')

    with col2:
        age = st.text_input('Age')

    with col3:
        smoking = st.text_input('Smoking')

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

# Anemia Prediction Page
if selected == 'Anaemia Prediction':
    st.title('Anaemia Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.text_input('Gender')
    with col2:
        hemoglobin = st.text_input('Hemoglobin Level')
    with col3:
        mch = st.text_input('MCH Level')
    with col1:
        mchc = st.text_input('MCHC Level')
    with col2:
        mcv = st.text_input('MCV Level')

    anemia_diagnosis = ''

    if st.button('Anaemia Test Result'):
        user_input = [gender, hemoglobin, mch, mchc, mcv]

        try:
            user_input = [float(x) if x.isdigit() else x for x in user_input]
            anemia_prediction = anaemia_model.predict([user_input])

            if anemia_prediction[0] == 1:
                anemia_diagnosis = 'The person has anemia'
            else:
                anemia_diagnosis = 'The person does not have anemia'

        except ValueError:
            st.error("Please ensure all fields are filled with valid numeric values where applicable.")

    st.success(anemia_diagnosis)

# Alzheimer's Disease Prediction Page
if selected == "Alzheimer's Prediction":
    st.title("Alzheimer's Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        gender = st.text_input('Gender')
    with col3:
        ethnicity = st.text_input('Ethnicity')
    with col1:
        education_level = st.text_input('Education Level')
    with col2:
        bmi = st.text_input('BMI')
    with col3:
        smoking = st.text_input('Smoking')
    with col1:
        alcohol = st.text_input('Alcohol Consumption')
    with col2:
        physical_activity = st.text_input('Physical Activity')
    with col3:
        diet_quality = st.text_input('Diet Quality')
    with col1:
        sleep_quality = st.text_input('Sleep Quality')
    with col2:
        family_history = st.text_input('Family History of Alzheimer\'s')
    with col3:
        cardiovascular_disease = st.text_input('Cardiovascular Disease')
    with col1:
        diabetes = st.text_input('Diabetes')
    with col2:
        depression = st.text_input('Depression')
    with col3:
        head_injury = st.text_input('Head Injury')
    with col1:
        hypertension = st.text_input('Hypertension')
    with col2:
        systolic_bp = st.text_input('Systolic Blood Pressure')
    with col3:
        diastolic_bp = st.text_input('Diastolic Blood Pressure')
    with col1:
        cholesterol_total = st.text_input('Total Cholesterol')
    with col2:
        cholesterol_ldl = st.text_input('Cholesterol LDL')
    with col3:
        cholesterol_hdl = st.text_input('Cholesterol HDL')
    with col1:
        cholesterol_triglycerides = st.text_input('Cholesterol Triglycerides')
    with col2:
        mmse = st.text_input('MMSE')
    with col3:
        functional_assessment = st.text_input('Functional Assessment')
    with col1:
        memory_complaints = st.text_input('Memory Complaints')
    with col2:
        behavioral_problems = st.text_input('Behavioral Problems')
    with col3:
        adl = st.text_input('ADL')
    with col1:
        confusion = st.text_input('Confusion')
    with col2:
        disorientation = st.text_input('Disorientation')
    with col3:
        personality_changes = st.text_input('Personality Changes')
    with col1:
        difficulty_completing_tasks = st.text_input('Difficulty Completing Tasks')
    with col2:
        forgetfulness = st.text_input('Forgetfulness')

    alzheimers_diagnosis = ''

    if st.button("Alzheimer's Test Result"):
        user_input = [
            age, gender, ethnicity, education_level, bmi, smoking, alcohol, physical_activity, diet_quality,
            sleep_quality, family_history, cardiovascular_disease, diabetes, depression, head_injury,
            hypertension, systolic_bp, diastolic_bp, cholesterol_total, cholesterol_ldl, cholesterol_hdl,
            cholesterol_triglycerides, mmse, functional_assessment, memory_complaints, behavioral_problems,
            adl, confusion, disorientation, personality_changes, difficulty_completing_tasks, forgetfulness
        ]

        try:
            user_input = [float(x) if x.isdigit() else x for x in user_input]
            alzheimers_prediction = alzheimers_model.predict([user_input])

            if alzheimers_prediction[0] == 1:
                alzheimers_diagnosis = "The person has Alzheimer's disease"
            else:
                alzheimers_diagnosis = "The person does not have Alzheimer's disease"

        except ValueError:
            st.error("Please ensure all fields are filled with valid numeric values where applicable.")

    st.success(alzheimers_diagnosis)
