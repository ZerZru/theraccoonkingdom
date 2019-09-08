import requests

def hack(vid):
	r = requests.get('https://sparta-game-bot.herokuapp.com/api/heroes/{}'.format(vid))
	data = r.json()

	#general
	name = data['data']['customName'];
	level = data['data']['stats']['level'];
	clan = data['data']['clan']['icon'];
	health = data['data']['values']['maxHealth'];
	uID = data['data']['animal']['userId'];
	try:
		uname = data['data']['username'];
	except:
		uname = '👤Безликий'
	unamet = data['data']['firstName'];
	unametl = data['data']['lastName']
	chaos = data['data']['chaos']

	#animal
	aname = data['data']['animal']['name']
	atype = data['data']['animal']['icon']
	ahlth = data['data']['animal']['maxHealth']
	admg_min = data['data']['animal']['minDamage']
	admg_max = data['data']['animal']['maxDamage']
	aexp = data['data']['animal']['experience']
	aexp_max = data['data']['animal']['experienceMax']
	alvl = data['data']['animal']['level']

	#skills
	strength_u = data['data']['skills']['strength']
	agility_u = data['data']['skills']['agility']
	intuition_u = data['data']['skills']['intuition']
	endurance_u = data['data']['skills']['endurance']
	luck_u = data['data']['skills']['luck']
	capacity = 50
	capacity_u = endurance_u * 5
	capacity = capacity + capacity_u

	#modificators
	strength_m = data['data']['modificators']['strength']
	agility_m = data['data']['modificators']['agility']
	intuition_m = data['data']['modificators']['intuition']
	endurance_m = data['data']['modificators']['endurance']

	strength = strength_u + strength_m
	agility = agility_u + agility_m
	intuition = intuition_u + intuition_m
	endurance  = endurance_u + endurance_m
	luck = data['data']['skills']['luck']

	#info
	damage_min = data['data']['values']['minDamage']
	damage_max = data['data']['values']['maxDamage']
	defense = data['data']['values']['defense']
	dodge = data['data']['values']['chanceDodge']
	critical = data['data']['values']['chanceCritical']
	counter = data['data']['values']['chanceCounter']
	power = data['data']['values']['criticalPower']
	antidodge = data['data']['values']['antiDodge']
	anticritical = data['data']['values']['antiCritical']
	blessing = data['data']['values']['blessing']

	#mastery
	m_sword = data['data']['values']['masterySwords']
	m_axe = data['data']['values']['masteryAxes']
	m_spear = data['data']['values']['masterySpears']
	m_knife = data['data']['values']['masteryDaggers']
	m_hammer = data['data']['values']['masteryHammers']
	m_animal = data['data']['values']['masteryAnimals']

	#stats
	rating = data['data']['stats']['rating']
	wins = data['data']['stats']['wins']
	loses = data['data']['stats']['loses']
	draws = data['data']['stats']['draws']
	ratingstatus = data['data']['stats']['ratingStatus']
	experience = data['data']['stats']['experience']
	experience_max = data['data']['stats']['experienceMax']
	experience_stage = data['data']['stats']['experienceStageMax']
	experience_stage_n = data['data']['stats']['levelStage']
	vampirism = data['data']['values']['vampirism']
	blessing = data['data']['values']['blessing']
	fights = wins + loses + draws
	honor = int(level / 2 * 100 * ((wins - loses + 1) / (wins + loses) + (draws / (2 * fights))))  

	name = str(name)
	level = str(level)
	clan = str(clan)
	health = str(health)
	uID = str(uID)
	unamet = str(unamet)
	unametl = str(unametl)
	chaos = str(chaos)
	aname = str(aname)
	atype = str(atype)
	ahlth = str(ahlth)
	admg_min = str(admg_min)
	admg_max = str(admg_max)
	aexp = str(aexp)
	aexp_max = str(aexp_max)
	alvl = str(alvl)
	strength_u = int(strength_u)
	strength_m = int(strength_m)
	agility_u = int(agility_u)
	agility_m = int(agility_m)
	intuition_u = int(intuition_u)
	intuition_m = int(intuition_m)
	endurance_u = int(endurance_u)
	endurance_m = int(endurance_m)
	luck_u = int(luck_u)
	damage_min = str(damage_min)
	damage_max = str(damage_max)
	defense = str(defense)
	dodge = str(dodge)
	critical = str(critical)
	counter = str(counter)
	power = str(power)
	antidodge = str(antidodge)
	anticritical = str(anticritical)
	m_sword = str(m_sword)
	m_axe = str(m_axe)
	m_spear = str(m_spear)
	m_hammer = str(m_hammer)
	m_knife = str(m_knife)
	m_animal = str(m_animal)
	rating = str(rating)
	wins = str(wins)
	draws = int(draws)
	loses = int(loses)
	ratingstatus = str(ratingstatus)
	experience = str(experience)
	experience_stage = str(experience_stage)
	experience_stage_n = str(experience_stage_n)
	experience_max = str(experience_max)
	vampirism = str(vampirism)
	blessing = str(blessing)

	n = 0
	effects = {}
	while True:
		try:
			edata = data['data']['items']['amulet']['data']['effects'][n]
			ndata = {'{}'.format(edata['id']): '{}'.format(edata['value'])}
			effects.update(ndata)
			n += 1
		except:
			break

	if('minDamage' in effects):
		if(effects['minDamage']!=''):
			damage_min += int(effects['minDamage'])
	if('maxDamage' in effects):
		if(effects['maxDamage']!=''):
			damage_max += int(effects['maxDamage'])
	if('strength' in effects):
		if(effects['strength']!=''):
			strength_m += int(effects['strength'])
	if('endurance' in effects):
		if(effects['endurance']!=''):
			endurance_m += int(effects['endurance'])
	if('intuition' in effects):
		if(effects['intuition']!=''):
			intuition_m += int(effects['intuition'])
	if('agility' in effects):
		if(effects['agility']!=''):
			agility_m += int(effects['agility'])
	if('luck' in effects):
		if(effects['luck']!=''):
			luck_m += int(effects['luck'])
	if('masterySwords' in effects):
		if(effects['masterySwords']!=''):
			m_sword += int(effects['masterySwords'])
	if('masteryAxes' in effects):
		if(effects['masteryAxes']!=''):
			m_axe += int(effects['masteryAxes'])
	if('masterySpears' in effects):
		if(effects['masterySpears']!=''):
			m_spear += int(effects['masterySpears'])
	if('masteryDaggers' in effects):
		if(effects['masteryDaggers']!=''):
			m_knife += int(effects['masteryDaggers'])
	if('masteryHammers' in effects):
		if(effects['masteryHammers']!=''):
			m_hammer += int(effects['masteryHammers'])

	#inventory
	try:
		helmet = data['data']['items']['helmet']['data']['_title']['ru']
		helmet_h = data['data']['items']['helmet']['depreciation']
		helmet_hMax = data['data']['items']['helmet']['maxDepreciation']
	except:
		helmet = '[-]'
		helmet_h = '-'
		helmet_hMax = '-'

	try:
		armor = data['data']['items']['armor']['data']['_title']['ru']
		armor_h = data['data']['items']['armor']['depreciation']
		armor_hMax = data['data']['items']['armor']['maxDepreciation']
	except:
		armor = '[-]'
		armor_h = '-'
		armor_hMax = '-'

	try:
		boots = data['data']['items']['boots']['data']['_title']['ru']
		boots_h = data['data']['items']['boots']['depreciation']
		boots_hMax = data['data']['items']['boots']['maxDepreciation']
	except:
		boots = '[-]'
		boots_h = '-'
		boots_hMax = '-'

	try:
		gloves = data['data']['items']['gloves']['data']['_title']['ru']
		gloves_h = data['data']['items']['gloves']['depreciation']
		gloves_hMax = data['data']['items']['gloves']['maxDepreciation']
	except:
		gloves = '[-]'
		gloves_h = '-'
		gloves_hMax = '-'

	try:
		ring = data['data']['items']['ring']['data']['_title']['ru']
		ring_h = data['data']['items']['ring']['depreciation']
		ring_hMax = data['data']['items']['ring']['maxDepreciation']
	except:
		ring = '[-]'
		ring_h = '-'
		ring_hMax = '-'

	try:
		shield = data['data']['items']['shield']['data']['_title']['ru']
		shield_h = data['data']['items']['shield']['depreciation']
		shield_hMax = data['data']['items']['shield']['maxDepreciation']
	except:
		shield = '[-]'
		shield_h = '-'
		shield_hMax = '-'

	try:
		amulet = data['data']['items']['amulet']['data']['_title']['ru']
		amulet_h = data['data']['items']['amulet']['depreciation']
		amulet_hMax = data['data']['items']['amulet']['maxDepreciation']
	except:
		amulet = '[-]'
		amulet_h = '-'
		amulet_hMax = '-'

	try:
		belt = data['data']['items']['belt']['data']['_title']['ru']
		belt_h = data['data']['items']['belt']['depreciation']
		belt_hMax = data['data']['items']['belt']['maxDepreciation']
	except:
		belt = '[-]'
		belt_h = '-'
		belt_hMax = '-'

	try:
		cloak = data['data']['items']['cloak']['data']['_title']['ru']
		cloak_h = data['data']['items']['cloak']['depreciation']
		cloak_hMax = data['data']['items']['cloak']['maxDepreciation']
	except:
		cloak = '[-]'
		cloak_h = '-'
		cloak_hMax = '-'

	try:
		weapon = data['data']['items']['weapon']['data']['_title']['ru']
		weapon_h = data['data']['items']['weapon']['depreciation']
		weapon_hMax = data['data']['items']['weapon']['maxDepreciation']
	except:
		weapon = '[-]'
		weapon_h = '-'
		weapon_hMax = '-'

	try:
		bag = data['data']['items']['bag']['data']['_title']['ru']
		bag_h = data['data']['items']['bag']['depreciation']
		bag_hMax = data['data']['items']['bag']['maxDepreciation']
		bag_e = data['data']['items']['bag']['data']['effects'][0]['value']
	except:
		bag = '[-]'
		bag_h = '-'
		bag_hMax = '-'
		bag_e = 0

	skillsreset = data['data']['freeSkillsReset']
	capacity = capacity + bag_e

	if unametl == None:
		unametl = '';

	if ratingstatus==None:
		ratingstatus='Отсутствует'

	p1 = '''
	Премудрый Енот говорит...

	{} {} 🎖️{} ❤️ {} [@{}]
	💬 Имя в Telegram: {} {}

	👿 Хаос ‒ {}%
	🏅 Очков зала славы: {}
	'''.format(clan, name, level, health, uname,
	unamet, unametl,
	chaos,
	honor)

	p2 = '''
	💪 Сила: {} ({}+{})
	⚡️ Ловкость: {} ({}+{})
	🎯 Интуиция: {} ({}+{})
	❤️ Выносливость: {} ({}+{})
	🎲 Удача: {}
	🎒 Вместительность: Скрыто/{} (+{})
	'''.format(strength, strength_u, strength_m,
	agility, agility_u, agility_m,
	intuition, intuition_u, intuition_m,
	endurance, endurance_u, endurance_m,
	luck,
	capacity, bag_e)

	p3 = '''
	🗡️ Урон: {}-{}
	🛡️ Броня {}
	⚡️ Уворот: {}
	🎯 Критический удар: {}
	🐍 Ответный удар: {}
	💥 Мощность: {}
	💘 Точность: {}
	💗 Стойкость: {}
	💖 Благословение: {}%
	❣️ Вампиризм: {}%
	'''.format(damage_min, damage_max,
	defense,
	dodge,
	critical,
	counter,
	power,
	antidodge,
	anticritical,
	blessing,
	vampirism)

	if(experience_stage_n == 4):
		p4 = '''
		🌟 Опыт: {} / {}
		💟 Склонность: В поиске...
		'''.format(experience, experience_max)
	else:
		p4 = '''
		🌟 Опыт: {} → {} /... / {}
		💟 Склонность: В поиске...
		'''.format(experience, experience_stage, experience_max)

	p5 = '''
	🔹Владение мечами: {}
	🔹Владение топорами: {}
	🔹Владение копьями: {}
	🔹Владение ножами: {}
	🔹Владение молотами: {}
	🔹Дрессировка: {}
	'''.format(m_sword,
	m_axe,
	m_spear,
	m_knife,
	m_hammer,
	m_animal)

	p6 = '''
	Лига Спарты 
	💯 Рейтинг: {}
	🏆 Побед: {}
	🤕 Поражений: {}
	🤝 Ничьих: {}
	🔸 Статус лиги: {}
	'''.format(rating,
	wins,
	loses,
	draws,
	ratingstatus)

	p7 = '''
	🔸 Оружие: {} ({}/{})
	🔸 Щит: {} ({}/{})
	🔸 Шлем: {} ({}/{})
	🔸 Доспехи: {} ({}/{})
	🔸 Перчатки: {} ({}/{})
	🔸 Сапоги: {} ({}/{})
	🔸 Ремень: {} ({}/{})
	🔸 Плащ: {} ({}/{})
	🔸 Амулет: {} ({}/{})
	🔸 Кольцо: {} ({}/{})
	🔸 Сумка: {} ({}/{})
	Бесплатных переобучений ‒ 🎓 {}
	'''.format(weapon, weapon_h, weapon_hMax,
	shield, shield_h, shield_hMax,
	helmet, helmet_h, helmet_hMax,
	armor, armor_h, armor_hMax,
	gloves, gloves_h, gloves_hMax,
	boots, boots_h, boots_hMax,
	belt, belt_h, belt_hMax,
	cloak, cloak_h, cloak_hMax,
	amulet, amulet_h, amulet_h,
	ring, ring_h, ring_hMax,
	bag, bag_h, bag_hMax,
	skillsreset)

	p8 = '''
	Имя: {} {}
	🎖️  Уровень: {}
	🌟 Опыт: {} / {}
	🗡️ Урон: {}-{}
	❤️ Здоровье: {}
	'''.format(atype, aname,
	alvl,
	aexp, aexp_max,
	admg_min, admg_max,
	ahlth)

	p9 = '''
	Версия 1.1.5
	'''

	answer = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9

hack('75002629')