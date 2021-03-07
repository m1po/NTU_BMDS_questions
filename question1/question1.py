###this is one method based on modulo operations to find the path where summed number descreases fastest
###however, it only proves the existence of one path rather than uniqueness

def find_operations(m,n,sum):
    #only numbers with in min and max can have paths
    max = 0.5 * (1 + m) * m + (n - 1) * m
    min = 0.5 * (1 + m) * m + (n - 1)
    if sum < min or sum > max:
        return str(sum) + ' ' + 'out of range'

    #the sum of the Down operations is always the same
    #then, study the Right opreations sum to figure out how many times one number may occur in Right operation
    steps =  m - 1 + n - 1
    col_sum = 0.5 * (1 + m) * m
    row_sum = sum - col_sum
    rowstep_count = 0
    left_toadd = row_sum

    #the first occurence of one number comes from Down operation except 1, we will fix 1 later
    dic = {i:'D' for i in range(1,m + 1)}


    for i in reversed(range(1,m + 1)):
        mod = int(left_toadd / i)
        rem = left_toadd % i

        #the sum left must be no less than row steps left for the path on the squared matrix
        #mod is the steps number i will take and fill in rem all using number 1
        while mod + rem < n - 1 - rowstep_count and mod > 0:
            mod = mod - 1
            rem = rem + i


        #record the occrence time in Right operations
        for j in range(int(mod)):
            dic[i] = dic[i] + 'R'

        rowstep_count = rowstep_count + mod

        left_toadd = rem

    #fix the first step
    dic[1]=''
    path = list(dic.values())
    path = ''.join(path)

    #if 1 only occur once, first step is Down, otherwise it is Right
    if steps-len(path) == 1:
        path = 'D' + path
    else:
        for i in range(steps-len(path)):

            path = 'R' + path
    result = str(sum)+' '+path
    return result

f = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question1/output_question_1','w')

f.write(find_operations(9,9,65) + '\n' + find_operations(9,9,72)+'\n' +find_operations(9,9,90) + '\n' + find_operations(9,9,110))
f.write('\n' + find_operations(90000,100000,87127231192)+'\n' + find_operations(90000,100000,5994891682))
f.close()
print('done')
