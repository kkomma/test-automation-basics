class FBPrep:
    def answerQueries(queries, N):
        output = []
        boolsArray = [False]*len(queries)
        boolsSet = set()

        for query in queries:
            if query[0] == 1:
                boolsArray[query[1]-1] = True
                boolsSet.add(query[1]-1)
            else:
                if len(boolsSet) == 0:
                    output.append(-1)
                else:
                    s = sorted(list(boolsSet))
                    for idx in s:          
                        if idx+1 >= query[1]:
                            output.append(idx+1)
                        else:
                            output.append(-1)
        return output
        
    if __name__=="__main__": 
        N = 5
        queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
        print(answerQueries(queries, N))