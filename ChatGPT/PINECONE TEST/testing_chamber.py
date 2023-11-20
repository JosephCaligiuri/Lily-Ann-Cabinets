from pinecone_datasets import load_dataset

dataset = load_dataset("squad-text-embedding-ada-002")
dataset.head()