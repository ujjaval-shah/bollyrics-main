import random, json

def Rand(start, end, num):
    return random.sample(range(start, end),num)

def generate(r_scheme):

    dicttemp = {}

    fp = open("dict_3_standard_2.json","r")
    dict3 = json.load(fp)
    fp.close()

    count = 1
    # maxima: number of possible 3-grams
    # maxima = max([int(i[1:]) for i in dict3.keys()])
    # print(maxima)


    # convert structure of dict3
    ##

    fp = open("dict_1.json","r")
    dict1 = json.load(fp)
    fp.close()
    #
    # fp = open("dict_2.json","r")
    # dict2 = json.load(fp)
    # fp.close()


    # stanza: stanza length 
    stanza = 4              
    # r_scheme = input()
    # print(r_scheme)
    types = list(set(i for i in r_scheme))


    # rhyme deciding
    rhymes_list = []
    fp = open("rhymes.json","r")
    rhymes_list = json.load(fp)
    # print("RHYMES loaded")
    fp.close()

    new_keys = [i for i in rhymes_list.keys() if len(rhymes_list[i])>=stanza]
    randlist = Rand(0,len(new_keys),len(types))


    # deciding rhymes based on 'randlist'
    n_dict_for_rhyme = {}
    c=0
    for i in types:
        n_dict_for_rhyme[i] = new_keys[randlist[c]]
        c = c + 1

    main_dic_for_rhyme = {}
    for i in types:
        main_dic_for_rhyme[i] = []
        for j in (Rand(0,len(rhymes_list[n_dict_for_rhyme[i]]),stanza)):
            main_dic_for_rhyme[i].append(rhymes_list[n_dict_for_rhyme[i]][j])

    # print(n_dict_for_rhyme)
    # print(main_dic_for_rhyme)

    rhyme = []
    for i in range(stanza):
        for j in r_scheme:
            rhyme.append(main_dic_for_rhyme[j][i])
        rhyme.append(" ")
    # print(rhyme)


    # Generating poem
    poem = []
    final = []
    for i in rhyme:
        if i==" ":
            poem.append(" ")
        else:
            while(True):
                if len(final)>5 and len(final)<11:
                    poem.append( (" ").join(final[1:]) )
                    final = []

                    break
                else:

                    previous = (i.split())[0:2]
                    final = previous
                    # print(previous[0],previous[1], end=" ")
                    predicted = ""
                    check= []
                    while(True):
                        if predicted == "<start>":
                            break
                        ind = dict3['keys_'].index(previous)
                        if ind >= 0:
                            # print(3,end=" ") 
                            predicted = random.choice(dict3['values_'][ind])
                            # print("tri")
                        else:
                            # print(1,end=" ")
                            predicted = random.choice(dict1["TOKENS"])
                            # print("uni")
                        # print(predicted, end=" ")
                        previous = [predicted , previous[0]]
                        final = [predicted] + final            

    return poem