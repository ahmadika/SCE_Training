authors = []
auth = open('authors.txt', 'r')
for line in auth:
    authors.append(line.split())
auth.close()
authors_seed = open('authors_seeds.txt', 'w')
for word in authors:
    authors_seed.write('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+word[1]+'+'+word[0]+'+ocean&btnG=')
    authors_seed.write('\n')
authors_seed.close()