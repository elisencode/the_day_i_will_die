#!/usr/bin/env python
# coding: utf-8

# Inspired by: <https://kk.org/ct2/my-life-countdown-1/>
# <https://gist.github.com/hugs/140262>
# Life expectancy date: 

print("Happy Coding!")


from datetime import date, timedelta

# birth_year = 1976
# birth_date = date(1976,3,2)
# life_expectancy = 76.09

user_prompt_birth_year = "Enter your birth year, please: "
birth_year = int(input(user_prompt_birth_year))

user_prompt_birth_month = "Enter your birth month, please: "
birth_month = int(input(user_prompt_birth_month))

user_prompt_birth_day = "Enter your birth day, please: "
birth_day = int(input(user_prompt_birth_day))

birth_date = date(birth_year, birth_month, birth_day)
print("Birth date:", birth_date)

user_prompt_life_expectancy = "Enter your life expectancy, please: "
life_expectancy = float(input(user_prompt_life_expectancy))

life_years = int(round(life_expectancy))
print("Life years:", life_years)

death_year = birth_year + life_years
print("Death year:", death_year)

birth_date_day_of_year = birth_date.timetuple()[7]
print("Birth date day of year:", birth_date_day_of_year)

percent_of_last_year = life_expectancy % 1

days = birth_date_day_of_year + percent_of_last_year * 365
days_to_live_in_last_year = timedelta(days)

# Start from dec 31 to avoid off-by-one error
the_day_i_will_die = date(death_year-1, 12, 31) + days_to_live_in_last_year
print("The day I will die:", the_day_i_will_die)

the_day_i_will_die.ctime()

days_lived = (date.today() - birth_date).days
print("Days lived:", days_lived)

days_until_i_die = (the_day_i_will_die - date.today()).days
print("Days until I die:", days_until_i_die)

total_days_i_will_live = (the_day_i_will_die - birth_date).days
print("Total days I will live:", total_days_i_will_live)

mid_life_crisis = birth_date + timedelta(days = total_days_i_will_live / 2)

mid_life_crisis.ctime()
print("Mid life crisis:", mid_life_crisis.ctime())

