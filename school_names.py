import pandas as pd

def main():
    print(get()[:10])

def get():
    result = []
    dataset = pd.read_excel("dataset.xlsx")
    school_names = dataset["ShortName"].tolist()
    result = [name for name in school_names if type(name) == str]
    return result

if __name__ == "__main__":
    main()
