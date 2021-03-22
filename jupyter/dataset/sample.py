import os
import time
import pandas as pd
import numpy as np
import datetime
import torch

MAX_PATIENT_ID = 1000

def sample_patients(input_file, max_patient_id):
    df = pd.read_csv(input_file, index_col="ROW_ID")
    df = df[df.SUBJECT_ID <= max_patient_id]
    df.to_csv(input_file + "_" + str(max_patient_id))

sample_patients("PATIENTS.csv", MAX_PATIENT_ID)
sample_patients("ADMISSIONS.csv", MAX_PATIENT_ID)
sample_patients("DIAGNOSES_ICD.csv", MAX_PATIENT_ID)
sample_patients("PROCEDURES_ICD.csv", MAX_PATIENT_ID)
sample_patients("ICUSTAYS.csv", MAX_PATIENT_ID)

