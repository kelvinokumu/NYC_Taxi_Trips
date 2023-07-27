import pandas as pd
import matplotlib.pyplot as plt

# 1. Trip Duration: What is the average duration of taxi trips based on the pickup and drop-off timestamps?
df['trip_duration_minutes'] = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']).dt.total_seconds() / 60
average_duration = df['trip_duration_minutes'].mean()
print(f"Average trip duration (minutes): {average_duration:.2f}")

# 2. Store and Forward Flag: How many trips had the "store_and_fwd_flag" set to true? 
#    Is there any correlation between this flag and trip duration or distance?
store_fwd_trips = df[df['store_and_fwd_flag'] == 'Y']
print(f"Number of trips with store_and_fwd_flag = True: {len(store_fwd_trips)}")

# 3. Ratecode Analysis: What are the distribution and frequencies of different rate codes? 
#    Are there any rate codes that are more commonly used?
ratecode_counts = df['RatecodeID'].value_counts()
print("Distribution of Rate Codes:")
print(ratecode_counts)

# 4. Passenger Count: What is the average passenger count per trip? 
#    Are there any correlations between passenger count and trip distance or fare amount?
average_passenger_count = df['passenger_count'].mean()
correlation_passenger_distance = df['passenger_count'].corr(df['trip_distance'])
correlation_passenger_fare = df['passenger_count'].corr(df['fare_amount'])

print(f"Average passenger count per trip: {average_passenger_count:.2f}")
print(f"Correlation between passenger count and trip distance: {correlation_passenger_distance:.2f}")
print(f"Correlation between passenger count and fare amount: {correlation_passenger_fare:.2f}")

# 5. Trip Distance: What is the average trip distance covered by taxis? 
#    Can you identify any outliers or unusually long or short trips?
average_trip_distance = df['trip_distance'].mean()
print(f"Average trip distance: {average_trip_distance:.2f}")

# Box plot to identify outliers in trip distance
plt.boxplot(df['trip_distance'])
plt.xlabel('Trip Distance')
plt.title('Box Plot of Trip Distance')
plt.show()

# 6. Fare Analysis: What is the distribution of fare amounts? 
#    Are there any factors such as distance or time that significantly influence fare amounts?
plt.hist(df['fare_amount'], bins=30, edgecolor='black')
plt.xlabel('Fare Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Fare Amounts')
plt.show()

# 7. Extra Charges: How often and in what circumstances are extra charges applied? 
#    Is there any correlation between extra charges and total fare amounts?
extra_charges_counts = df['extra'].value_counts()
print("Frequency of Extra Charges:")
print(extra_charges_counts)

correlation_extra_fare = df['extra'].corr(df['total_amount'])
print(f"Correlation between extra charges and total fare amount: {correlation_extra_fare:.2f}")

# 8. Tip Amount: What is the average tip amount given by passengers? 
#    Can you identify any patterns or trends in tipping behavior?
average_tip_amount = df['tip_amount'].mean()
print(f"Average tip amount: {average_tip_amount:.2f}")

# 9. Tolls and Congestion Charges: What is the frequency and distribution of tolls and congestion charges incurred during trips? 
#    Are there specific locations or times when these charges are more common?
plt.hist(df['tolls_amount'], bins=30, edgecolor='black')
plt.xlabel('Tolls Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Tolls Amount')
plt.show()

# 10. Payment Types: What are the most common payment types used by passengers? 
#     Is there any correlation between payment type and tip amount or total fare amount?
payment_type_counts = df['payment_type'].value_counts()
print("Frequency of Payment Types:")
print(payment_type_counts)

correlation_payment_tip = df['payment_type'].corr(df['tip_amount'])
correlation_payment_fare = df['payment_type'].corr(df['total_amount'])
print(f"Correlation between payment type and tip amount: {correlation_payment_tip:.2f}")
print(f"Correlation between payment type and total fare amount: {correlation_payment_fare:.2f}")

# 11. Trip Types: What is the distribution of trip types (e.g., street-hail, dispatch) in the dataset? 
#     Are there any differences in trip duration or fare amounts based on trip type?
trip_type_counts = df['trip_type'].value_counts()
print("Frequency of Trip Types:")
print(trip_type_counts)

# 12. Location Analysis: Which pickup and drop-off locations (PULocationID, DOLocationID) 
#     have the highest demand for taxi services? Are there any particular patterns or clusters of popular locations?

# You can use the PULocationID and DOLocationID columns along with external data or a map to analyze location-based insights.

# 13. Congestion Surcharge: How frequently is the congestion surcharge applied? 
#     Is there any correlation between congestion surcharge and trip duration or distance?
plt.hist(df['improvement_surcharge'], bins=30, edgecolor='black')
plt.xlabel('Improvement Surcharge')
plt.ylabel('Frequency')
plt.title('Distribution of Improvement Surcharge')
plt.show()

correlation_surcharge_duration = df['improvement_surcharge'].corr(df['trip_duration_minutes'])
correlation_surcharge_distance = df['improvement_surcharge'].corr(df['trip_distance'])
print(f"Correlation between improvement surcharge and trip duration: {correlation_surcharge_duration:.2f}")
print(f"Correlation between improvement surcharge and trip distance: {correlation_surcharge_distance:.2f}")

# 14. Time-based Analysis: Can you identify peak hours or time intervals with the highest demand for taxi services? 
#     Are there any variations in fare amounts or trip duration during different times of the day?

# You can analyze the distribution of trips based on pickup timestamps to identify peak hours.

# 15. Vendor Analysis: What is the distribution of trips among different vendors (VendorID)? 
#     Is there any difference in trip duration, distance, or fare amounts based on the vendor?
vendor_counts = df['VendorID'].value_counts()
print("Frequency of Vendors:")
print(vendor_counts)

# Analyze trip duration, distance, and fare amounts for different vendors
vendor_stats = df.groupby('VendorID')[['trip_duration_minutes', 'trip_distance', 'fare_amount']].mean()
print(vendor_stats)
