import operator


top3_orig=open("top3.txt","r")
top3_final=open("top3_final.txt","w")

user=1
for line in top3_orig:
    user_str=str(user)
    output_str=user_str+','+line

    top3_final.write(output_str)
    user+=1


'''
top3={}
i=0
number_lines= 11000000
for line in pred:
    prediction=line.strip().split(',')
    user=prediction[0]
    book=prediction[1]
    actual_rating=prediction[2]
    predicted_rated=prediction[3]
    book_rating_tup=(book,predicted_rated)
    if user not in top3:
        top3[user]=[book_rating_tup]
    elif user in top3:
        if len(top3[user])!=3:
            top3[user].append(book_rating_tup)
            top3[user].sort(key=operator.itemgetter(1),reverse=True)
        elif len(top3[user])==3:
            least_popular=top3[user][2]
            least_popular_rating=least_popular[1]
            if predicted_rated > least_popular_rating:
                user_top3=top3[user]
                top3[user].pop()
                top3[user].append(book_rating_tup)
                top3[user].sort(key=operator.itemgetter(1), reverse=True)

    if i%1000000000:
        percent=(i/number_lines)*100
        print(str(percent)+" done")
    i+=1


for key in top3:
    book_user=key
    top3_books=top3[book_user]
    book1_tup=top3_books[0]
    book1_title=book1_tup[0]
    book1_rating=book1_tup[1]

    book2_tup = top3_books[1]
    book2_title = book2_tup[0]
    book2_rating = book2_tup[1]

    book3_tup = top3_books[2]
    book3_title = book3_tup[0]
    book3_rating = book3_tup[1]

    output_str=str(book_user)+","+str(book1_title)+","+str(book1_rating)+","+str(book2_title)+","+str(book2_rating)+","+str(book3_title)+","+str(book3_rating)+"\n"
    top3_file.write(output_str)
'''
top3_final.close()
top3_orig.close()



