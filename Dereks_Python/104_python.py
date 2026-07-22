#!/usr/bin/python3

# Determine what grade you are in based on age
# Add in comparisons between American, AU, NZ and Fiji
# Age < 4 - Too young for school

age = int(input("What's your age? "))

if age < 4:
    print(f"At {age} years old, you are too young for school")
elif age == 4:
    print(f"{age} years old:\n"
         "In USA, you are in Pre-K or Kindergarten or Grade K\n"
          "In Australia, you are too young for school\n"
          "In New Zealand, you are too young for school\n"
          "In Fiji, you are too young for school")
elif age == 5:
    print(f"At {age} years old:\n"
          "In USA, you are in Pre-K or Kindergarten or Grade K\n"
          "In Australia, you are in Kindergarten or Kindy Prep also known as Foundation (Yr 0)\n"
          "In New Zealand, you are in Kindergarten or Kindy\n"
          "In Fiji, you are in Kindergarten or Kindy")
elif age == 6:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 1 in Elementary School\n"
          "In Australia, you are in Year 1 in Primary School\n"
          "In New Zealand, you are in Year 1 in Primary School\n"
          "In Fiji, you are in Year 1 / Class 1 in Primary School")
elif age == 7:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 2 in Elementary School\n"
          "In Australia, you are in Year 2 in Primary School\n"
          "In New Zealand, you are in Year 2 in Primary School\n"
          "In Fiji, you are in Year 2 / Class 2 in Primary School")
elif age == 8:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 3 in Elementary School\n"
          "In Australia, you are in Year 3 in PrimarySchool with national exam NAPLAN Year 3 (National Assessment Program Literacy and Numeracy)\n"
          "In New Zealand, you are in Year 3 in Primary School\n"
          "In Fiji, you are in Year 3 / Class 3 in Primary School")
elif age == 9:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 4 in Elementary School\n"
          "In Australia, you are in Year 4 in Primary School\n"
          "In New Zealand, you are in Year 4 in Primary School\n"
          "In Fiji, you are in Year 4 / Class 4 - Primary School")
elif age == 10:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 5 in Elementary School\n"
          "In Australia, you are in Year 5 in Primary School  with national exam NAPLAN Year 5 (National Assessment Program Literacy and Numeracy)\n"
          "In New Zealand, you are in Year 5 in Primary School\n"
          "In Fiji, you are in Year 5 / Class 5 in Primary School")
elif age == 11:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 6 in Middle School\n"
          "In Australia, you are in Year 6 in Primary School\n"
          "In New Zealand, you are in Year 6 in Primary School\n"
          "In Fiji, you are in Year 6 / Class 6 in Primary School with national exam FY6E Fiji Year 6 Examination")
elif age == 12:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 7 in Middle School\n"
          "In Australia, you are in Year 7 in Junior High School with national exam NAPLAN Year 7 (National Assessment Program Literacy and Numeracy)\n"
          "In New Zealand, you are in Year 7 in Intermediate School\n"
          "In Fiji, you are in Year 7 / Class 7 / Form 1 in Primary School with national exam FY7FE Fiji Year 7 Final Examination")
elif age == 13:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 8 in Middle School\n"
          "In Australia, you are in Year 8 in Junior High School\n"
          "In New Zealand, you are in Year 8 in Intermediate School\n"
          "In Fiji, you are in Year 8 / Class 8 / Form 2 in Primary School with national exam FY8E Fiji Year 8 Examination")
elif age == 14:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 9 in High School\n"
          "In Australia, you are in Year 9 in Junior High School with national exam NAPLAN Year 9 (National Assessment Program Literacy and Numeracy)\n"
          "In New Zealand, you are in Year 9 in Secondary / High School\n"
          "In Fiji, you are in Year 9 / Form 3 in Secondary / High School with national exam FY9FE Fiji Year 9 Final Examination")
elif age == 15:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 10 in High School\n"
          "In Australia, you are in Year 10 in Senior High School\n"
          "In New Zealand, you are in Year 10 in Secondary / High School or College\n"
          "In Fiji, you are in Year 10 / Form 4 in Secondary / High School with national exam FY10E Fiji Year 10 Examination")
elif age == 16:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 11 in High School\n"
          "In Australia, you are in Year 11 in Senior High School\n"
          "In New Zealand, you are in Year 11 in Secondary / High School with national exam NCEA Level 1\n"
          "In Fiji, you are in Year 11 / Form 5 in Secondary / High School")
elif age == 17:
    print(f"At {age} years old:\n"
          "In USA, you are in Grade 12 in High School\n"
          "In Australia, you are in Year 12 in Senior High School with national exam State Based Senior Exams\n"
          "In New Zealand, you are in Year 12 in Secondary / High School  with national exam NCEA Level 2\n"
          "In Fiji, you are in Year 12 / Form 6 in Secondary / High School with national exam FY13CE Fiji Year 12 Certificate Examination")
elif age == 18:
    print(f"At {age} years old:\n"
          "In USA, you are probably at University, Trade School or something else\n"
          "In Australia, you are probably at University, Trade School or something else\n"
          "In New Zealand, you are in Year 13 in Secondary / High School with national exam NCEA Level 3 / UE (University Entrance)\n"
          "In Fiji, you are in Year 13 / Form 7 - Secondary / High School with national exam FY13CE Fiji Year 13 Certificate Examination")
elif 19 < age < 22:
    print(f"At {age} years old:\n"
          "In USA, you are probably at University, Trade School or something else\n"
          "In Australia, you are probably at University, Trade School or something else\n"
          "In New Zealand, you are probably at University, Trade School or something else\n"
          "In Fiji, you are probably working or unemployed")
else:
    print(f"At {age} Welcome to Work sucker or Welcome to no-money no-life. Take a pick")
