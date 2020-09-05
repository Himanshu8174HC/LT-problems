class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}
        k = date.split()
        
        if k[0][1:] in ('st','th','rd','nd'):
            k[0] = '0'+k[0][0]
        else:
            k[0] = k[0][0:2]
        
        k[1] = month[k[1]]

        
        return '-'.join(reversed(k))       
        
