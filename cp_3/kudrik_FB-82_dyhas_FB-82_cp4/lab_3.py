from collections import Counter

alf=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
list_of_bigs=['ст','но','то','на','ен']
file=open("03.txt","r",encoding="UTF-8")
text=file.read().lower().replace("\n", "").replace(" ", "")

def numeric_form_of_biggrams(bigram, let_index, abc_length):
    return let_index[bigram[0]]*abc_length+let_index[bigram[1]]

def inverse(a, module):
    for number in range(module):
        if number * a % module == 1:
            return number
    return 0

def gcd(x, y):

    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y

def equation(x_c, a, module):   
    a=(module+a)%module
    x_c=(module+x_c)%module
    divider=gcd(a,module)
    answers = []
    if(x_c%divider)==0:
        x_c_inverse=inverse(a//divider,module//divider)
        for answer_number in range(divider):
            x=(x_c_inverse*(x_c//divider)+answer_number*(module//divider))%module
            answers.append(x)
    return answers


def rawtext(abc):
    abclen=len(abc)
    let_index={abc[key]:key for key in range(abc_length)}
    index_letter={key:abc[key] for key in range(abc_length)}
    return let_index, index_letter


def find_keys(most_used_our_biggrams, most_used_language_biggrams, abc):
    print(f"From lang: {most_used_language_biggrams}")
    print(f"From text: {most_used_our_biggrams}"+"\n")
    abc_length = len(abc)
    let_index,_= rawtext(abc)
    most_used_our_biggrams=list(map(lambda x:numeric_form_of_biggrams(x,let_index,abc_length),most_used_our_biggrams))
    most_used_language_biggrams=list(map(lambda x:numeric_form_of_biggrams(x,let_index,abc_length),most_used_language_biggrams))
    can_be_key=[]
    module=abc_length**2
    for pop_lan_big_ind1 in range(len(most_used_language_biggrams)-1):
        for pop_lan_big_ind2 in range(pop_lan_big_ind1+1,len(most_used_language_biggrams)):
            for pop_text_big_ind1 in range(len(most_used_our_biggrams)):
                for pop_text_big_ind2 in range(len(most_used_our_biggrams)):
                    if not pop_text_big_ind1==pop_text_big_ind2:
                        Y1, Y2=most_used_our_biggrams[pop_text_big_ind1],most_used_our_biggrams[pop_text_big_ind2]
                        X1, X2=most_used_language_biggrams[pop_lan_big_ind1],most_used_language_biggrams[pop_lan_big_ind2]
                        a_s=equation(Y1-Y2, X1-X2, module)
                        b_s=list(map(lambda x:(((Y1-x*X1)%module)+module)%module,a_s))
                        keys=list(map(lambda k:(a_s[k],b_s[k]),range(len(a_s))))
                        for key in keys:
                            can_be_key.append(key)
                        print(f"{Y1}=a*{X1} + b module {module}")
                        print(f"{Y2}=a*{X2} + b module {module}\n")
    print(f"Keys: {can_be_key}\nAmount: {len(can_be_key)}\n")
    return list(set(can_be_key))



