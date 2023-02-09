# DRIVEN BY DATA
## Fraud App Detection 

___

## Idea and Implementation
Fraudulent App Detection in the financial sector. Our solution aimed at providing a comprehensive self sufficient software that could detect fraudulent apps both reactively and proactively in areas such as betting, investment, loan fraud, and fantasy sports on the Google Play Store before or even after they could commence operations and harm unsuspecting citizens.

Using Microsoft Azure for compute power, we collected various information from the Google Play Store using a scraper and developed a host of 8 models to detect fraudulent apps, including sentiment analysis, RC analysis, version tracer, description model, developer record analysis, and metric analysis, most of which were based on machine learning and other heuristic algorithms and were trained on data from official sources.


## How To Use
1. Download  all the Python Libraries

google-play-scraper
difflib
re
urllib
numpy
cv2
skimage.metrics
structural_similarity
csv handler
envelope
path lib
path
csv
language_tool_python
pandas
pickle
timer
time

2. Run all the files excluding Driver 3,FDriver.ipynb
3. In Driver3 
Set FROM, PASS AND TO USING  https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317
CAP in Driver3- max number of items to be sent in the mail.
Run Driver3.ipynb
In FDriver.ipynb set FIRST=1 the first time it’s being used, and change it to zero after that.
Run FDriver.ipynb


