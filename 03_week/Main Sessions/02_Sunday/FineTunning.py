# Step 1: Install necessary libraries
# pip install transformers datasets torch torchvision torchaudio pandas scikit-learn tqdm

# # Step 2: Import libraries
import pandas as pd
import torch
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments,
)
from datasets import load_dataset

# Step 3: Load the Sentiment140 dataset
dataset = load_dataset("sentiment140")

# Step 4: Preprocess the dataset
# Rename the 'sentiment' column to 'target'
# The dataset has 'text' and 'sentiment' as the main columns
dataset = dataset.rename_column("sentiment", "target")

# Step 5: Map the sentiment values (0 for negative, 4 for positive) to 0 and 1
dataset = dataset.map(lambda x: {"target": 0 if x["target"] == 0 else 1})
# Step 6: Tokenize the texts
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")


def tokenize_function(examples):
    return tokenizer(
        examples["text"], truncation=True, padding="max_length", max_length=128
    )


tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Step 7: Set format for PyTorch
tokenized_datasets.set_format(
    "torch", columns=["input_ids", "attention_mask", "target"]
)

# Step 8: Split the dataset into train and test
train_dataset = tokenized_datasets["train"]
test_dataset = tokenized_datasets["test"]

# Step 9: Initialize the model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Step 10: Set training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=100,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# Step 11: Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Step 12: Fine-tune the model
trainer.train()

# Step 13: Evaluate the model
trainer.evaluate()

# Step 14: Save the model
model.save_pretrained("./sentiment_model")
tokenizer.save_pretrained("./sentiment_model")
