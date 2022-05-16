import json
DATA_PATH = "candidates.json"


def get_data(path=DATA_PATH):
    """Получает данные кандидатов из json файла"""
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


#print(get_candidates())


def get_candidates_pk(pk):
    """Получает кандидата по id"""
    candidates = get_data()
    for candidate in candidates:
        if candidate["id"] == pk:
            return candidate
#print (get_candidates_pk(1))


def get_candidates_skills(skill_name):
    """Получает кандидата по skill"""
    candidates_skill = []  # список кандидатов по навыкам
    skill_name = skill_name.lower()
    candidates = get_data() # получаем кандидатов из функции
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            candidates_skill.append(candidate)
    return candidates_skill


 #  print(get_candidates_skills("go"))