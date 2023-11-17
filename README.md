
# Sentiment Analysis with Email Notification

This Python script utilizes the Streamlit library to create a simple Sentiment Analysis application. The sentiment analysis is performed on both user-input text and CSV files containing text data. The results are displayed in a Streamlit app, and users have the option to download the sentiment analysis results as a CSV file. Additionally, users can provide an email address to receive the overall sentiment analysis results via email.


## Deployment

To deploy this project run

```bash
  git clone https://github.com/ishuoncode/sentiment-analysis.git
  cd your-repo
  pip install -r requirements.txt
  streamlit run main.py
```
Ensure that you have Python installed and all the required packages.




## Documentation

[Documentation](https://linktodocumentation)

The Streamlit app will open in your default web browser.
Enter the receiver's email address in the provided text input.
Analyze text sentiment by entering text in the "Analyze Text" section.
Upload a CSV file containing a column named 'tweets' to perform sentiment analysis on the CSV data.
Receive Email Notification:

If you provided a receiver's email address, the overall sentiment analysis results will be sent to that email.
Notes
The application uses the TextBlob library for sentiment analysis.
The overall sentiment label and CSV file with sentiment analysis results are available for download.
Ensure that you have allowed "Less secure app access" or used an "App Password" for the sender's email account.
Update the sender's email and password in the script with your own email credentials.
Feel free to customize and enhance the application based on your needs!

## References

1. For ML learning: https://www.youtube.com/watch?v=-YCDhHVNNLA&t=4s
2. For generating your app password and email: https://www.youtube.com/watch?v=6ANKk9NQ3GI
