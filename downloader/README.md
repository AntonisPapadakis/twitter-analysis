# Twitter Followers IDs Downloader
Το πρόγραμμα κατεβάζει τα IDs των ακόλουθων των λογαριασμών Twitter και τα αποθηκέυει σε ένα csv αρχείο
σαν ακμές ενός γράφου με κόμβους τους λογαριασμούς και τους ακόλουθούς τους.    
## Εγκατάσταση
1. Κατεβάζουμε τα αρχεία download.py και setup.py
2. Δημιουργούμε και ενεργοποιούμε ένα virtual environment.
3. Εκτελούμε την εντολή pip install --editable .
## Χρήση
Η εντολή που εκτελούμε κατά την εγκατάσταση εγκαθιστά τις απαραίτητες βιβλιοθήκες και μας επιτρέπει να 
τρέχουμε το πρόγραμμα σαν CLI εφαρμογή ως εξής:\
download ACCOUNTS_FILE CREDENTIALS_FILE --dest FILE_DESTINATION
## Requirements
python-twitter\
requests\
click