import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from textblob import TextBlob
import pandas as pd
import streamlit as st


# Streamlit app
st.header('Sentiment Analysis')

# Input receiver's email
receiver_email = st.text_input('Enter receiver\'s email:')

# Function to send email with attachment
sender_email = "ishusingh40064@gmail.com"
password = "ywohtiurfbbehqjk"
def send_email(subject, body, attachment_path):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender_email, password)

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        # Attach the sentiment file
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename= {attachment_path}")
            message.attach(part)

        st.text("Sending result to email...")
        progress_bar.progress(20)
        
        # Send email
        smtp.sendmail(sender_email, receiver_email, message.as_string())
        progress_bar.progress(100)

        st.text("Email sent successfully!")

# Analyze Text
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))

# Analyze CSV
with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'

    if upl:
        df = pd.read_csv(upl)

        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)

        # Show top 5 comments with highest score
        st.subheader('Top 5 Comments with Highest Score:')
        top_comments = df.nlargest(5, 'score')
        st.table(top_comments[['tweets', 'score', 'analysis']])

        # Show bottom 5 comments with least score
        st.subheader('Bottom 5 Comments with Least Score:')
        bottom_comments = df.nsmallest(5, 'score')
        st.table(bottom_comments[['tweets', 'score', 'analysis']])

        # Calculate and display overall sentiment
        overall_sentiment = df['score'].mean()
        overall_sentiment_label = analyze(overall_sentiment)
        st.subheader('Overall Sentiment:')
        st.write(f'The overall sentiment for the entire dataset is: {round(overall_sentiment, 2)}')
        st.write(f'Sentiment Label: {overall_sentiment_label}')

        # Save the DataFrame to a CSV file
        sentiment_file_path = 'sentiment.csv'
        df.to_csv(sentiment_file_path, index=False)

        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )

        # Send email with sentiment label and sentiment file attachment
        if receiver_email:
            progress_bar = st.progress(0)
            send_email("Sentiment Analysis Result", f"The overall sentiment is: {overall_sentiment_label}", sentiment_file_path)

