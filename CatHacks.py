#######################
## Cat Hacks Project ##
## By Shahzeb Atif   ##
#######################


def getDayFromDate(readDay):
  Daya = readDay[3:6]
  return int(Daya)


def getWordEndingFromDate(determineDaySequence):
  PostFixb = determineDaySequence[5]

  if PostFixb == "1":
    Endingb = "st"

  elif PostFixb == "2":
    Endingb = "nd"

  elif PostFixb == "3":
    Endingb = "rd"

  else:
    Endingb = "th"

  return Endingb


def getMonthFromDate(readMonth):
  Monthc = readMonth[0:3]
  return Monthc


def getYearFromDate(readYear):
  Yeard = readYear[8:12]
  return int(Yeard)


def getMonthIndexFromDate(setMonthIndex):
  if setMonthIndex == "Jan":
    Indexe = 0

  elif setMonthIndex == "Feb":
    Indexe = 1

  elif setMonthIndex == "Mar":
    Indexe = 2

  elif setMonthIndex == "Apr":
    Indexe = 3

  elif setMonthIndex == "May":
    Indexe = 4

  elif setMonthIndex == "Jun":
    Indexe = 5

  elif setMonthIndex == "Jul":
    Indexe = 6

  elif setMonthIndex == "Aug":
    Indexe = 7

  elif setMonthIndex == "Sep":
    Indexe = 8

  elif setMonthIndex == "Oct":
    Indexe = 9

  elif setMonthIndex == "Nov":
    Indexe = 10

  elif setMonthIndex == "Dec":
    Indexe = 11

  return Indexe


def getMonthNameFromDate(setMonthFullName):
  if setMonthFullName == "Jan":
    FullMonthf = "January"

  elif setMonthFullName == "Feb":
    FullMonthf = "Febuary"

  elif setMonthFullName == "Mar":
    FullMonthf = "March"

  elif setMonthFullName == "Apr":
    FullMonthf = "April"

  elif setMonthFullName == "May":
    FullMonthf = "May"

  elif setMonthFullName == "Jun":
    FullMonthf = "June"

  elif setMonthFullName == "Jul":
    FullMonthf = "July"

  elif setMonthFullName == "Aug":
    FullMonthf = "August"

  elif setMonthFullName == "Sep":
    FullMonthf = "September"

  elif setMonthFullName == "Oct":
    FullMonthf = "October"

  elif setMonthFullName == "Nov":
    FullMonthf = "November"

  elif setMonthFullName == "Dec":
    FullMonthf = "December"

  return FullMonthf


def getDaysIntoYear(minimumIncrease, monthIndex, tallyCount, totalDaysInMonth, dayInputed):
  while minimumIncrease != monthIndex:
    tallyCount = tallyCount + totalDaysInMonth[minimumIncrease]
    minimumIncrease = minimumIncrease + 1

  daysIntoYear = tallyCount + dayInputed

  return daysIntoYear
  


def getSecondDayFromDate(readSecondDay):
  Dayaa = readSecondDay[3:6]
  return int(Dayaa)


def getSecondWordEndingFromDate(determineSecondDaySequence):
  PostFixbb = determineSecondDaySequence[5]

  if PostFixbb == "1":
    Endingbb = "st"

  elif PostFixbb == "2":
    Endingbb = "nd"

  elif PostFixbb == "3":
    Endingbb = "rd"

  else:
    Endingbb = "th"

  return Endingbb


def getSecondMonthFromDate(readSecondMonth):
  Monthcc = readSecondMonth[0:3]
  return Monthcc


def getSecondYearFromDate(readSecondYear):
  Yeardd = readSecondYear[8:12]
  return int(Yeardd)


def getSecondMonthIndexFromDate(setSecondMonthIndex):
  if setSecondMonthIndex == "Jan":
    Indexee = 0

  elif setSecondMonthIndex == "Feb":
    Indexee = 1

  elif setSecondMonthIndex == "Mar":
    Indexee = 2

  elif setSecondMonthIndex == "Apr":
    Indexee = 3

  elif setSecondMonthIndex == "May":
    Indexee = 4

  elif setSecondMonthIndex == "Jun":
    Indexee = 5

  elif setSecondMonthIndex == "Jul":
    Indexee = 6

  elif setSecondMonthIndex == "Aug":
    Indexee = 7

  elif setSecondMonthIndex == "Sep":
    Indexee = 8

  elif setSecondMonthIndex == "Oct":
    Indexee = 9

  elif setSecondMonthIndex == "Nov":
    Indexee = 10

  elif setSecondMonthIndex == "Dec":
    Indexee = 11

  return Indexee


