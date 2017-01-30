# AI-residential-electricity-bill-prediction
Prediction of Residential Electricty Bill Amount using Aritificial Intelligence

Used AI techniques and programmed in Python and R to develop a system that predicts the next month’s electricity bill amount for a given household. Trained and tested the model using data from over 12,000 U.S. residential units.

The total worldwide electricity consumption is increasing year by year which means high demand for electricity. Lot of research has been done to reduce the consumption of energy, electricity in particular, by using prediction methods where consumer usage and load is forecasted in kWh. This project focuses on predicting the predicting the electricity bill amount in dollars at the residential level for the use of a household consumer. This helps in financial preparedness and also to reduce electricity at the residential level which in turn helps in saving energy sources. The implementation is done in two stages: In stage 1, data collection, data processing and feature selection is done. The data set contained over 900 attributes that influence the energy consumption at the residential level; around 190 attributes are found in particular that influence the electricity consumption. The best features were selected using classifiers and 24 selected inputs were obtained. In stage 2, we implemented kNN and used lazy learning technique for modeling. Training and testing sets were divided in 90/10 ratio. We were able to predict the electricity bill amount values for the test set after training. To evaluate the efficiency of the model, MAE and RMSE errors are calculated. We have an error percentage of 19.32%.

Detailed flow of research project:

1. Data Collection
Collected energy consumption data for 12,083 U.S. residential housing units. The samples in the data set represent 113.6 million U.S. homes. This data set is from the year 2009 and it was the 13th iteration of the RECS program (first conducted in 1978). This type of data set ensured good accuracy as it has enough samples (12,083) to train and test the algorithm with no missing values. Data set had 935 factors that affect energy consumption of a housing unit. 

2. Data Analysis
Factored out the possible attributes that affect only the electricity consumption of housing unit. Used Python to parse the 190 columns from the CSV data set. 

3. Feature Selection
Using Random Forest Classifier algorithm, programmed feature selection model in R. 190 possible input factors were reduced to 24 specific inputs using feature selection after 100 iterations. The feature importance chart is also plotted. The 24 specific inputs to the final learning model are as follows:
    - TYPEHUQ (Type of Housing Unit)
    - HDD30YR (Heating degree days, 30-year average 1981-2010, base 65F)
    - CDD30YR (Cooling degree days, 30-year average 1981-2010, base 65F)
    - BEDROOMS (Number of bedrooms)
    - NCOMBATH (Number of full bathrooms)
    - TOTROOMS (Total number of rooms in the housing unit)
    - CELLAR (Basement in housing unit)
    - GARGHEAT (Heating used in attached garage)
    - HEATROOM (Number of rooms heated)
    - ACROOMS (Number of rooms cooled)
    - USECENAC (Frequency central air conditioner used in summer 2009)
    - TEMPNITEAC (Temperature at night (summer))
    - TOTSQFT (Total square footage (includes all attached garages, all basements, and finished/heated/cooled attics))
    - TOTHSQFT (Total heated square footage)
    - TOTCSQFT (Total cooled square footage)
    - KWH (Total Site Electricity usage, in kilowatt-hours)
    - KWHCOL (Electricity usage for air-conditioning, central and window/wall (room), in kilowatt-hours)
    - KWHRFG (Electricity usage for refrigerators, in kilowatt-hours)
    - KWHOTH (Electricity usage for other purposes (all end-uses except SPH, COL, WTH, and RFG), in kilowatt-hours)
    - DOLELCOL (Electricity cost for air-conditioning, central and window/wall (room), in whole dollars)
    - DOLELWTH (Electricity cost for water heating, in whole dollars)
    - DOLELRFG (Electricity cost for refrigerators, in whole dollars)
    - DOLELOTH (Electricity cost for other purposes (all end-uses except SPH, COL, WTH, and RFG), in whole dollars)
    - DOLLAREL (Total Electricity cost, in whole dollars)
    
4. kNN Modeling (Lazy learning)
We have 12,083 samples of data. Used 10,000 samples to train the kNN model and 2,083 samples to test the model. 

5. Training and Testing
Predicted the electricity bill amount for the next month of a given residential housing unit based on the 24 factors that affect electricity consumption.

6. Error Calculation for accuracy measurement
To evaluate the efficiency of the model, MAE (mean absolute error) and RMSE (root mean square error) are calculated for the predicted values. The error is between the testing set and the predicted values. The predicted value can be greater than, lesser than or equal to the actual value. MAE is useful in this case as it measures the accuracy for continuous variables.
