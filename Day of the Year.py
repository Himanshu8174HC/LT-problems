class Solution:
    def dayOfYear(self, date: str) -> int:
        dates = date.split('-')
        y, m, d = int(dates[0]), int(dates[1]), int(dates[2])
        
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        countDays = 0
        i = 0
		
        while i < m - 1:
            countDays += months[i]
            i += 1
			
        if i>=2 and y%4==0 and y>1900:
            countDays += 1
			
        countDays += d
        return countDays