def getSecondMonthNameFromDate(setSecondMonthFullName):
  if setSecondMonthFullName == "Jan":
    FullMonthff = "January"

  elif setSecondMonthFullName == "Feb":
    FullMonthff = "Febuary"

  elif setSecondMonthFullName == "Mar":
    FullMonthff = "March"

  elif setSecondMonthFullName == "Apr":
    FullMonthff = "April"

  elif setSecondMonthFullName == "May":
    FullMonthff = "May"

  elif setSecondMonthFullName == "Jun":
    FullMonthff = "June"

  elif setSecondMonthFullName == "Jul":
    FullMonthff = "July"

  elif setSecondMonthFullName == "Aug":
    FullMonthff = "August"

  elif setSecondMonthFullName == "Sep":
    FullMonthff = "September"

  elif setSecondMonthFullName == "Oct":
    FullMonthff = "October"

  elif setSecondMonthFullName == "Nov":
    FullMonthff = "November"

  elif setSecondMonthFullName == "Dec":
    FullMonthff = "December"

  return FullMonthff


def getSecondDaysIntoYear(secondMinimumIncrease, secondMonthIndex, secondTallyCount, totalDaysInSecondMonth, secondDayInputed):
  while secondMinimumIncrease != secondMonthIndex:
    secondTallyCount = secondTallyCount + totalDaysInSecondMonth[secondMinimumIncrease]
    secondMinimumIncrease = secondMinimumIncrease + 1

  daysIntoSecondYear = secondTallyCount + secondDayInputed
  return daysIntoSecondYear


def getYearsBetween(yearInput, secondYearInput, monthInput, secondMonthInput, dayInput, secondDayInput):

  findWhichGreater = secondYearInput - yearInput

  if findWhichGreater >= 0:
    differenceOfYears = findWhichGreater

  elif findWhichGreater < 0:
    differenceOfYears = findWhichGreater*(-1)

  if differenceOfYears >= 1:
    daysInBetweenYears = 365*differenceOfYears

  else:
    if secondMonthInput >= monthInput:
      daysInBetweenYears = 365*differenceOfYears

    else:
      if secondDayInput > dayInput:
        daysInBetweenYears = 365*differenceOfYears
      
      else:
        daysInBetweenYears = 0
  
  return daysInBetweenYears


def getLeapYearsWith100Rule(yearInput, secondYearInput, rangeOfYears, totalLeapYears):
  for f in range(yearInput, secondYearInput+1):
      testForLeapYear = rangeOfYears % 4
      testForLeapYearException = rangeOfYears % 100
      rangeOfYears = rangeOfYears + 1

      if testForLeapYear == 0:

        if testForLeapYearException != 0:
          totalLeapYears = totalLeapYears + 1
  
  return totalLeapYears


def getTotalDifferenceDays(differenceOfYears, sumOfDays, secondSumOfDays):
  if differenceOfYears >= 0:
    totalDifferenceDays = secondSumOfDays - sumOfDays

  elif YearDifference < 0:
    totalDifferenceDays = sumOfDays - secondSumOfDays

  return totalDifferenceDays


def getFinalAnswer(differenceOfDays):
  if differenceOfDays >= 0:
    FinalAnswer = differenceOfDays

  elif differenceOfDays < 0:
    FinalAnswer = differenceOfDays*(-1)

  return FinalAnswer

#START OF PROGRAM

programLoop = 0
date1Loop = 0
date2Loop = 0

border = "══════════════════════════════"

#Welcoming Statements
print("Find out the number of days between two dates. ")
print("Month, Day, Year // (Mmm DD, YYYY) ")
print("Examples: 'Jul 05, 2019' ")
print("          'Aug 21, 2037' ")
print("          'Dec 23, 1987' ")
print()
print(border)
print()

#Will keep asking for the starting date if not the proper format
while date1Loop == 0:
  print("          ► Date 1:")
  print()
  Date1 = str(input("Starting Date: "))

  if Date1[3] != " ":
    print()
    print("         ! Invalid !")
    print("   ! Improper formating !")
    print()
    print()
    
  elif Date1[6] != ",":
    print()
    print("         ! Invalid !")
    print("   ! Improper formating !")
    print()
    print()

  elif Date1[7] != " ":
    print()
    print("         ! Invalid !")
    print("   ! Improper formating !")
    print()
    print()
        
  else:
    date1Loop = 1
    print() 
    print()
    print()
    print()

