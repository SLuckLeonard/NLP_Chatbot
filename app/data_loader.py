import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, delimiter='\t', header=None, names=['flags', 'utterance', 'category', 'intent'])
    return df

# Example usage
if __name__ == "__main__":
    data = load_data('/data/20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv')
    print(data.head())
