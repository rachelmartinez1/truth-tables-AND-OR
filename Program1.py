#Program 1
#Rachel Martinez

def menu():
    tableType = input("Do you want to AND or OR the propositional values: ").lower()
    if tableType != 'and' and tableType != 'or':
        print("This is invalid input.")
        menu()

    NOTp = input("Do you want to NOT p: ").lower()
    if NOTp != 'yes' and NOTp != 'y' and NOTp != 'no' and NOTp != 'n':
        print("This is invalid input.")
        menu()

    NOTq = input("Do you want to NOT q: ").lower()
    if NOTq != 'yes' and NOTq != 'y' and NOTq != 'no' and NOTq != 'n':
        print("This is invalid input.")
        menu()
    else: 
        return NOTp, NOTq, tableType


def statementBuilder(NOTp, NOTq, tableType):
    if NOTp == 'yes' or NOTp == 'y':
        NOTpSymb = '~'
    else:
        NOTpSymb = ''

    if NOTq == 'yes' or NOTq == 'y':
        NOTqSymb = '~'
    else:
        NOTqSymb = ''

    if tableType == 'and':
        tableTypeSymb = 'A'
    else: 
        tableTypeSymb = 'V'

    #Building 2D Array/Table
    table = [
        ['p','q','x'],
        ['T','T','x'], 
        ['T','F','x'], 
        ['F','T','x'], 
        ['F','F','x']
    ]

    table[0][2] = "[" + NOTpSymb + "p " + tableTypeSymb + " " +  NOTqSymb + "q" + "]"

    return table

# sandbox = p

def truthTableCompute(table, tableType, NOTp, NOTq):
    #AND LOGIC
    if tableType == 'and':

        #Only T if both stay as they are
        if table[1][0] == 'T' and table[1][1] == 'T' and NOTp != 'yes' or NOTp != 'y' and NOTq != 'yes' or NOTq != 'y':
            table[1][2] = 'T'
        else:
            table[1][2] = 'F'

        #Only if q is negated it will be T
        if table[2][0] == 'T' and table[2][1] == 'T':
            table[2][2] = 'T'
        elif NOTq == 'yes' or NOTq == 'y':
            table[2][2] = 'T'
        else:
            table[2][2] = 'F'

        #Only if p is negated it will be T
        if table[3][0] == 'T' and table[2][1] == 'T':
            table[3][2] = 'T'
        elif NOTp == 'yes' or NOTp == 'y':
            table[3][2] = 'T'
        else:
            table[3][2] = 'F'

        #Only if both are negated it will be T
        if table[4][0] == 'T' and table[4][1] == 'T':
            table[4][2] = 'T'
            return table
        elif NOTp == 'yes' or NOTp == 'y' and NOTq == 'yes' or NOTq == 'y':
            table[4][2] = 'T'
            return table
        else:
            table[4][2] = 'F'
            return table


    elif tableType == 'or':
        #Only if Both are negated it will be F
        if table[1][0] == 'T' or table[1][1] == 'T':
            table[1][2] = 'T'
        elif NOTp == 'yes' or NOTp == 'y' and NOTq == 'yes' or NOTq == 'y':
            table[1][2] = 'F'
        else:
            table[1][2] = 'T'

        #Only if p is negated it will be F
        if table[2][0] == 'T' or table[2][1] == 'T':
            table[2][2] = 'T'
        elif NOTp == 'yes' or NOTq == 'y':
            table[2][2] = 'F'
        else:
            table[2][2] = 'T'

        #Only if q is negated it will be F
        if table[3][0] == 'T' or table[3][1] == 'T':
            table[3][2] = 'T'
        elif NOTq == 'yes' or NOTq == 'y':
            table[3][2] = 'F'
        else:
            table[3][2] = 'T'

        #If either or both are negated it will be T
        #It will only be F if it stays how it is
        if table[4][0] == 'T' or table[4][1] == 'T':
            table[4][2] = 'T'
        elif NOTp == 'yes' or NOTp == 'y' or NOTq == 'yes' or NOTq == 'y':
            table[4][2] = 'T'
        elif NOTp == 'yes' or NOTp == 'y' and NOTq == 'yes' or NOTq == 'y':
            table[4][2] = 'T'#this just covers if or is not exclusive
        else:
            table[4][2] = 'F'

    return table

def printTable(table):
    for r in table:
        for c in r:
            print(c,end = " ")
        print()


def main():
    NOTp, NOTq, tableType = menu()
    statementBuilder(NOTp, NOTq, tableType)
    table = statementBuilder(NOTp, NOTq, tableType)
    truthTableCompute(table, tableType, NOTp, NOTq)
    printTable(table)

if __name__ == "__main__":
    main()