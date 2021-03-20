def read_file(EmpCount):
    count=EmpCount
    r=open('sample_input.txt','r')
    lines=r.readlines()

    process=False
    inp_dict={}
    for line in lines:
        actual = line.strip('\n')
        if 'Goodies and Prices' in actual:
            process = True
            continue

        ## Convert the input in the form of dictionary
        if process and actual != '':
            text = actual.split(':')
            inp_dict[text[0]]=int(text[-1].strip(' '))

    ## Sort the keys in dictionary in ascending order based on values
    sorted_dict = {}
    sorted_keys = sorted(inp_dict, key=inp_dict.get)
    for w in sorted_keys:
        sorted_dict[w] = inp_dict[w]

    items=[]
    prices=[]

    ## Split keys of sorted dictionary into items, and values into prices in List form
    items=list(sorted_dict.keys())
    prices=list(sorted_dict.values())



    prev_value=prices[count-1]-prices[0]


    ## For each loop, run until you get the minimum difference between the EmpCount
    for x in range(0,len(prices)-count):
        diff=prices[x+count-1]-prices[x]


        if prev_value > diff:
            prev_value = diff
            first_item=x
            last_item=x + count - 1

    ## Print the output to a sample_file.txt here
    output_file=open('sample_output.txt','w')
    output_file.write("The goodies selected for distribution are:"+ '\n'+'\n')

    for item in range(first_item,last_item+1):
        # print(items[item],':',prices[item])
        output_file.write(items[item]+': '+str(prices[item])+'\n')

    output_file.write('\n'+''"And the difference between the chosen goodie with highest price and the lowest price is " + str(prev_value))

    output_file.close()


## Take input of total employee count
count=int(input('Enter total employees : '))
read_file(count)