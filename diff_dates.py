from datetime import date
class Solution:
    def daysBetweenDates(self, date1, date2):
        day1 = list(map(int,str(date1).split('-')))
        day2 = list(map(int,str(date2).split('-')))
        date_one = date(day1[0],day1[1], day1[2])
        date_two = date(day2[0],day2[1], day2[2])
        diff_date = date_one - date_two
        return abs(diff_date.days)

def main():
    date1 = "2019-05-29"
    date2 = "2019-06-30"
    sol = Solution()
    print(sol.daysBetweenDates(date1, date2))
if __name__ == '__main__':
    main()