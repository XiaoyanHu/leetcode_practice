class Solution(object):
    def reverse(self, x):
        if abs(int(x))>2147483647:
            return 0
        else:
            strx=str(x)
            lenx=len(strx)
            i=lenx-1
            if '-'in strx:
                orix='-'
                while i >0 :
                    orix=orix+strx[i]
                    i=i-1
                if abs(int(orix))>2147483647:
                    return 0
                else:
                    return int(orix)
            else:
                orix=''
                while i>=0:
                    orix=orix+strx[i]
                    i=i-1
                if int(orix)>2147483647:
                    return 0
                else:
                    return int(orix)
    
###sample resolution####   
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
            
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x = x/10
        
        if rev > 2147483647:
            return 0
        else:
            return rev * flag
