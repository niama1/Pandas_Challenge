#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[77]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"


# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[78]:


purchase_data = pd.DataFrame(purchase_data)
purchase_data


# ## Player Count

# * Display the total number of players
# 

# In[79]:


# display the total number of players
total_players = len(purchase_data["SN"].unique())
total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[80]:


# Calculate unique items.
unique = purchase_data["SN"].unique()
# Average price.
average_price = purchase_data["Price"].mean()
# Total revenue.
revenue = purchase_data["Price"].sum()
# dic = {[ "Key": Value..
          

# Create a summary data frama to hold the results
summary_df = pd.DataFrame({"unique":[unique],
                           "average_price":[average_price],
                           "revenue":[revenue]
                         
})
         


summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[81]:


# Percentage and count of gender Playres
gender_groups = purchase_data.groupby(["Gender"])
percent_any_gender = round((gender_groups["SN"].count() / total_players) *100, 2)

gender_df = pd.DataFrame({"Player Count": gender_groups["SN"].count(), "Percent of Players": percent_any_gender})
gender_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[82]:


# Purchase count,avg.purchase count, avg.purchase etc.. by group by gender.
gender_groupby = purchase_data.groupby(["Gender"])
purchase_count_gender = gender_groupby['Price'].count()
average_price = round(gender_groupby["Price"].mean(), 2)
total_val = round(gender_groupby["Price"].sum() ,2)
per_person = total_val / gender_df["Player Count"]

purchasing_df = pd.DataFrame({"Purchase Count": purchase_count_gender, "Avg. Purchase Price": average_price, "Total Purchase Value": total_val, "Total Purchase per Person": per_person})
purchasing_df["Avg. Purchase Price"] = purchasing_df["Avg. Purchase Price"].map("${:.2f}".format)
purchasing_df["Total Purchase Value"] = purchasing_df["Total Purchase Value"].map("${:.2f}".format)
purchasing_df["Total Purchase per Person"] = purchasing_df["Total Purchase per Person"].map("${:.2f}".format)
purchasing_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[90]:


# Etablish bins for age
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]



# In[96]:


purchase_data["Age Demographics summary"] = pd.cut(purchase_data["Age"], bins, labels=group_names, include_lowest=True)
purchase_data.head()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[141]:


# Create bins and labels to hold demographic data
bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 1000]
labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], bins, labels=labels)


#Create summary data
purchase_count = purchase_data_groupby["Price"].count()
avg_pur_price = round(purchase_data_groupby["Price"].mean(), 2)
total_pur = round(purchase_data_groupby["Price"].sum(), 2)
avg_pur_person = round(total_pur/purchase_count ,2)

pur_analysis = pd.DataFrame({"Purchase Count": purchase_count, "Average Purchase Price": avg_pur_price, "Total Purchase Price": total_pur, "Average Per Person": avg_pur_person})
pur_analysis["Average Purchase Price"] = pur_analysis["Average Purchase Price"].map("${:.2f}".format)
pur_analysis["Total Purchase Price"] = pur_analysis["Total Purchase Price"].map("${:.2f}".format)
pur_analysis["Average Per Person"] = pur_analysis["Average Per Person"].map("${:.2f}".format)
pur_analysis = pur_analysis.sort_index()
pur_analysis

                         


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[143]:


# Obtain the result
total_by_user = purchase_data.groupby(["SN"]).sum()["Price"]
avg_by_user = round(purchase_data.groupby(["SN"]).mean()["Price"], 2)
count_by_user = purchase_data.groupby(["SN"]).count()["Price"]
# Create a Summary of data frame
top_spenders = pd.DataFrame({"Total Purchase Value": total_by_user, "Average Purchase Price": avg_by_user, "Purchase Count": count_by_user})
top_spenders["Average Purchase Price"] = top_spenders["Average Purchase Price"].map("${:.2f}".format)
# Sort of total purchase
top_spenders.sort_values("Total Purchase Value", ascending=False).head(10)


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[144]:


# Retrieve the item ID, Item Name, and Item Price columns
popular_items_group = purchase_data.groupby(["Item ID", "Item Name"])
pop_pur_count = popular_items_group['Price'].count()
pop_price = popular_items_group['Price'].mean()
tot_price = popular_items_group["Price"].sum()

#Create the dataframe
df_popular_items = pd.DataFrame({'Purchase Count': pop_pur_count, "Total Purchase Value": tot_price, "Item Price": pop_price})
df_popular_items["Item Price"] = df_popular_items["Item Price"].map("${:.2f}".format)
df_popular_items.sort_values("Purchase Count", ascending=False).head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[145]:


# Sort of the above table by purchase value in descending order
df_popular_items.sort_values("Total Purchase Value", ascending=False).head()


# In[ ]:




