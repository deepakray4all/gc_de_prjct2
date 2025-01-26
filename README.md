# GCP Data Engineering and Analytics Project
This project is for extracting data from web app  to GCS and from there to BigQuery using Cloud Function

## Requirement:
1. Global Retail Chain needs to consolidate and analyze its sales  revenue
2. The company needs a web application to load the sales data kept  in csv from all the geogaphy to a single location
3. From  the single location the company wants to have analytics performed by it's Business Analyst

## Solution
1. A simple Web application to upload the csv files of sales data
2. The Web Application should store these files in GCS Bucket
3. When the file is uploaded to GCS bucket one GCP Cloud function event must be triggered
4. The uploaded file in GCS should be loaded to Biggquery with help cloud run function
5. Required transformation  is performed in BigQuery to get the sales revenue values
6. The transformed data must be saved in BigQuery View
7. Using Looker Studio the Dashboardcan  be created for the  bigquery data

##Architecture
![image](https://github.com/user-attachments/assets/f64a377a-e6ad-405d-a5c7-ecfa8f2f1c7a)
