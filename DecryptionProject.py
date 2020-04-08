import operator

englishText = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }


# test1 = {"A" : 1, "B" : 1}
#0
# test2 = {"A" : 0.5, "B": 1.5}
#.25


def populationVariance(population):
    size = len(population)
    popSum = 0
    for i in population:
        popSum += population[i]
    mean = popSum/size
    squaredDifference = 0
    for i in population:
        squaredDifference += (population[i] - mean)**2
    return squaredDifference/size
# 2A
print("The population variance of letters in English text is " + str(populationVariance(englishText)))
# 0.0010405667735207099


input2 = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproperuseofinformationtechnologyatumaswellastheengineeringhonorcodeasmembersoftheuniversitycommunityyouarerequiredtoabidebythesepolicies"

def frequencyAnalysis(encryption):
    all_freq = {}
    for i in encryption:
        if i in all_freq:
            all_freq[i] += 1.0/len(encryption)
        else:
            all_freq[i] = 1.0/len(encryption)
    return all_freq

# 2B
letterFrequencyInput2 = (frequencyAnalysis(input2))
popVarInput2 = populationVariance(letterFrequencyInput2)
print("The population variance of input2 is " + str(popVarInput2))
# 0.0010115330845891608
vignereTestText = "AAAAAA"
vignereKey1 = "yz"
vignereKey2 = "xyz"
vignereKey3 = "wxyz"
vignereKey4 = "vwxyz"
vignereKey5 = "uvwxyz"

# adapted from geeksforgeeks
# function to return key for any value
def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"

