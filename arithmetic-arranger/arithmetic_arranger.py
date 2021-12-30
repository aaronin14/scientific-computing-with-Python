def arithmetic_arranger(problems,calculate=False):
    operator = list()    
    first_num = list()
    second_num = list()
    result = list()
    ndashes = list()
    num_of_problem = len(problems)

    # Too many problems
    if num_of_problem > 5 or num_of_problem < 1:
        return 'Error: Too many problems.'
        

    pieces = list()
    for problem in problems:
        pieces = problem.split()
        
        # Operator must be '+' or '-'
        if pieces[1] == '+' or pieces[1] == '-':
            operator.append(pieces[1])
        else:
            return'Error: Operator must be \'+\' or \'-\'.'        

        # Numbers must only contain digits
        try:
            pieces[0] = int(pieces[0])
            pieces[2] = int(pieces[2])
        except:
            return 'Error: Numbers must only contain digits.'


        # Number cannot be more than four digits.
        if len(str(pieces[0])) > 4 or len(str(pieces[2])) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        else:
            first_num.append(pieces[0])
            second_num.append(pieces[2])

    for i in range(num_of_problem):
        if operator[i] == '+':
            result.append(first_num[i] + second_num[i])
        else:
            result.append(first_num[i] - second_num[i])

        len1 = len(str(first_num[i]))
        len2 = len(str(second_num[i]))
        if len1 > len2:
            ndashes.append(len1+2)
        else:
            ndashes.append(len2+2)

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for i in range(num_of_problem):
        first_num[i]=str(first_num[i]).rjust(ndashes[i],' ')
        if first_line == '':
            first_line = first_num[i]  
        else:
            first_line = first_line + '    ' + first_num[i]
        
        second_num[i]=str(second_num[i]).rjust(ndashes[i]-1,' ')
        if second_line == '':
            second_line = operator[i] + second_num[i]
        else:
            second_line = second_line + '    ' + operator[i] + second_num[i]

        if third_line == '':
            third_line = '-'*ndashes[i]
        else:
            third_line = third_line + '    ' + '-'*ndashes[i]

        result[i]=str(result[i]).rjust(ndashes[i],' ')
        if fourth_line == '':
            fourth_line = result[i]
        else:
            fourth_line = fourth_line + '    ' + result[i]


    arranged_problems = first_line + '\n' + second_line + '\n' + third_line
    if calculate==True:
        arranged_problems = arranged_problems + '\n' + fourth_line






    return arranged_problems