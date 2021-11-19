from pprint import pprint

todos = [
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False
  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": True
  },
  {
    "userId": 1,
    "id": 5,
    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
    "completed": False
  },
  {
    "userId": 1,
    "id": 6,
    "title": "qui ullam ratione quibusdam voluptatem quia omnis",
    "completed": False
  },
  {
    "userId": 1,
    "id": 7,
    "title": "illo expedita consequatur quia in",
    "completed": False
  },
  {
    "userId": 1,
    "id": 8,
    "title": "quo adipisci enim quam ut ab",
    "completed": True
  },
  {
    "userId": 1,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",
    "completed": False
  }
]


completed_todos = [todo for todo in todos if todo['completed']]

for todo in todos:
    if todo['completed'] == True:
        completed_todos.append(todo)

pprint(completed_todos)
pprint(todos)

d = {
    "userId": 1,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",
    "completed": False
}

keys = d.keys()
values = d.values()
print(keys)
print(values)


l =[1,2,3]
if 1 in l:
     print("ok")

if 9 in d:
    print('ok')
else:
    print('ko')