def vignereEncryption(key, text):
    dictAlphabet = {"A" : 1, "B" : 2, "C": 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, "K" : 11,
    "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22,
    "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}
    for letter in dictAlphabet:
        dictAlphabet[letter] -= 1
    keyLength = len(key)
    encryptedText = ""
    key = key.upper()
    text = text.upper()
    for index, letter in enumerate(text):
        encryptedIndex = ((dictAlphabet[letter] - dictAlphabet[key[index % keyLength]]) % 26)
        encryptedLetter = get_key(dictAlphabet, encryptedIndex)
        encryptedText += encryptedLetter
    return encryptedText

def vignereDecryption(key, text):
    dictAlphabet = {"A" : 1, "B" : 2, "C": 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, "K" : 11,
    "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22,
    "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}
    for letter in dictAlphabet:
        dictAlphabet[letter] -= 1
    keyLength = len(key)
    encryptedText = ""
    key = key.upper()
    text = text.upper()
    for index, letter in enumerate(text):
        encryptedIndex = ((dictAlphabet[letter] - dictAlphabet[key[index % keyLength]]) % 26)
        encryptedLetter = get_key(dictAlphabet, encryptedIndex)
        encryptedText += encryptedLetter
    return encryptedText
encryptedInput2 = (vignereEncryption(vignereKey1, input2))
def popVarianceList(keys, text):
    for key in keys:
        encryptedText = vignereEncryption(key, text)
        letterFrequency = frequencyAnalysis(encryptedText)
        popVariance = populationVariance(letterFrequency)
        print("For key " + key + " the population variance of the given text is " + str(popVariance))

allKeys = [vignereKey1, vignereKey2, vignereKey3, vignereKey4, vignereKey5]
allEncryptions = [vignereEncryption(vignereKey1, input2), vignereEncryption(vignereKey2, input2), vignereEncryption(vignereKey3, input2),
                  vignereEncryption(vignereKey4, input2), vignereEncryption(vignereKey5, input2)]
# 2C
popVarianceList(allKeys, input2)
# The variation appears to decrease as the length of the string increases. The decrease also decreases in magnitude.
# This is because the keys are becoming more and more "random" (more like well-distributed), causing each letter to
# become equally frequent.

def vignereVarianceDecrypter(keyLength, encryption, printFrequency = False):
    allVariances = []
    allVariancesNumbers = []
    for i in range(keyLength):
        allVariances.append("")
    for index, letter in enumerate(encryption):
        allVariances[(index % keyLength)] += letter
    for i in range(keyLength):
        letterFrequency = frequencyAnalysis(allVariances[i])
        allVariancesNumbers.append(populationVariance(letterFrequency))
        if printFrequency:
            print(dict( sorted(letterFrequency.items(), key=operator.itemgetter(1),reverse=True)))
    if printFrequency:
        return
    return sum(allVariancesNumbers)/keyLength
def vignereVarianceDecrypterList(keys, encryptions):
    for index, key in enumerate(keys):
        variance = vignereVarianceDecrypter(len(key), encryptions[index])
        print("For key " + key + " the population variance of the vignere sequence viewed as a collection "
                                 "of caesar cyphers is " + str(variance))
    return

# 2D
print(vignereVarianceDecrypterList(allKeys, allEncryptions))
# The variances are much closer to the variance from part b because we've essentially taken the same exact string,
# the only difference is we moved the letters a certain distance from their starting place.
encryptionuvwxyz = vignereEncryption(vignereKey5, input2)
# 2E
for i in range(2, 6):
    popVar = vignereVarianceDecrypter(i, encryptionuvwxyz)
    print("The population variance when using key length on the encrypted vignere sequence " + str(i) + " is " +
          str(popVar))
# Yes, the population variance when using the correct key length is much higher than when using an incorrect key length.
# This is for reasons explained in the last part. Clearly, any incorrect key length has a much more evenly distributed
# character count when seen as independent caesar cyphers, while the correct one has a character count distribution
# closer to that of the English language.


# problem 1
encryption2 = "ZOHESTFZOWZUPGEEGZZMGZGDZFRNUDWJHYYFNPHELCETTZBJYDEMPWEEMSVPRRLPILXCWRTEGTSNRTAEEVVPQACPJVPKRPLZICMSZYGNFKWPHOERFOXLYVQGRPEVVEAVPCBDCZTNLBEMFJFDHNGXYYTZCWSEETBKMQVPCMSMPYDTDYMZEDZFJKMREAVFLQSESOKYDEQFZCMRVPCMGCDSZYOCGZFZCARRUOYZFMCDYAPFJMZAWOOKYXEEDTRAQIEEVVUTOWPGEMIDPYRZQOLZDIICQPTDCUCQLPGOKCPPPZDCCESFDDZAUOYZTKFUSDZRFCEPZAICYDCFWHLPQBJEVVUMYHSWTFYAVPGZRMPAPOIYEIQTAZLFHPDWKPAOXLBUGYMZGWEEFHTYUJRTECPGJMYESLZWYRIYRSINDIYEOEBTAWQOEFAUCWOKCDIXEFRAWIYRHYCSUJTBKFQSECSVREOQTGKYZBFWWKRGRYDCLRUTOZSJLFWZCYKFMTHLMJMYEETAVQUMUFGKRDYTYUKMSEELQFLZENEWFLUWTWZJYKBJEVVUMYLYRZBANEHOERFORZHFMRACLTZCXDMFHKFQSYZKUCZIDDIVTMSEWMFTQRDEOKCPTSPRRLSECDHFSECTEWQCZSTYHVPYSZQGGWUNRMSTYGSPEVVDMCEZTKFQMLEHVPUSESOKMGRTYHVJXIRPBTCMGPYQZCEACPDICFTJDQISBUWZIJYNOFEIJNQRDZBJNQOAWSFLGSDZWCUTAEEVFQQDTDQCMEUCPGUGPIOPBKGRYHLGVVOEDDSJMHECDSRQIIESFVQBENEHFNQOAWSNFAACPBFRUNESWJAAUYEFPYXOEZTKFASPSOMCNEPYTZVQDOZBKRMKPXMNMDDQZFZRFHPCSNYEAYTBUCBEYOSERBAYPZKFMTUFGKEDAOPRKFQRPQCIKETSLHNCEEEFDKMMVZTRKFASPNVRPSEDMIKGGNOPFJRMNOEVRRFHLEFRGEEODIJNUCTZBJQAWPCSTMZCPCBVBMBZFHGPUVLNMNCPOYEKRLFGZGSILYEYEHFZQLZZYZLSTSCCLETEGPFPZADJDDYMZEDHWCJKNTWZPUUTSZIKYZYVTBUMROGPFJGSHEZFGPABLMZVAMUDPCIYOLPLFJCZSPEVRRUTDEOIEQTPOOKQAMPZBVUTOXTUYRNELHFFLSDZPF"
for i in range(2, 10):
    popVar = vignereVarianceDecrypter(i, encryption2)
    print("The population variance when using key length on the encrypted vignere sequence " + str(i) + " is " +
          str(popVar))
# Clearly, the key is of length 7 as this is close to the population variance of english text and much higher
# than any other population variance.
vignereVarianceDecrypter(7, encryption2, True)
print(dict(sorted(englishText.items(), key=operator.itemgetter(1), reverse=True)))



print((vignereDecryption("MALVBGY", encryption2))) # Subtracting E from the most popular letter of each frequencydict.
# Seeing some four letter combinations. Therefore, I'll keep MAL___Y
print((vignereDecryption("MALGMRY", encryption2))) # Subtracting E  from the second most common in the frequencydict,
# while keeping the four letter combination. Seeing some five letter combinations.
print((vignereDecryption("MALLMRY", encryption2))) # After playing around more, Subtracting T from the second most common in
# the frequencydict, while keeping the five letter combination. Seeing some six letter combinations.
# Furthermore, we can see that the two Ls share many letters in the frequency analysis at the same relative places.

# At this point, it is very obvious what the last letter is. For example, "NOWTGCHNOLOIY" is clearly "NOWTECHNOLOGY".
# Shifting this final letter over gives us the following answer.
print((vignereDecryption("MALLORY", encryption2)))
