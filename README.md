# Salary Prediction Project

The deploy web app is live at: https://predicted-salary.herokuapp.com/

## The web app was built in Python using the following libraries:

streamlit
pandas
numpy
scikit-learn
pickle

## Problem Statement

The most important asset in any company is is the people—the human capita. It’s important to find great talent, and more importantly to keep the great talent happy and loyal to the company.

Salary, without a doubt is a great factor in attracting great people and keep people happy in the organization.

In this project, we want to find out:

With the data available, can we develop a model that predicts the salary for a specific job and profile?

How accurate can we get?


## Data


## 1. Introduction


### The dataset, features and target value

There are a million entries in the dataset.

The decription for the variables are as follows:

* **jobId:** The ID of the job.
* **companyId:** The ID of the company.
* **jobType:** The description of the job.
* **degree:** The degree of the employee.
* **major:** The university or college field of specialization of the employee.
* **industry:** The field to which the company belongs.
* **yearsExperience:** The employee years of experience on the job.
* **milesFromMetropolis:** The distance in miles, the employee lives away from his/her place of work.

The target variable is the salary each employee receives, being the columns the following:

* **jobId:** The ID of the job.
* **salary:** Salary amount paid for that job.


## 2. Data quality check

There are no duplicated entries or missing values in the dataset.

There are, however, some outliers in our target variable. Upon evaluation, we noticed that the outliers in the upper boundary are from high paying industries e.g. oil and fianance, so we will keep these values.

There are also salaries with value of 0. We decided to remove these outliers off the dataset.


## 3. Descriptive statistics

### General overview

We will examine independent variables in relation to our target variable.

* The categorical features have the following unique values:


Feature | Unique values | 
--- | --- 
jobType | CFO, CEO, VICE_PRESIDENT, MANAGER, JUNIOR, JANITOR, CTO, SENIOR
degree | MASTERS, HIGH_SCHOOL, DOCTORAL, BACHELORS, NONE
major | MATH, NONE, PHYSICS, CHEMISTRY, COMPSCI, BIOLOGY, LITERATURE, BUSINESS, ENGINEERING
industry | HEALTH, WEB, AUTO, FINANCE, EDUCATION, OIL, SERVICE

Job type:

As we can see that the job type variable is eventually distributed across the dataset. 

Janitor has the lowest median salary while CEO has the highest. 

![](https://i.imgur.com/Ke07Z4r.png)

Degree:

About half of the peope in the dataset has either a high school diploma or no degree. Bachelor, master and doctoral degrees are eventually distributed. 

Not surprising, people has no degree has the lowest median salary.

![](https://i.imgur.com/9B0y1TA.png)

Major:

More than half of the people in the dataset has no major. The rest of the majors are eventually distributed.

People has no major has the lowest median salary while engineering major has the highest salary.

![](https://i.imgur.com/LfasZvS.png)

Industry:

All industires are eventlly distributed.

Education has the lowest median salary while oil has the highest median salary.

![](https://i.imgur.com/jq6152X.png)

Years of experience:

Years of experience is positively correlated with salary.

![](https://i.imgur.com/PoelEn4.png)

Miles from metropolis:

Miles from metropolis is negatively correlated with salary.

![](https://i.imgur.com/lgwIsFD.png)


## 5. Model development

### Baseline

We encode our categorical variables with label encoder and deployed a simple linear regression model.

The MSE for the baseline model is: 925.31


### Hypothesize solution 

The baseline model doesn't really do a decent job of predicting salary. There are still a lot of room to improve the performance:

The larger the variance in the variables, the strong impact it does for the model. So we can scale all the numerical variables in the dataset.

We will test the model by using Random Tree model.

Gradient Boosting Regressor is very robust as well.

It also makes sense that people who have similar background may have similar salary. So we will also test KNearest Neighbor.

### Feature engeenering

During the explorary data analysis, we noticed that there is an order to the median salaries of the categorical variables. 

Because of that, we are going to to code with the categorical variables with their mean salaries.

Correalation Matrix:

After we applied mean encoding to the categorical variables. We see a correlation matrix as follows:

![](https://i.imgur.com/jXhSSZo.png)


## 5. Develop Model


### Feature engeenering

During the explorary data analysis, we noticed that there is an order to the median salaries of the categorical variables. 

Because of that, we are going to to code with the categorical variables with their mean salaries.

Correalation Matrix:

After we applied mean encoding to the categorical variables. We see a correlation matrix as follows:

![](https://i.imgur.com/jXhSSZo.png)


### Best model selection

For this regression task, 3 different machine learning algorithms were selected, one linear and two ensembles, to see which performs better for the problem:

* **Linear regressor.**
* **Random forest regressor.**
* **XGboost regressor.**

After being carefully tuned, we've tested each of them with *cross_val_score*, having the following results:

Classifier | MSE | RMSE 
--- | --- | --- 
Random forest regressor | 432.5944 | 18.4552
XGBoost regressor | 366.3565 | 18.4216

The lowest *MSE* error was returned by the _**XGBoost regressor**_, although the score of the *Random forest regressor* was very close. Once the best model was fitted with the train data, the feature importance generated by the model are:


Then, the prediction for the unseen jobs position was made and exported into a CSV file.
