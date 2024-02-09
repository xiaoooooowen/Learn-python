#coding= gbk
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) 
alien_0['x_position'] = 0 
alien_0['y_position'] = 25 
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print(f"Original x_position: {alien_0['x_position']}") 
# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow': 
    x_increment = 1 
elif alien_0['speed'] == 'medium': 
    x_increment = 2 
else: 
# 这个外星人的移动速度肯定很快。
    x_increment = 3
   # 新位置为旧位置加上移动距离。
alien_0['x_position'] = alien_0['x_position'] + x_increment 
print(f"New x_position: {alien_0['x_position']}")

user_0 = { 
 'username': 'efermi', 
 'first': 'enrico', 
 'last': 'fermi', 
 } 
for key, value in user_0.items(): 
    print(f"\nKey: {key}") 
    print(f"Value: {value}\n")

favorite_languages = {
 'jen': 'python', 
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favorite_languages.items(): 
    print(f"{name.title()}'s favorite language is {language.title()}.")


