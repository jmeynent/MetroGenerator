import pandas as pd 
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer,AutoModelForCausalLM
from huggingface_hub import login

#Import data to have training data
idf = pd.read_csv('data/idf.csv', sep=";")
marseille = pd.read_csv('data/marseille.csv', sep=";")

name_idf = idf['nom_long']
name_marseille = marseille['Long Name']

names = pd.concat([name_idf, name_marseille], ignore_index=True)
names = names.to_frame(name="noms")


# Load model directly
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-Small-24B-Instruct-2501")
#model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-Small-24B-Instruct-2501")

if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    #model.resize_token_embeddings(len(tokenizer))
    
batch_size = 1000  # Ajuste selon la RAM dispo
tokenized_names = []

for i in range(0, len(names), batch_size):
    batch = names["noms"].iloc[i : i + batch_size].tolist()
    tokenized_names.extend(tokenizer(batch, padding="max_length", truncation=True)["input_ids"])