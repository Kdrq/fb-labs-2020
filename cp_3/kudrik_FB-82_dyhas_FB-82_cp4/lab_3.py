from collections import Counter

alf=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
file=open("03.txt","r",encoding="UTF-8")
text=file.read().lower().replace("\n", "").replace(" ", "")

def bigram_to_int(bigram, letter_index, abc_length):
    return letter_index[bigram[0]]*abc_length+letter_index[bigram[1]]

def inverse(a, mod):
    for number in range(mod):
        if number * a % mod == 1:
            return number
    return 0

def gcd(x, y):

    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y

def equation(x_c, a, mod):   
    a=(mod+a)%mod
    x_c=(mod+x_c)%mod
    divider=gcd(a,mod)
    answers = []
    if(x_c%divider)==0:
        x_c_inverse=inverse(a//divider,mod//divider)
        for answer_number in range(divider):
            x=(x_c_inverse*(x_c//divider)+answer_number*(mod//divider))%mod
            answers.append(x)
    return answers


def rawtext(abc):
    abclen=len(abc)
    letter_index={abc[key]:key for key in range(abc_length)}
    index_letter={key:abc[key] for key in range(abc_length)}
    return letter_index, index_letter


def find_keys(most_used_our_biggrams, most_used_language_biggrams, abc):
    print(f"From lang: {most_used_language_biggrams}")
    print(f"From text: {most_used_our_biggrams}"+"\n")
    abc_length = len(abc)
    letter_index,_= rawtext(abc)
    most_used_our_biggrams=list(map(lambda x:bigram_to_int(x,letter_index,abc_length),most_used_our_biggrams))
    most_used_language_biggrams=list(map(lambda x:bigram_to_int(x,letter_index,abc_length),most_used_language_biggrams))
    can_be_key=[]
    mod=abc_length**2
    for pop_lan_big_ind1 in range(len(most_used_language_biggrams)-1):
        for pop_lan_big_ind2 in range(pop_lan_big_ind1+1,len(most_used_language_biggrams)):
            for pop_text_big_ind1 in range(len(most_used_our_biggrams)):
                for pop_text_big_ind2 in range(len(most_used_our_biggrams)):
                    if not pop_text_big_ind1==pop_text_big_ind2:
                        Y1, Y2=most_used_our_biggrams[pop_text_big_ind1],most_used_our_biggrams[pop_text_big_ind2]
                        X1, X2=most_used_language_biggrams[pop_lan_big_ind1],most_used_language_biggrams[pop_lan_big_ind2]
                        a_s=equation(Y1-Y2, X1-X2, mod)
                        b_s=list(map(lambda x:(((Y1-x*X1)%mod)+mod)%mod,a_s))
                        keys=list(map(lambda k:(a_s[k],b_s[k]),range(len(a_s))))
                        for key in keys:
                            can_be_key.append(key)
                        print(f"{Y1}=a*{X1} + b mod {mod}")
                        print(f"{Y2}=a*{X2} + b mod {mod}\n")
    print(f"Keys: {can_be_key}\nAmount: {len(can_be_key)}\n")
    return list(set(can_be_key))

def index_accordance(text):
    letter_index=Counter(text)
    letter_amount=len(text)
    letter_index=list(sorted(letter_index.items(), key=lambda t:t[0]))
    i_c=0
    for pair in letter_index:
        i_c+=(pair[1]*(pair[1]-1))/(letter_amount*(letter_amount-1))
    return i_c

def index_in_bigram(integer, index_letter, abc_length):
    return index_letter[(integer-integer%abc_length)/abc_length]+index_letter[integer%abc_length]   


def selection(e_bigramed_text, can_be_key, abc):
   defaultt=0.055
    delta=0.005
    abc_length=len(abc)    
    letter_index,index_letter=rawtext(abc)
    mod=abc_length**2
    result=[]
    for key in can_be_key:
        a_inverce=inverse(key[0],mod)
        if not a_inverce==0:
            e_bigram=list(map(lambda x: bigram_to_int(x,letter_index,abc_length),e_bigramed_text))
            d_bigram=list(map(lambda x: a_inverce*(x-key[1]+1000*mod)%mod,e_bigram))
            d_bigram_text=list(map(lambda x: index_in_bigram(x,index_letter,abc_length),d_bigram))
            d_text="".join(d_bigram_text)
            i_c=index_accordance(d_text)
            ifdefault-default_delta<i_c<default+default_delta:
                result.append((key,i_c,d_text))
    return result

def substitution(encoded_text, abc):
    print(f"{abc}\n")
    bigram_text=[encoded_text[i:i+2] for i in range(0,len(encoded_text),2)]
    list_of_biggs=["ст","но","то","на","ен"][:3]
    5_most_used_our_biggrams=list(map(lambda x: x[0],Counter(bigrammed_text).most_common(5)))[:3]
    can_be_key=find_keys(5_most_used_our_biggrams,list_of_biggs, abc)
    d_text=selection(bigrammed_text,can_be_key,abc)
    return d_text


decoded_variants=substitution(text, alf)
for triplet in decoded_variants:
    print(f"Key: {triplet[0]}\nConformity index: {triplet[1]}\nDecoded: {triplet[2]}")

print(equation(11, 22, 33))