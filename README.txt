
This project detects whether an email message is SPAM or NOT SPAM using Machine Learning. It uses the Naive Bayes algorithm to classify messages based on their content.

1. email.csv        - Dataset with email text and labels (1 = spam, 0 = not spam)
2. spam-detector.py - Python script to train the model and test spam messages
3. README.txt       - Project description and instructions


- Python 3.x
- pandas
- scikit-learn

Install required libraries using:
pip install pandas scikit-learn


1. Make sure all files are in the same folder.
2. Open terminal or command prompt in that folder.
3. Run the Python file:
   python spam-detector.py


- Loads email data from `email.csv`
- Converts email text to numerical features
- Trains a Naive Bayes model
- Tests the model and shows accuracy
- You can input your own sample message to check if it’s spam
