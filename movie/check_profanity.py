import urllib

def read_text():
    quotes = open("C:\Users\sanja\OneDrive\Desktop\Udacity Python\Intro to Python\movie\moviequotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alet!!")
    elif "false" in output:
        print ("No Profanity")
    else:
        print ("Cannot read the document")
    
read_text()
