# Currently this code only focus on US data any other data as of right now needs to be manually edited to change
#
import json
import pandas as pd
import numpy as np
import sys

if __name__ == "__main__" and len(sys.argv) > 2:
    csv_data_path = str(sys.argv[1])
    json_data_path = str(sys.argv[2])
else:
    csv_data_path = 'US_youtube_trending_data.csv'
    json_data_path = 'US_category_id.json'

file_encoding = "utf-8"


if __name__=="__main__":
    with open(json_data_path, 'r') as json_file:
        data = json.load(json_file)

    titles = []
    ids = []

    # inserts json data into the array
    for item in data['items']:
        ids.append(item['id'])
        titles.append(item['snippet']['title'])

    # testing - printing out array value
    #for i in range(len(ids)):
    #    print(f"ID: {ids[i]}, Title: {titles[i]}")

    data = pd.read_csv("US_youtube_trending_data.csv")

    print(data['categoryId'].head(5))
    data['categoryName'] = data['categoryId'].astype(str)

    for i in range(len(data)):
        category_id = data.at[i, 'categoryName']
        for j in range(len(ids)):
            if category_id == ids[j]:
                data.at[i, 'categoryName'] = titles[j]
                break

    columns_to_drop = ['video_id', 'tags', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'description']
    data = data.drop(columns=columns_to_drop)


    reshaped_data = np.array(data).reshape(-1, len(data.columns))
    df = pd.DataFrame(reshaped_data, columns=[data.columns])
    df.to_csv(csv_data_path.replace('.csv', '_updated.csv'), index=False)
