course_a = {
	'course': 'ECE-1574',
	'title': 'Engr Problem Solving with C++',
	'credits': 3,
	'slots': [
		{
			'crn': 82917,
			'days': 'M W',
			'start': 1115,
			'end': 1205,
			'location': 'HAN 100',
			'ad_days': 'T',
			'ad_start': 1700,
			'ad_end': 1850,
			'ad_location': 'SURGE 109'
		},
		{
			'crn': 82918,
			'days': 'M W',
			'start': 1115,
			'end': 1205,
			'location': 'HAN 100',
			'ad_days': 'T',
			'ad_start': 1700,
			'ad_end': 1850,
			'ad_location': 'WLH 350'
		}
	]
}

course_b = {
	'course': 'MATH-2114',
	'title': 'Introduction to Linear Algebra',
	'credits': 3,
	'slots': [
		{
			'crn': 85771,
			'days': 'M W F',
			'start': 1010,
			'end': 1100,
			'location': 'HOLD 110',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		},
		{
			'crn': 85772,
			'days': 'T R',
			'start': 1530,
			'end': 1645,
			'location': 'RAND 221',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		},
		{
			'crn': 85773,
			'days': 'M W F',
			'start': 800,
			'end': 850,
			'location': 'MCB 113',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		},
		{
			'crn': 85785,
			'days': 'M W F',
			'start': 1115,
			'end': 1205,
			'location': 'HOLD 110',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		}
	]
}

course_c = {
	'course': 'ENGL-1106',
	'title': 'First-Year Writing',
	'credits': 3,
	'slots': [
		{
			'crn': 83990,
			'days': 'M W F',
			'start': 905,
			'end': 955,
			'location': 'DURHM 261',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		},
		{
			'crn': 83991,
			'days': 'T R',
			'start': 1530,
			'end': 1645,
			'location': 'HOLD 110',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		}
	]
}

course_d = {
	'course': 'PHYS-2306',
	'title': 'Foundations of Physics',
	'credits': 4,
	'slots': [
		{
			'crn': 87374,
			'days': 'M W',
			'start': 1600,
			'end': 1715,
			'location': 'HAHN N 100',
			'ad_days': 'M',
			'ad_start': 800,
			'ad_end': 850,
			'ad_location': 'ROB 122'
		},
		{
			'crn': 87375,
			'days': 'T R',
			'start': 930,
			'end': 1045,
			'location': 'HAHN N 130',
			'ad_days': 'W',
			'ad_start': 905,
			'ad_end': 955,
			'ad_location': 'ROB 122'
		},
		{
			'crn': 87380,
			'days': 'M W F',
			'start': 905,
			'end': 955,
			'location': 'HAHN N 130',
			'ad_days': 'F',
			'ad_start': 1325,
			'ad_end': 1410,
			'ad_location': 'ROB 122'
		}
	]
}

course_e = {
	'course': 'ENGE-1216',
	'title': 'Foundations of Engineering',
	'credits': 2,
	'slots': [
		{
			'crn': 83858,
			'days': 'M W',
			'start': 1115,
			'end': 1230,
			'location': 'RAND 316',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		},
		{
			'crn': 83859,
			'days': 'M W',
			'start': 1300,
			'end': 1415,
			'location': 'RAND 316',
			'ad_days': None,
			'ad_start': None,
			'ad_end': None,
			'ad_location': None
		}
	]
}

results_test = {
	'major': 'Computer Engineering',
	'gradyear': '2018',
	'checksheet': 'https://registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/coe/COE_cpe_18.pdf',
	'term': 'Fall 2018',
	'results': []
}

results_test['results'].append(course_a)
results_test['results'].append(course_b)
results_test['results'].append(course_c)
results_test['results'].append(course_d)
results_test['results'].append(course_e)