#Will keep asking for the ending date if not the proper format
while date2Loop == 0:
  print("          ► Date 2:")
  print()
  Date2 = str(input("Final Date: "))
  
  if Date2[3] != " ":
    print()
    print("         ! Invalid !")
    print("   ! Improper formating !")
    print()
    print()

  elif Date2[6] != ",":
    print()
    print("         ! Invalid !")
    print("   ! Improper formating !")
    print()
    print()

  elif Date2[7] != " ":
    print()
    print("         ! Invalid !")
    print("   ! Improper formating !")
    print()
    print()

  else:
    date2Loop = 1
    print()
    print()

#Gets starting day based on input between 0-31
Day1 = getDayFromDate(Date1)

#Gets the starting day indicator based on input
Ending1 = getWordEndingFromDate(Date1)

#Gets the starting month based on input between Jan-Dec
Month1 = getMonthFromDate(Date1)

#Gets the starting year based on input between any year
Year1 = getYearFromDate(Date1)

#Gets the full name of the starting month based on input of the short form
FullMonth1 = getMonthNameFromDate(Month1)

#Gets the chronological order of starting month in the year starting from January
dayIndex = getMonthIndexFromDate(Month1)


#Gets ending day based on input between 0-31
Day2 = getSecondDayFromDate(Date2)

#Gets the ending day indicator based on input
Ending2 = getSecondWordEndingFromDate(Date2)

#Gets the ending month based on input between Jan-Dec
Month2 = getSecondMonthFromDate(Date2)

#Gets the ending year based on input between any year
Year2 = getSecondYearFromDate(Date2)

#Gets the full name of the ending month based on input of the short form
FullMonth2 = getSecondMonthNameFromDate(Month2)

#Gets the chronological order of ending month in the year starting from January
dayIndex2 = getSecondMonthIndexFromDate(Month2)


YearDifference = Year2 - Year1
YearRange = Year1
DaysLeftBetweenMonth = 0
LeapYears = 0
LeapYearsException = 0
MonthBeforeDays1 = 0
MonthBeforeDays2 = 0
countUpMonth1 = 0
countUpMonth2 = 0

#Maximum days in each month chronologically
DayLengths = [31, 28, 31, 30, 31, 30, 30, 31, 30, 31, 30, 31]

#Gets the number of days into the year based on month and day, starting from 1 (January 1st)
totalSumDays1 = getDaysIntoYear(MonthBeforeDays1, dayIndex, countUpMonth1, DayLengths, Day1)
totalSumDays2 = getSecondDaysIntoYear(MonthBeforeDays2, dayIndex2, countUpMonth2, DayLengths, Day2)

#Gets the difference of years and converts them into days
DaysYears = getYearsBetween(Year1, Year2, Month1, Month2, Day1, Day2)

#Gets the years lapsed and checks for any that pass, excluding the turn of centuries
LeapYears = getLeapYearsWith100Rule(Year1, Year2, YearRange, LeapYears)

#Gets the difference of days in the span of a year based on which date is further in the year
totalDifferenceDays = getTotalDifferenceDays(YearDifference, totalSumDays1, totalSumDays2)

#Gets the total sum of days between both dates
DaysBetween = totalDifferenceDays + DaysYears + LeapYears

#Determines the final answer based on which year comes first chronologically (date 1 can be later than date 2)
FinalAnswer = getFinalAnswer(DaysBetween)

print(border)
print()
print("          ► Total Days between  '" + FullMonth1 + " " + str(Day1) + Ending1 + ", " + str(Year1) + "'  and  '" + FullMonth2 + " " + str(Day2) + Ending2 + ", " + str(Year2) + "' ")
print()
print("          = " + str(FinalAnswer) + " days")
print()
print(border)
##print()
##print()
##print()
##print("Day1 = " + str(Day1) )
##print("Month Before = " + str(MonthBeforeDays1) )
##print("Sum in year = " + str(totalSumDays1))
##print("Month1 = " + str(Month1) )
##print("Month Indexe = " + str(dayIndex) )
##print("Year1 = " + str(Year1) )
##print()
##print("Day2 = " + str(Day2) )
##print("Month Before = " + str(MonthBeforeDays2) )
##print("Sum in year = " + str(totalSumDays2))
##print("Month2 = " + str(Month2) )
##print("Month Indexee = " + str(dayIndex2) )
##print("Year2 = " + str(Year2) )
##print()
##print("Leap Year = " + str(LeapYears) )
##print()
##print()
