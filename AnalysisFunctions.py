import enchant
#mallory
encryption = "CSASTPKVSIQUTGQUCSASTPIUAQJB"
encryption2 = "ZOHESTFZOWZUPGEEGZZMGZGDZFRNUDWJHYYFNPHELCETTZBJYDEMPWEEMSVPRRLPILXCWRTEGTSNRTAEEVVPQACPJVPKRPLZICMSZYGNFKWPHOERFOXLYVQGRPEVVEAVPCBDCZTNLBEMFJFDHNGXYYTZCWSEETBKMQVPCMSMPYDTDYMZEDZFJKMREAVFLQSESOKYDEQFZCMRVPCMGCDSZYOCGZFZCARRUOYZFMCDYAPFJMZAWOOKYXEEDTRAQIEEVVUTOWPGEMIDPYRZQOLZDIICQPTDCUCQLPGOKCPPPZDCCESFDDZAUOYZTKFUSDZRFCEPZAICYDCFWHLPQBJEVVUMYHSWTFYAVPGZRMPAPOIYEIQTAZLFHPDWKPAOXLBUGYMZGWEEFHTYUJRTECPGJMYESLZWYRIYRSINDIYEOEBTAWQOEFAUCWOKCDIXEFRAWIYRHYCSUJTBKFQSECSVREOQTGKYZBFWWKRGRYDCLRUTOZSJLFWZCYKFMTHLMJMYEETAVQUMUFGKRDYTYUKMSEELQFLZENEWFLUWTWZJYKBJEVVUMYLYRZBANEHOERFORZHFMRACLTZCXDMFHKFQSYZKUCZIDDIVTMSEWMFTQRDEOKCPTSPRRLSECDHFSECTEWQCZSTYHVPYSZQGGWUNRMSTYGSPEVVDMCEZTKFQMLEHVPUSESOKMGRTYHVJXIRPBTCMGPYQZCEACPDICFTJDQISBUWZIJYNOFEIJNQRDZBJNQOAWSFLGSDZWCUTAEEVFQQDTDQCMEUCPGUGPIOPBKGRYHLGVVOEDDSJMHECDSRQIIESFVQBENEHFNQOAWSNFAACPBFRUNESWJAAUYEFPYXOEZTKFASPSOMCNEPYTZVQDOZBKRMKPXMNMDDQZFZRFHPCSNYEAYTBUCBEYOSERBAYPZKFMTUFGKEDAOPRKFQRPQCIKETSLHNCEEEFDKMMVZTRKFASPNVRPSEDMIKGGNOPFJRMNOEVRRFHLEFRGEEODIJNUCTZBJQAWPCSTMZCPCBVBMBZFHGPUVLNMNCPOYEKRLFGZGSILYEYEHFZQLZZYZLSTSCCLETEGPFPZADJDDYMZEDHWCJKNTWZPUUTSZIKYZYVTBUMROGPFJGSHEZFGPABLMZVAMUDPCIYOLPLFJCZSPEVRRUTDEOIEQTPOOKQAMPZBVUTOXTUYRNELHFFLSDZPF"


# Returns the longest repeating non-overlapping
# substring in str
def longestRepeatedSubstring(str):
    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
             for y in range(n + 1)]

    res = ""  # To store result
    res_length = 0  # To store length of result

    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):

            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if (str[i - 1] == str[j - 1] and
                    LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1

                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)

            else:
                LCSRe[i][j] = 0

    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if (res_length > 0):
        for i in range(index - res_length + 1,
                       index + 1):
            res = res + str[i - 1]

    return res

# Finds a word that is off by a certain number from the given word
# def wordFinder(encryptSubstring, keyLength):
#     for i in range(26):
#         newString = ""
#         for (n, letter) in enumerate(encryptSubstring):
#             j = n % keyLength
#             k = i + j
#             number = ord(letter.upper()) + k
#             if number > 90:
#                 number -= 26
#             newLetter = chr(number)
#             newString += newLetter
#         print(newString, letter)



#the functions below estimate the size of the key
def letterFrequency(string):
    all_freq = {}
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq
def coincidenceRate(letterFrequencies, stringLen):
    numerator = 0.0
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if (letter not in letterFrequencies):
            continue
        frequency = letterFrequencies[letter]
        numerator += frequency * (frequency - 1)
    denominator = stringLen * (stringLen - 1)
    return numerator/denominator
def keyLength(coincidence):
    numerator = 0.067 - (1/26)
    denominator = coincidence - (1/26)
    return numerator/denominator
def estimatedKeyLength(encryption):
    letterFrequencies = (letterFrequency(encryption))
    coincidence = (coincidenceRate(letterFrequencies, len(encryption)))
    return (keyLength(coincidence))

def frequencyAnalysis(encryption, keyLength):
    all_freq = {}
    for i in encryption:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq
# print(estimatedKeyLength(encryption2))
# (longestRepeatedSubstring(encryption2))
# print(wordFinder(encryption2[:40], 6))
