
def get_bmi(h,w):
    return w / (h*h)
def get_cond(bmi):
    if bmi >= 18.5 and bmi < 25:
        return 'normal weight'
    elif bmi <18.5:
        return 'below normal weight'
    elif bmi >=25 and bmi < 30:
        return 'overweight'
    elif bmi >= 30 and bmi < 35:
        return 'class I obesity'
    
weight = input('weight(kg): ')
height = input('height(m): ')

get_bmi(weight,height)