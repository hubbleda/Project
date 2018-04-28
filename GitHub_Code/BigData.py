
#C:\Users\Zach\Documents\cse335\reviews_Books_5.json
#import pandas as pd

# get all the paths and files open
path="Books_5.json"
#user_path="C://Users//Zach//Documents//cse335//reviews_Books_5.json//users.txt"
#books_path="C://Users//Zach//Documents//cse335//reviews_Books_5.json//books.txt"
output_path="outputDir//output.csv"
output_f=open(output_path,"w")
f=open(path,"r")
#user_file=open(user_path,"w")
#books_file=open(books_path,"w")

#import time to print out time messages and csv to write to a csv file
import time
import csv

# parse through the massive JSON file
def parse(file):

    for line in file:



        yield eval(line)


# create the dictionaries for the users and books
#user_dict is a dictionary of user id's and the number of reviews the have
# books is a dictionary of books ids and the number of reviews they have
def getDicts(file):
    # gets the dataframe
    i = 0
    # make dictionary that will be converted to datframe
    # make dictionaries for unique users and books

    users={}
    books={}
    # for each line in the JSON file
    start_time1 = time.time()
    for d in parse(file):
    # limit it to 100 lines for now

        # dataframe at that location is that JSON line

        i += 1
        # the user_id in the line and the book_id
        user_id=d['reviewerID']
        book_id=d['asin']

        # if user_id hasn't shown up before, make it 1 in the in the dict
        # if it has shown up increment it
        if user_id not in users:
            users[user_id]=1
        else:
            users[user_id]+=1
        if book_id not in books:
            books[book_id]=1
        else:
            books[book_id]+=1
        # prints out if we've looked at 10,000 entries
        if i % 10000==0:
            print("looked at "+str(i)+" items")
            curr_time=time.time()
            the_time= str((curr_time - start_time1))
            print("--- "+str(the_time)+" seconds ---"  )
            start_time1=time.time()
    print("number of users= "+str(len(users)))
    print("number of books= " + str(len(books)))
    #for item in books:
        #book_f.write(item+" "+str(books[item])+"\n")
        #print(item+" "+str(books[item]))
    #for a_user in users:
        #user_f.write(a_user + " " + str(users[a_user]) + "\n")
    #return pd.DataFrame.from_dict(df, orient='index')
    return users,books

def write_file(orig_file,user_dict,book_dict,out_file,user_threshold,book_threshold):
    # writes column names to csv
    header = "userID,bookID,score"+"\n"
    out_file.write(header)
    writer = csv.writer(out_file, delimiter=',')
    i=0
    # for every entry in the JSON file
    for entry in parse(orig_file):
        #get column data
        user_id = entry['reviewerID']
        book_id = entry['asin']
        score=entry['overall']
        i+=1
        # apply threshold and write to output.csv if it passes
        if i % 10000==0:
            print("looked at "+str(i)+" items")
            curr_time=time.time()
            the_time= str((curr_time - start_time1))
            print("--- "+str(the_time)+" seconds ---"  )
            start_time1=time.time()
        if user_dict[user_id] >= user_threshold:
            if book_dict[book_id] >= book_threshold:
                output_str=str(user_id)+","+str(book_id)+","+str(score)+"\n"
                out_file.write(output_str)
                #writer.writerow(output_str)

# get dicts
user_dict,book_dict = getDicts(f)
# close the file and open it again so the parse function starts over
f.close()
f=open(path,"r")
# write to the csv file
write_file(f,user_dict,book_dict,output_f,30,200)
#user_file.close()
#books_file.close()
f.close()