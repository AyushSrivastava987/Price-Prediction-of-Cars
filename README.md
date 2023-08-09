# 
                               Price-Prediction of Pre-owned Mercedes-Benz Cars

<p align="center"><img src="https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Media/car%202.gif" width="400" height="200"> 
 <br>
  
## 📝 Description
* This repository represents **"Price-Prediction of Mercedes Benz"**
* With the help of this project we can meaningfully and reliably predict prices of pre-owned cars based on some relevant characteristics.

## ⏳ Dataset 
* Data of over 3000 pre-owned Mercedes-Benz-cars was extracted from https://www.cars.com/
* Data cleaning, organization, and feature engineering were done over the dataframe.
* Download the dataset for custom training:
 https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Cleaned_Car.csv

## 📝 Steps Involved

1. **Objective:** To build a Machine Learning model (Linear Regression) that can predict prices (label) of used cars based on various features
2. **Data Collection:** The data was scrapped from the website www.cars.com
3. **Data Cleaning & Feature Engineering:** Initially the dataset had all the data in 6 columns, the data had null values, duplicates, and noise too. After applying techniques like Data Cleaning (imputation, outlier detection, and removing duplicate records), EDA, and Feature Generation, 7 meaningful features were generated, which can be used for drawing insights through aggregations and visualization.The final dataset has the following independent features:
```bash
Name             
Mileage         
Dealer_Name      
Rating          
Review_Count      
Price           
Year    
```
4. **Data Analysis and Visualisation:** Meanwhile data analysis through groupby, pivot table, and aggregate functions was also done and the data was visualized (screenshots may be referred to).
5. **Training:** The final dataset was then split into training and testing datasets and trained through Linear Regression.
6. **Testing:** The predicted values for the label (price) were then generated. The accuracy came out to be 82%.
7. **Predicting (Applying the Model):** As a test case, predicting the price of a used car using hypothetical features seems to be quite reasonable and meaningful. The model now can be used by a user who may be a buyer/seller to predict the prices of pre-owned cars.

 ## Visual Insights

<img src="https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Media/Distribution%20of%20Price.png" width="350" height="300"> <img src="https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Media/Distribution%20of%20mileage.png" width="350" height="300">
<br>
<img src="https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Media/Correlation.png" width="350" height="260"> <img src="https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Media/Top%205%20most%20Expensive%20Cars.png" width="350" height="260">
<br>
<img src="https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Media/Top%205%20most%20rated%20Variants.png" width="350" height="300"> <img src="https://github.com/AyushSrivastava987/Price-Prediction-of-Cars/blob/main/Media/Top%205%20most%20rated%20with%20year%20information.png" width="400" height="300">
<br>


## <img src="https://user-images.githubusercontent.com/108053296/185756908-fbb62168-d923-48f2-992f-b8e2fde848fe.gif" width="48" height="48" > Key insights from the dataset
   
   1. Top most expensive cars have come out to be :
      
          Maybach S 680
          Maybach S 580
          AMG G 63
   2. Most rated variants of cars have come out to be :
      
          S-Class S 560     
          AMG GLE 53 Base   
          GLS 580 Base 4MATIC  
          S-Class S 500 4MATIC
          GLS 450 4MATIC
   3. Most rated variant with year come out to be:
      
          S-Class S 560     2019
          AMG GLE 53 Base     2021
          GLS 580 Base 4MATIC     2020
          S-Class S 500 4MATIC     2022
          GLS 450 4MATIC     2022

