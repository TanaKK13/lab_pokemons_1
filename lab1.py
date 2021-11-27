import json

file = open('pokemon_full.json')
pokemons = file.read()

#количество символов в строке
chr_total = len(pokemons)
print ('Количество символов в строке:', chr_total)

#количество символов без пробелов и знаков перпинания
count = 0 
marks = '!@#$%^&*()_+-!№;%:?*-=,./><{}[]" '
marks += "'"
for i in pokemons:
        if i in marks:
                count += 1
print ('Количество символов в строке без знаков препинания и пробелов:', chr_total - count)

#поиск покемона с максимальной длинной описания
pokemons_list = json.loads(pokemons)
res_max_description = 0
for pokemon in pokemons_list:
        if pokemon['description'] != "Description not available yet":
                res_max_description = max(res_max_description, len(pokemon['description']))
                if res_max_description == len(pokemon['description']):
                        name_of_pokemon = pokemon['name']
print ('Имя покемона с максимальной длиной описания:', name_of_pokemon, 'Длина описания:', res_max_description)

#умение с максимальным количеством слов
res_max_count_words = 0
for pokemon in pokemons_list:
        for ability in pokemon ['abilities']:
                count_words = len(ability.split())
                res_max_count_words = max(res_max_count_words, count_words)
                if res_max_count_words == count_words:
                        max_count_words_of_ability = ability
                        
#проверка на несколько умений с максимальным количеством слов
list_pokemons_with_max_words_of_abilities = []
for pokemon in pokemons_list:
        for ability in pokemon ['abilities']:
                count_words = len(ability.split())
                if count_words == res_max_count_words:
                        list_pokemons_with_max_words_of_abilities.append (ability)
if len(list_pokemons_with_max_words_of_abilities) == 1:
        print ('Умение, которое содержит больше всего слов:', max_count_words_of_ability)
else:
        print ('Умения, которые содержат максималное количество слов:', list_pokemons_with_max_words_of_abilities)
