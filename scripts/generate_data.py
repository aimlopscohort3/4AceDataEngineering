# Split dataset into train and validation
split = dataset.train_test_split(test_size=0.2)
train_dataset = split['train']
val_dataset = split['test']

print(train_dataset[:5])