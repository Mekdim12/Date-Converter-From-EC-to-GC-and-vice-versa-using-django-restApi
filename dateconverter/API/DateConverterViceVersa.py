
class DateConverter:
    def toGregorian(self, ethiopian_day, ethiopian_month, ethiopian_year):
        gregorian_calander = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ethiopian_calander = [0, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 5]

        # year differences in gregorian months like there is 8 years in Gregorians January and 7 years  gregorian September
        y_diff = [0, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
        # year differences in Ethiopian months like there is 8 years in Ethiopian's Tir(January) and 7 years  gregorian Mwskerem (September)
        e_diff = [0, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

        # number of difference between ethiopian calendar and gregorian calendar in each month
        diff = [0, 10, 10, 9, 9, 8, 7, 9, 8, 8, 7, 7, 6, 10]

        # representation of months in numbers in Gregorians Calendar
        ec = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # representation of months in numbers in Ethiopian Calendar interms of the positioning of Ethiopian Calendar
        gc = [0, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        gy = int(ethiopian_year) + int(y_diff[
                                           ethiopian_month])  # gets gregorian year for the specified ethiopian year  using already known year difference for the given month
        gm = gc[
            ethiopian_month]  # //gets month value in GC by looking through it's correspondant  in the EC , like January for Tir

        if ethiopian_year % 4 == 0 and ethiopian_month == 6:
            # if leap year and february then  make the days of february 29 and difference in days to 8
            gregorian_calander[2] = 29
            diff[6] = 8

        gd = int(ethiopian_day) + int(
            diff[ethiopian_month])  # GC days are the EC day in addition to the difference of the current EC month

        if ethiopian_month == 13:
            # if the given month is the unique Puagme
            if ethiopian_year % 4 == 0:
                # if leap year
                gd -= 6
            else:
                gd -= 5
        if gd > gregorian_calander[gm]:
            # if the no of days exceeded the limit of the month like 34 for september or 31 for february
            gd = gd - gregorian_calander[gm]  # days will be days minus the amount of days in the current
            gm = gm + 1  # month will be the next month
            if gm == 13:
                # if the month becomes 13 it means it engaged with new year
                gy += 1  # //so  set the GC year to the next one
                gm = 1  # // also make the GC month to the first Month of the year which is January

        itemss = [gd, gm, gy]
        return itemss

    def toEthiopianDateTime(self, euro_date, euro_month, euro_year):
        gergorian_calander = [30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31]
        ethiopian_calander = [0, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 5]

        # year differences in gregorian months like there is 8 years in Gregorians January and 7 years  gregorian September
        y_diff = [0, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 8]
        # year differences in Ethiopian months like there is 8 years in Ethiopian's Tir(January) and 7 years  gregorian Mwskerem (September)
        e_diff = [0, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8]

        # number of difference between ethiopian calendar and gregorian calendar in each month
        diff = [0, 8, 7, 9, 8, 8, 7, 7, 6, 10, 10, 9, 9]

        # representation of months in numbers in Gregorians Calendar
        gc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # representation of months in numbers in Ethiopian Calendar interms of the positioning of Gregorian Calendar
        ec = [0, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]

        et_y = euro_year - y_diff[
            euro_month]  # ethiopian year , given year minus the the current  month's differnce in years

        et_m = ec[
            euro_month]  # the ethiopian year which can be corespondant to gregorian month like meskerem for January or 1th  to 9th

        if euro_year % 4 == 3 and euro_month == 9:
            # if the year has 366 days and given month is in September GC
            diff[euro_month] = diff[euro_month] + 1  # then the current month will have one more day

        et_day = euro_date - diff[
            euro_month]  # days in EC will be given days minus the number of days in the given month
        if et_day <= 0:
            # if EC day becom -ve , this means the month is changed or decremented
            et_m = et_m - 1  # so make the month decrement by 1 like March to  February
            if et_m == 0:
                # the EC month becomes 0 this means we have decrement the EC year by
                et_m = 13
                if euro_year % 4 == 3:
                    # if the year has 366 days
                    ethiopian_calander[et_m] = 6  # then Puagme will have 6 days in it

                et_day = ethiopian_calander[
                             et_m] + et_day  # the new dayb will be the subtraction of the former negative number et_day like (september 3 - 5 days will be pagme 5 , in 366 days format

                if et_day <= 0:
                    # if still has negative value do the above again , mainly occurs for subtracting higher number from september which will result a day in August , by passing all over puagme
                    et_m = et_m - 1
                    et_day = ethiopian_calander[et_m] + et_day

                et_y = euro_year - e_diff[13]  # and the year we calculated from above will be decremented
            else:
                # means no decrement in months will occur the change will be easily from day to day
                et_day = ethiopian_calander[et_m] + et_day
        items = [et_day, et_m, et_y]
        return items
