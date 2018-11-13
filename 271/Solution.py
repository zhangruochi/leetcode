"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
"""


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return "".join([str(len(str_))+"@"+str_ for str_ in strs])
        
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """

        ans = []
        while s:
            index = s.index("@")
            j = index-1
            while j >= 0 and s[j].isdecimal():
                j -= 1
            num = int(s[j+1:index])
            ans.append(s[index+1:index+1+num])
            s = s[index+1+num:]
        return ans

if __name__ == '__main__':
    solution = Codec()
    strs = solution.encode(["4M.WqAI5=JZR>)+]VyQ@c<8Ds]pRNc@V46Su7UQ@;0K`HRXr^Vp_Q8mVfPTzW]x=~w2*d&)e _#M%8G#G*~S3",";H2XG!04+[2m0`3W;J~a?pJWA?J?44U-;V J?f7QN2kuD{c~9qeF=GCI.QnDJwwjtRgtv(QS`&Lu:>n.$c$0qGO?S","({A2+o!w2}1x(>C)[|KK8W9rjoNQ{d994p5Y:FGL*=<js&lhJ;d(Wqt;ix7M7xv|6${O4g_4w{Ml#;`M7,Nzb>","@6IE.z2Xm|SYP>F6@Om<LHsX/HI;BGDyJZ0<NfMbGws(R)}0_$<(ak)SD2F!v)n/tl,.{Ui8qoZaw@6B(5Q$}Sn KfPRs1rtOW","MP6Zi>7l3C#;@l,El/LHEJRwT","J6nHi4Kr:Y<dH6BkIuf?Q2aoo#<","EWOgW8GR~7q; +&j6QKP<~,~_@) TIijzf]AzD7&|*Hd@Ma@-B.L$<K`fx)b/mC9Pd-S,uep","W<kpbFFj.NE&1K.We$VB1^wRL,S1BLSE$6sl-6L*~*r:`jS $UR+S-svh9N+a!6%0V2oXCkX","AX{4WF:}[ozw] ]#k`zu%3-WL","1r1E/`d-/H>z7*XKy#x])0Wb}|OaC","#Fm@I0P^ZZ9a=}Lt:r7IrTC@<I+m|ox{h#9mz^w4Eu!(A","f,C[3Jw}*PjXmlC:n5B,0~f/$*%o)FuqP5EGItZ.[2ZH}qo3y)kb*P9e&71.y]/82TBZhD*b]QS<,c]VL/G","r(P}vVbb>C:(vnaHZ)`7;f[:z2dLn+[1RWIba.In(Z","e^;Pkl>=b?3%wa$OQ).9G5J#j8I8AZc&83` No6C.**~^OK~qO</<LY`2Iw!x2]gW9A@l/z!Y]~S36n~V-uhZ[NY`","eSF+TTvZe@3DYi19 3l-KL!*xvN,o?1EJGJ^2>1,>[Jy&oL+n~ ~JV%6Lo8fO~YX@+4HL+0","c(","%86$uA@?JZ_Xea5vowNT0x=R`[l=)!MgNc;Iy#C}/z0kDVVqUI|d","hLqXx?~LIfDA(J","egNpT<6!0CG=sB0+q]{0Ydco<RQy$Jiy])>mP#&d=x5];dOpyW,R","<J*yMXL:.#[WzdF6{C7`1jj;o!NJL+Zh.5}?@?Tx|5q0[]^%B%;0Pa#d9{CcM1r+o;M}eavzivp<7uv!N","[~),qD8/RFjGdY("])
    print(strs)
    print(solution.decode(strs))