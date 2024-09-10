import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the ingested data
data = pd.read_csv('ingested_data.csv')

# Example preprocessing steps
# Drop missing values
data_cleaned = data.dropna()

# Feature scaling
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_cleaned)

# Split the data into training and testing sets
X_train, X_test = train_test_split(data_scaled, test_size=0.2, random_state=42)

# Save the processed data for training
pd.DataFrame(X_train).to_csv('train_data.csv', index=False)
pd.DataFrame(X_test).to_csv('test_data.csv', index=False)

print("Data preprocessing completed and saved as train_data.csv and test_data.csv")
