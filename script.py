import csv

def calculate_average(lst):
    avg = round(sum(lst) / len(lst), 2)
    return avg

def get_median(lst):
    sorted_list = sorted(lst)
    median = sorted_list[len(lst) // 2]
    return median

def make_med_or_avg_dict(dictionary, function):
    new_dict = {}
    for key, value in dictionary.items():
        if value:
            new_value = function(value)
            new_dict[key] = new_value
    return new_dict

def has_children(num_children):
    if num_children > 0:
        return True
    else:
        return False

def get_percentage(num_1, num_2):
    percentage = round((num_1 / (num_1 + num_2)) * 100, 3)
    return percentage

with open('insurance.csv', newline='') as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv, delimiter=',')
    
    age_lists = [list() for i in range(10)]
    male_female_list = [[], []]
    with_children = 0
    no_children = 0
    
    for row in insurance_dict:
        age_lists[int(row['age']) // 10].append(float(row['bmi']))
        
        if row['sex'] == 'male':
            male_female_list[0].append(float(row['charges']))
        else:
            male_female_list[1].append(float(row['charges']))
        
        if has_children(int(row['children'])):
            with_children += 1
        else:
            no_children += 1

age_to_bmi_dict = {}
for age in [i * 10 for i in range(10)]:
    age_to_bmi_dict["{} - {}".format(age, age + 9)] = None
for i in [i * 10 for i in range(len(age_lists))]:
    age_to_bmi_dict["{} - {}".format(i, i + 9)] = age_lists[i // 10]

gender_to_cost_dict = {}
gender_to_cost_dict['male'] = male_female_list[0]
gender_to_cost_dict['female'] = male_female_list[1]

has_children_dict = {}
has_children_dict['has children'] = with_children
has_children_dict["doesn't have children"] = no_children

average_bmi_dict = make_med_or_avg_dict(age_to_bmi_dict, calculate_average)
median_bmi_dict = make_med_or_avg_dict(age_to_bmi_dict, get_median)

average_charges_dict = make_med_or_avg_dict(gender_to_cost_dict, calculate_average)
median_charge_dict = make_med_or_avg_dict(gender_to_cost_dict, get_median)

has_children_percent = {}
has_children_percent['has children'] = "{} %".format(get_percentage(has_children_dict['has children'], has_children_dict["doesn't have children"]))
has_children_percent["doesn't have children"] = "{} %".format(get_percentage(has_children_dict["doesn't have children"], has_children_dict['has children']))

print("Average BMI for age group: {}".format(average_bmi_dict))
print("Median BMI for age_group: {}".format(median_bmi_dict))
print("\n")
print("Average cost for sex: {}".format(average_charges_dict))
print("Median cost for sex: {}".format(median_charge_dict))
print("\n")
print("Has at least one child: {}".format(has_children_percent))
