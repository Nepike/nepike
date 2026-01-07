from datetime import date

def base_template(request):
    today = date.today()

    # # Новый год
    # if today.month == 12 and today.day >= 20 or today.month == 1 and today.day <= 10:
    #     return {'base_template': 'base_new_year.html'}
	#
    # # Хэллоуин
    # if today.month == 10 and today.day >= 25:
    #     return {'base_template': 'base_halloween.html'}
	#
    # # День рождения сайта
    # if today.month == 5 and today.day == 1:
    #     return {'base_template': 'base_birthday.html'}

    return {'base_template': 'core/base.html'}