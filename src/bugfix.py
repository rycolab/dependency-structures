from algorithms import *
from test_algorithms import *
from terms import *

enc_proj = encode_proj(proj1)
term1 = Term((0, 1), Term((1, 0), Term((0, 1), Term((1,0), Term((0), ())))))

term1 =      Term((0, 1), [None, Term((1, 0), [Term((0, 1), [Term((1,0), [Term((0), [()])]), None]), None])])
#term1_copy = Term((0, 1), [None, Term((1, 0), [Term((0, 1), [(), Term((1, 0),[Term((0,),[(),])(),])])(),])])
t2 = Term((1,1),Term("oa1",Term("oa2",())))
def visualize(t : Term):
    l = []
    def rec(t: Term, l):
        if t is None or t == ():
            l.append(())
            return
        l.append(t.oa)
        
        for child in t.lst:

            rec(child,l)
    rec(t,l)
    return l

# print("term1:",visualize(term1))
# print("enc:",visualize(enc_proj))
# print(proj1)


def termer(t:Term):
    print("Term(",end='')
    print(t.oa,end=',[')
    for c in t.lst:
        if c is None or c == ():
            print("()",end=',')
        else:
            termer(c)
    print("])",end='')

print("term1:",visualize(term1))
termer(enc_proj)
print()
        
print(decode_proj(encode_proj(proj1)))
print(proj1)
# visualize(term1)
# print("------")
# visualize(enc_proj)
