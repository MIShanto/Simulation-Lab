x0 = 0 #seed c 
a = 1 #multiplicative constant a
c = 3 #additive constant b
m = 10 # modulus
noOfRandomNums = 13 #Length of sequence. 12 random numbers will be generated

# To store random numbers
randomNums = [0] * (noOfRandomNums)
randomNums[0] = x0

print(randomNums[0],end=' ')

for i in range(1, noOfRandomNums):
    randomNums[i] = (a * randomNums[i-1] + c) % m

    print(randomNums[i],end=' ')
