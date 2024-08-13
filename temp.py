import os

# Define the base directory for Chapter 2
base_dir = "Chapter_2_Data_and_Sampling_Distributions"

# Define the sections and sub-sections with index numbers
sections = {
    "1_Random_Sampling_and_Sample_Bias": [
        "1_Bias",
        "2_Random_Selection"
    ],
    "2_Size_Versus_Quality_When_Does_Size_Matter": [],
    "3_Sample_Mean_Versus_Population_Mean": [],
    "4_Selection_Bias": [
        "1_Regression_to_the_Mean"
    ],
    "5_Sampling_Distribution_of_a_Statistic": [
        "1_Central_Limit_Theorem",
        "2_Standard_Error"
    ],
    "6_The_Bootstrap": [
        "1_Resampling_Versus_Bootstrapping"
    ],
    "7_Confidence_Intervals": [],
    "8_Normal_Distribution": [
        "1_Standard_Normal_and_QQ_Plots"
    ],
    "9_Long_Tailed_Distributions": [],
    "10_Students_t_Distribution": [],
    "11_Binomial_Distribution": [],
    "12_Chi_Square_Distribution": [],
    "13_F_Distribution": []
}

# Function to create directories and Jupyter notebooks
def create_folders_and_notebooks(base_dir, sections):
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    
    for section, subsections in sections.items():
        section_dir = os.path.join(base_dir, section)
        if not os.path.exists(section_dir):
            os.mkdir(section_dir)
        
        # Create the main section notebook
        section_notebook_name = section.split('_', 1)[1]  # Remove the index from the notebook name
        with open(os.path.join(section_dir, f"{section_notebook_name}.ipynb"), 'w') as f:
            f.write('''{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}''')
        
        for subsection in subsections:
            subsection_dir = os.path.join(section_dir, subsection)
            if not os.path.exists(subsection_dir):
                os.mkdir(subsection_dir)
            
            # Create the sub-section notebook
            subsection_notebook_name = subsection.split('_', 1)[1]  # Remove the index from the notebook name
            with open(os.path.join(subsection_dir, f"{subsection_notebook_name}.ipynb"), 'w') as f:
                f.write('''{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}''')

# Create the folders and notebooks
create_folders_and_notebooks(base_dir, sections)
