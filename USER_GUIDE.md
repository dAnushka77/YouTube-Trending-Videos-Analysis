# CMSC 436/636 - Web Application

# How to Run:
** NOTE: Ensure you have a Python interpreter able to run Dash applications, such as virtualenv with Dash installed **

With all prerequisite models installed, path to the location of the 'app.py' file (this should be /YoutubeVis/project).
Once there, you can run the file by with the following command:
    python app.py '[FILENAME]'
Where [FILENAME] is replaced with the .csv file you want to pull data from. If a file isn't provided, a default one will be selected. 

Once the application is started, you can open it in your web browser with the link tied to it, which should be provided in the terminal you are using.

The web app will display a title, a drop down menu, a visualization, as well as some filters in the form of checkboxes and a timeline. You can open the drop down menu to choose different visualizations, the four currently implemented are:
* Scatter plot of Likes vs Views
* Grouped Bar Chart of User Engagement Metric of Videos
* Spine Chart of Average Likes and Dislikes Per Category
* Sunburst Chart of the Top 50 Most Popular Channels

The filters at the bottom of the web app allows you to change the data being presented. You can use the timeline to set a specific window from which to gather data, and the visualizations will only count data from videos published within the window. The checkboxes can be used to only display certain categories, such as Music, Gaming, Entertainment, etc. When no checkboxes are selected, all data will be shown; otherwise if you have at least one checkbox selected it will only display selected data.

# Data processing
Before running 'app.py', ensure you have 'youtube_trending_data_updated.csv.' Create it using 'clean.py,' which requires a .csv file and a .json file pair from the dataset linked,
https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset.
This file is located at (/YoutubeVis/project).

You can run the file with the following command:
    python app.py '[FILENAME.csv]' '[FILENAME1.json]'   
ex: python app.py US_youtube_trending_data.csv US_category_id.json.
The file will export as [FILENAME_updated.csv]

Make sure that the .csv and json name matches with the same region. Currently, this application defaults to US_youtube_trending_data.csv and US_category_id.json.


Note: US_youtube_trending_data.csv is not added in Github by default with its large size, manual installation into the files is necessary. There is a file US_youtube_trending_data_updated.csv that can be used immediately for app.py.


# Clearing data
If you encounter errors or unexpected behaviors:
* Restart the 'app.py' application
* Switching between different visualization might cause slight loading time

Note: As of 12/4/2023 there is no issue of this.
