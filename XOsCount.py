def XOCount(StringWord , XS):
    conclu = True
    count = [Numb for Numb in StringWord if Numb in XOs]
    numbx = [comp for comp in count if comp == 'X']
    numbo = [compo for compo in count if compo == 'O']
    if len(numbx) == len(numbo):
        print('Number of Xs and Os are:',len(numbx),len(numbo))
        print(True)
    else:
        print('Number of Xs and Os are:',len(numbx),len(numbo))
        print(False)
Word = input('Enter your word here: ')
XOs = 'XO'
XOCount(Word, XOs)
