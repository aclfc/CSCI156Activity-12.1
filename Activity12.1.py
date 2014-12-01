__author__ = 'Aidan'
def email(x):
    at =''
    for i in x:
        if i == "@":
            at = 'yes'
    if at != 'yes':
        return(print("That is not a vlid email."))
    if x[-4] != ".":
        return(print("That is not a valid email."))
    U, D = x.split('@')
    D, gtld = D.split('.')
    if at == 'yes':
        if gtld == 'com' or gtld == 'gov' or gtld == 'edu' or gtld == 'org' or gtld == 'mil' or gtld == 'net':
            print("Username is:",U,"\nDomain is:",D,"\ngTLD is: ."+gtld)

email('aidan.calkins@gmail.com')