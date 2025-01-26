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

## Architecture

![image](https://github.com/user-attachments/assets/f64a377a-e6ad-405d-a5c7-ecfa8f2f1c7a)


## Screenshots
### WebApp for Uploading file
![image](https://github.com/user-attachments/assets/60669c3c-f962-4be0-8409-3e423fdce120)

### GCS Bucket with files
![image](https://github.com/user-attachments/assets/62494a6b-6c58-4f56-88f3-715a8dd020a6)

### Cloud Function
![image](https://github.com/user-attachments/assets/54579109-6c3e-4646-829e-389ddbf69225)
![image](https://github.com/user-attachments/assets/72c31ec4-c710-4ee6-8238-eb588a2f25ad)

![image](https://github.com/user-attachments/assets/a26498ee-48f1-4bc0-99c1-900fd3ab9200)

### BigQuery Data set ,Tables and Views
![image](https://github.com/user-attachments/assets/306962a7-b95b-429a-8e62-c635d2ceff5a)
![image](https://github.com/user-attachments/assets/2ce62b4f-febd-44ec-92c0-5fc7d40e1b3e)

### Looker Studio  Dashboard
![image](https://github.com/user-attachments/assets/f531d44d-1c93-4256-b28d-6fd0ecc96463)





