def main():
    result = 0
    with open('input.txt') as infile:
        for line in infile:
            answer, terms = line.split(': ')
            answer = int(answer)
            terms = [int(x) for x in terms.split(' ')]
            if find_solution(answer, terms):
                result += answer

    print(result)

def find_solution(answer, terms):
    if len(terms) == 2:
        return (terms[0]+terms[1] == answer) or (terms[0]*terms[1] == answer)
    return find_solution(answer, [terms[0]+terms[1]]+terms[2:]) \
            or find_solution(answer, [terms[0]*terms[1]]+terms[2:])

main()
