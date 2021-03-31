import requests

def smartest_hero():
    for hero_name in hero_list:
        url = 'https://superheroapi.com/api/'
        token = 2619421814940190
        hero_url = url + str(token) + '/search/' + hero_name
        response = requests.get(hero_url)
        hero_int = response.json()['results'][0]['powerstats']['intelligence']
        smart_heroes.update({hero_name: hero_int})
    return smart_heroes

if __name__ == '__main__':
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    smart_heroes = dict()
    smartest_hero()
    smartest = ''
    max_int = 0
    for hero, intelligence in smart_heroes.items():
        if max_int > int(intelligence):
            continue
        else:
            max_int = int(intelligence)
            smartest = hero
    print(f'The smartest superhero is {smartest}. Intelligence = {max_int}')