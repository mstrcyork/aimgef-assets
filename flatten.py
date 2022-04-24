import pandas as pd
import csv

def get_category_part(idx):
    if idx in range(1, 151):
        part = 'CSQ'
    elif idx in range(151, 251):
        part = 'CPI'
    else:
        raise ValueError
    if idx in range(1, 26) or idx in range(151, 176):
        category = 'Orig'
    elif idx in range(101, 126) or idx in range(201, 226):
        category = 'MuTr'
    elif idx in range(76, 101) or idx in range(176, 201):
        category = 'MVAE'
    elif idx in range(26, 51):
        category = 'MaMa'
    elif idx in range(51, 76):
        category = 'CoRe'
    elif idx in range(126, 151):
        category = 'BeAf'
    elif idx in range(226, 251):
        category = 'LiTr'
    else:
        raise ValueError
    return category, part


def flatten_ratings(fp):
    res = [['ID', "Rating", "Category", "Aspect", "Part"]]
    df = pd.read_csv(fp)
    for row in df.iterrows():
        category, part = get_category_part(row[1]["ID"])
        for aspect in ['Ss', 'Ap', 'Re', 'Me', 'Ha', 'Rh']:
            res.append([row[1]["ID"], row[1][aspect], category, aspect, part])
    with open("ratings_flatten.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(res)

if __name__ == '__main__':
    flatten_ratings('ratings.csv')
