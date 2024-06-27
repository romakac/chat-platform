import random
import json

# Типы данных
class Message:
  def __init__(self, text, date):
    self.text = text
    self.date = date

class Chat:
  def __init__(self, messages, chat_id, user_id, operator_id):
    self.messages = messages
    self.chat_id = chat_id
    self.user_id = user_id
    self.operator_id = operator_id
    self.csat = None

class User:
  def __init__(self, user_id, name, city, birth_date):
    self.user_id = user_id
    self.name = name
    self.city = city
    self.birth_date = birth_date

class Operator:
  def __init__(self, operator_id, name, city, birth_date, job_title, work_experience):
    self.operator_id = operator_id
    self.name = name
    self.city = city
    self.birth_date = birth_date
    self.job_title = job_title
    self.work_experience = work_experience

class ChatPlatform:
  chats = []

  def __init__(self, users, operators):
    self.users = users
    self.operators = operators

  def start_chat(self, user_id):
    # Выбираем оператора
    operator = self.operators[random.randint(0, len(self.operators) - 1)]
    
    # Создаем пустой чат и добавляем его в платформу
    # Идентификатор чата -- его порядковый номер
    chat_id = len(self.chats)
    chat = Chat([], chat_id, user_id, operator.operator_id)
    self.chats.append(chat)
    
    # Возвращаем чат
    return chat


# Тестовые наборы данных
cities = [
  'Москва',
  'Санкт-Петербург',
  'Светлоград',
  'Курган'
]

user_names = [
  'Иванов Иван Иванович',
  'Петров Петр Петрович',
  'Иванова Мария Петровна',
  'Широков Роман Иванович'
]

operator_names = [
  'Агентов Агент Агентович',
  'Операторов Оператор Операторович',
  'Поддержкина Поддержка Поддержковна'
]

birth_dates = [
  '01.01.1970',
  '05.06.1995',
  '10.09.2000',
  '20.02.2002'
]

message_dates = [
  '25.06.2024',
  '26.06.2024',
  '27.06.2024'
]

job_titles = [
  'Старший оператор',
  'Оператор',
  'Младший оператор'
]

operator_messages = [
  'Здравствуйте, чем могу помочь?',
  'Подождите минутку',
  'Ваша проблема решена, приносим извинения за неудобства'
]

user_messages = [
  'Здравствуйте, у меня проблема',
  'Хорошо, жду',
  'Спасибо'
]


# Генерация данных
# Генерирует пользователя со случайными данными
def gen_random_user():
  user_id = random.randint(0, 1000)
  name = user_names[random.randint(0, len(user_names) - 1)]
  city = cities[random.randint(0, len(cities) - 1)]
  birth_date = birth_dates[random.randint(0, len(birth_dates) - 1)]
  
  return User(user_id, name, city, birth_date)


# Генерирует оператора со случайными данными
def gen_random_operator():
  operator_id = random.randint(0, 1000)
  name = operator_names[random.randint(0, len(operator_names) - 1)]
  city = cities[random.randint(0, len(cities) - 1)]
  birth_date = birth_dates[random.randint(0, len(birth_dates) - 1)]
  job_title = job_titles[random.randint(0, len(job_titles) - 1)]
  work_experience = random.randint(0, 5);
  
  return Operator(operator_id, name, city, birth_date, job_title, work_experience)


# Заполняет чат случайными сообщениями и случайным образом проставляет csat
def fill_chat(chat):
  for i in range(0, 6):
    date = message_dates[random.randint(0, len(message_dates) - 1)]
    text = ''
    
    if i % 2 == 0:
      text = user_messages[random.randint(0, len(user_messages) - 1)]
    else:
      text = operator_messages[random.randint(0, len(operator_messages)) - 1]
    
    message = Message(text, date)
    chat.messages.append(message)
    
  # С вероятностью 50% делаем чат закрытым и ставим случайный csat
  coinflip = random.randint(0, 1)
  if coinflip == 1:
    csat = random.randint(1, 5)
    chat.csat = csat


# Генерирует платформу чатов
def gen_chat_platform(chats_count):
  users = []
  operators = []
  
  for i in range(0, 100):
    users.append(gen_random_user())
  
  for i in range(0, 10):
    operators.append(gen_random_operator())
  
  chat_platform = ChatPlatform(users, operators)
  
  for i in range(0, chats_count):
    user = users[random.randint(0, len(users) - 1)]
    chat = chat_platform.start_chat(user.user_id)
    fill_chat(chat)
    
  return chat_platform


# Выгрузки
# Выгрузка всех пользователей платформы
def print_all_users(chat_platform):
  users_json = []
  
  for user in chat_platform.users:
    users_json.append({
      "id": user.user_id,
      "name": user.name,
      "city": user.city,
      "birth_date": user.birth_date
    })

  # Используем параметр ensure_ascii = False чтобы русские символы выводились корректно
  # https://stackoverflow.com/questions/18337407/saving-utf-8-texts-with-json-dumps-as-utf-8-not-as-a-u-escape-sequence
  print(json.dumps(users_json, ensure_ascii = False))


# Выгрузка всех операторов платформы
def print_all_operators(chat_platform):
  operators_json = []
  
  for operator in chat_platform.operators:
    operators_json.append({
      "id": operator.operator_id,
      "name": operator.name,
      "city": operator.city,
      "birth_date": operator.birth_date,
      "job_title": operator.job_title,
      "work_experience": operator.work_experience
    })

  # Используем параметр ensure_ascii = False чтобы русские символы выводились корректно
  # https://stackoverflow.com/questions/18337407/saving-utf-8-texts-with-json-dumps-as-utf-8-not-as-a-u-escape-sequence
  print(json.dumps(operators_json, ensure_ascii = False))


# Количество чатов для заданного оператора
def print_count_chats_for_operator(chat_platform, operator_id):
  count = 0
  
  for chat in chat_platform.chats:
    if chat.operator_id == operator_id:
      count += 1
  
  print(count)


# Количество чатов для пользователя
def print_count_chats_for_user(chat_platform, user_id):
  count = 0
  
  for chat in chat_platform.chats:
    if chat.user_id == user_id:
      count += 1
  
  print(count)


def print_chat(chat_platform, chat_id):
  chat = chat_platform.chats[chat_id]
    
  messages_json = []

  for message in chat.messages:
    messages_json.append({
      "text": message.text,
      "date": message.date
    })
    
  # Используем параметр ensure_ascii = False чтобы русские символы выводились корректно
  # https://stackoverflow.com/questions/18337407/saving-utf-8-texts-with-json-dumps-as-utf-8-not-as-a-u-escape-sequence
  print(json.dumps(messages_json, ensure_ascii = False))


users = gen_random_user()
operators = gen_random_operator()
chat_platform = gen_chat_platform(100) 

print_all_users(chat_platform)
print_all_operators(chat_platform)
print_chat(chat_platform, random.randint(0, len(chat_platform.chats)) - 1)
