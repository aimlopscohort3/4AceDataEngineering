#SAMPLE--to do with actual

# 1. Load and Preprocess Dataset
def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    label_mapping = {"neutral": 0, "negative": 1, "positive": 2}
    df['label'] = df['label'].map(label_mapping)
    return Dataset.from_pandas(df)

# 2. Load Dataset
data_path = "/content/airline_sentiment_dataset.csv"  # Path to your dataset
dataset = preprocess_data(data_path)