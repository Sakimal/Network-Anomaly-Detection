import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib


df = pd.read_csv("C:\\Projects\\network-anomaly-detector\\dataset.csv", header=None)

print(df.shape)

column_names = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", 
    "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", 
    "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells", "num_access_files", 
    "num_outbound_cmds", "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", 
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", 
    "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", 
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", 
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "numeric_feature"
]


df.columns = column_names


label_encoders = {}
for column in ['protocol_type', 'service', 'flag']:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Create features (X) and label (y) sets
X = df.drop('label', axis=1)
y = df['label']

# Label binarization (1 for 'normal', -1 for anomalies)
df['anomaly'] = df['label'].apply(lambda x: 1 if x == 'normal.' else -1)
y = df['anomaly']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X_train)


joblib.dump(model, 'model.joblib')

print("Model training complete and saved as model.joblib.")
