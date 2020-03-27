import unittest

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):

    # add daily bounds as blocked off times and convert all string time values to ints
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)

    # merge in numeric order
    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)

    # flatten calendar to merge overlapping meetings
    flattenedCalendar = flattenCalendar(mergedCalendar)

    # find potential blocks for new meeting
    matchingAvailability = findMatchingAvailability(flattenedCalendar, meetingDuration)
    
    print(updatedCalendar1)
    print(mergedCalendar)
    print(flattenedCalendar)
    print(matchingAvailability)
    
    # convert availability back to string military time
    matchingAvailability = convertToMilitaryTime(matchingAvailability)

    print(matchingAvailability)
    return matchingAvailability

def convertToMilitaryTime(calendar):
    militaryTime = []
    for timeBlock in calendar:
        hrs1 = timeBlock[0] // 60
        mins1 = timeBlock[0] % 60
        hrs2 = timeBlock[1] // 60
        mins2 = timeBlock[1] % 60
        militaryTime.append([
            timeToString([hrs1, mins1]),
            timeToString([hrs2, mins2])
        ])

    return militaryTime


def timeToString(time):
    mins = str(time[1]) if time[1] >= 10 else '0' + str(time[1])
    return str(time[0]) + ':' + mins

def findMatchingAvailability(calendar, meetingDuration):
    matchingAvailability = []

    for i in range(1, len(calendar)):
        endPrevMeeting = calendar[i - 1][1]
        startCurrMeeting = calendar[i][0]
        if startCurrMeeting - endPrevMeeting >= meetingDuration:
            matchingAvailability.append([
                endPrevMeeting,
                startCurrMeeting
            ])

    return matchingAvailability


def flattenCalendar(calendar):
    flattened = [calendar[0]]
    for i in range(1, len(calendar)):
        currentMeeting = calendar[i]
        currStart, currEnd = currentMeeting

        # can the latest meeting block in flattened be extended based on currentMeeting?
        prevMeeting = flattened[-1]
        prevStart, prevEnd = prevMeeting

        # no overlap at all
        if currStart > prevEnd:
            flattened.append(currentMeeting)

        # current meeting overlaps with prev meeting
        elif currStart <= prevEnd:
            # current meeting entirely captured in prev meeting block
            # or # current meeting ends later than the pev meeting block
            # update the end time of prev meeting with larger of the two end times
            flattened[-1][1] = max(prevEnd, currEnd)

    return flattened  


def mergeCalendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0

    # merge by sorted values
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1

    # while loop breaks when i or j out of bounds
    # need to add remaining elements of other list
    while i < len(calendar1): 
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2): 
        merged.append(calendar2[j])
        j += 1
    
    return merged



def updateCalendar(calendar, dailyBounds):
    
    # make a copy of calendar to manipulate it - don't want to manipulate original data
    updatedCalendar = calendar[:]

    # add unavailability for before work day starts, and after it ends
    updatedCalendar.insert(0, ['0:00', dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1], '23:59'])

    # convert each start and end time for the block into minutes:
    timeInMins = []
    for timeBlock in updatedCalendar:
        timeInMins.append([
            timeToMinutes(timeBlock[0]),
            timeToMinutes(timeBlock[1]),
        ])
    
    return timeInMins

# transform string times into numeric values -> calculate total minutes and return that
def timeToMinutes(time):
    # '12:00' -> [12, 0]
    hours, minutes = list(map(int, time.split(':')))
    return 60 * hours + minutes

    



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:00", "20:00"]
        calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
        dailyBounds2 = ["10:00", "18:30"]
        meetingDuration = 30
        expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)
    
test = TestProgram()
test.test_case_1()

'''
Practice Problem from Algo Expert
'''