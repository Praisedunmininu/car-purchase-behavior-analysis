# ======================
# import  libraries 
# ========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Load Dataset
# ==========================
df = pd.read_csv(r"C:\Users\Islamiat Seriki\sales_prediction\car_purchasing.csv",encoding='latin1')

# =======================
# Initial Data Exploration
# ===========================
print(df.head())
print(df.info())
print(df.columns)
print(df.shape)

# =========================
# Gender Analysis -Overview
# ===========================
print("unique values in gender columns:")
print(df["gender"].unique())
print("\nHow many of each category in gender columns:")
print(df["gender"].value_counts())

# ================================
# Car Purchase Amount Analysis
#  ==================================
print(df["car purchase amount"].describe())

# ====================================
# Binning Car Purchase Amount
# =================================
purchase_bins =[0,37629,43997,51254,80000]
purchase_labels = ["low_cars","medium_cars","high_cars","very_high_cars"]
df["car_purchase_worth"]= pd.cut(df["car purchase amount"],bins=purchase_bins,labels=purchase_labels)

# =================================
# Gender Spending Analysis (Average)
# ===================================
gender_spending = df.groupby("gender")["car purchase amount"].mean().reset_index()
print(gender_spending)

gender_spending.plot(x="gender", y="car purchase amount",kind='bar')
plt.title("Average gender spending")
plt.xlabel("gender")
plt.ylabel("car purchase amount")
plt.show()
plt.close()

# ==============================
# Gender Purchase Count Analysis
# ===============================
gender_purchase = df.groupby("gender")["car_purchase_worth"].size()
print(gender_purchase)

gender_purchase.plot(kind='bar')
plt.title("Count of gender purchase")
plt.xlabel("gender")
plt.ylabel("car_purchase_worth")
plt.show()
plt.close()

# ==========================
# Gender spending Analysis (Total)
# ===============================
gender_spending = df.groupby("gender")["car purchase amount"].sum()
print(gender_spending)

gender_spending.plot(x="gender", y="car purchase amount",kind='bar')
plt.title("Total Revenue by Gender")
plt.xlabel("gender")
plt.ylabel("car purchase amount")
plt.show()
plt.close()

# ==========================
# Net Worth Analysis
# ===================

print(df["net worth"].describe())

net_worth_bins =[0,299824,426750,557324,1000000]
net_worth_labels =["low","medium","high","very_high"]
df["net_worth_group"]=pd.cut(df["net worth"],bins=net_worth_bins,labels=net_worth_labels)
print(df["net_worth_group"].head())

net_worth_analysis =df.groupby("net_worth_group")["car purchase amount"].mean().reset_index()
print(net_worth_analysis)

net_worth_analysis.plot(x="net_worth_group",y="car purchase amount",kind='bar')
plt.title("Average car purchase by Net Worth")
plt.xlabel("Net_worth_group")
plt.ylabel("Average purchase amount")
plt.show()
plt.close()


# ============================
# Age analysis
# ============================
print(df["age"].describe())

age_bins = [20,40,50,60,70]
age_labels =["young", "middle", "senior","older"]
df["age_group"]=pd.cut(df["age"],bins=age_bins,labels=age_labels)
print(df["age_group"].head())


# ===========================
# Age vrs purchase Analysis
# ===============================
age_analysis = df.groupby("age_group")["car purchase amount"].mean().reset_index()
print(age_analysis)


age_analysis.plot(x="age_group",y="car purchase amount",kind='bar')
plt.title("Car purchase amount by age ")
plt.xlabel("Age_group")
plt.ylabel("Average purchase amount")
plt.show()
plt.close()

country_analysis = df.groupby("country")["car purchase amount"].mean().reset_index()
print(country_analysis)

country_analysis = country_analysis.sort_values(by="car purchase amount",ascending =False)
top_country = country_analysis.head(5)
print(top_country)

top_country.sort_values(by ="car purchase amount").plot(x="country",y="car purchase amount",kind='barh')
plt.title("Top countries by Average car purchase")
plt.xlabel("country")
plt.ylabel("car purchase amount")
plt.show()
plt.close()


# =============================
# Credit card debt Analysis
# ===========================

print(df["credit card debt"].describe())

credit_card_debt_bins = [0,7397,9655,11798,20000]
credit_card_debt_labels = ["low","medium","high","very_high"]
df["debt_card_group"] = pd.cut(df["credit card debt"],bins = credit_card_debt_bins,labels= credit_card_debt_labels)
print(df["debt_card_group"].head())

credit_card_debt_analysis = df.groupby("debt_card_group")["car purchase amount"].mean().reset_index()
print(credit_card_debt_analysis)

credit_card_debt_analysis.plot(x="debt_card_group",y="car purchase amount",kind='bar')
plt.title("Average Car Purchase Amount by Credit Card Debit Level")
plt.xlabel("debt_card_group")
plt.ylabel("car purchase amount")
plt.show()
plt.close()


















