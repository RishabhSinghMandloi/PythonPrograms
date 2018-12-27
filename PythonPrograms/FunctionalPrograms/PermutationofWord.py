# @Purpose To find all the permutations of the String
# @aurthor Rishabh Singh
# @version  3.7
# @since 26/12/2018


from UtitlitiesMethod import Utility
try :
    def permutation(list):
        if len(list) == 0:
            return []
        elif len(list) == 1:
            return [list]
        else:
            l = []
            for i in range(len(list)):
                x = list[i]
                xs = list[:i] + list[i + 1:]
                for p in permutation(xs):
                    l.append([x] + p)
            return l


    data = input("Enter your string \n")
    data1 = list(data)

    for p in permutation(data1) :
        print(p)

except Exception as e:
    print("Invalid input")


