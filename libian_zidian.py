user_0={
    'username':'efemi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")
favourtie_languages = {
    'jen':'pytoon',
    'sarah':'c',
    'phll':'ruby',
}
for name,languages in favourtie_languages.items():
    print(f"{name.title()}'s favorite languages is {languages.title()}")
favourtie_languages = {
    'jen':'pytoon',
    'sarah':'c',
    'phll':'ruby',
}
for name in  favourtie_languages.keys():
    print(name.title())