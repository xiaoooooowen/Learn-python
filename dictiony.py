#coding= gbk
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) 
alien_0['x_position'] = 0 
alien_0['y_position'] = 25 
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print(f"Original x_position: {alien_0['x_position']}") 
# �����ƶ������ˡ�
# ���ݵ�ǰ�ٶ�ȷ���������������ƶ���Զ��
if alien_0['speed'] == 'slow': 
    x_increment = 1 
elif alien_0['speed'] == 'medium': 
    x_increment = 2 
else: 
# ��������˵��ƶ��ٶȿ϶��ܿ졣
    x_increment = 3
   # ��λ��Ϊ��λ�ü����ƶ����롣
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


