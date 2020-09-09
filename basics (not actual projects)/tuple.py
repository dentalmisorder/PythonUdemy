divisions = ("iron", "bronze", "silver", "gold", "platinum", "diamond", "master", "challenger")

admins = ("Spylestia", "Lesteeh", "furrypussy femboy")
genders = ("man", "woman")
genders_that_can_be_changed = ["man", "woman"]

man, woman = genders
print(f'genders_that_can_be_changed: {genders_that_can_be_changed},')
genders_that_can_be_changed.append("trap")
print(f'now we add one more: {genders_that_can_be_changed}')
print(f'genders: {genders} but we cant add anything cause its tuple but we can unpack something: {woman}, {man}')


admin0, admin1, admin2 = admins #unpacking

print(admin1)
print(admin2)