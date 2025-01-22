# Precise Blood Cancer Detection using GANs and cross-modality data integration for optimal diagnostics

## Abstract
Blood cancers, encompassing leukemia, lymphoma, and myeloma, are a diverse group of malignancies that affect the blood and bone marrow.

- **Leukemia**: Characterized by the uncontrolled production of abnormal blood cells in the bone marrow. It includes:
  - Acute Lymphoblastic Leukemia (ALL): A rapidly progressing cancer affecting immature lymphoid cells.
  - Acute Myeloid Leukemia (AML): A fast-growing leukemia that starts in the myeloid cells.
  - Chronic Lymphocytic Leukemia (CLL): A slower-growing leukemia affecting mature lymphocytes.
  - Chronic Myeloid Leukemia (CML): A cancer that starts in the blood-forming cells of the bone marrow and invades the blood.
  
- **Lymphoma**: Affects the lymphatic system and is categorized into:
  - Hodgkin Lymphoma (HL): Marked by the presence of Reed-Sternberg cells, it typically presents with swollen lymph nodes and can progress rapidly.
  - Non-Hodgkin Lymphoma (NHL): Includes a variety of lymphoid cancers, such as:
    - Diffuse Large B-Cell Lymphoma (DLBCL): A fast-growing lymphoma that affects B cells.
    - Follicular Lymphoma: A slower-growing lymphoma that originates from follicle center cells.

- **Myeloma**: Primarily refers to:
  - Multiple Myeloma: A cancer of the plasma cells in the bone marrow, characterized by the proliferation of abnormal plasma cells that produce abnormal proteins and can cause bone damage.

This project aims to develop an advanced classification system for three blood cancers—leukemia, lymphoma, and myeloma—and their subtypes using a combination of Generative Adversarial Networks (GANs) and Convolutional Neural Networks (CNNs).

## Getting Started
### Technologies Used
- Python 
- Flask
- HTML, CSS
- Django
- Tensorflow

### Image Dataset Description
The dataset contains a total of 17,092 images of individual normal cells, which were acquired using the analyzer CellaVision DM96 in the Core Laboratory at the Hospital Clinic of Barcelona. The dataset is organized in the following eight groups: neutrophils, eosinophils, basophils, lymphocytes, monocytes, immature granulocytes (promyelocytes, myelocytes, and metamyelocytes), erythroblasts and platelets or thrombocytes. The size of the images is 360 x 363 pixels, in format JPG, and they were annotated by expert clinical pathologists. The images were captured from individuals without infection, hematologic or oncologic disease and free of any pharmacologic treatment at the moment of blood collection.
Here’s how the classes might be helpful in detecting the three main types of blood cancers:

Leukemia: Basophils, lymphocytes, erythroblasts.
Lymphoma: Lymphocytes, monocytes.
Myeloma: Platelets, plasma cells and ig (immature granulocytes).

## Run the Flask application
python app.py

