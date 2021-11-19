from pprint import pprint
import json

def main_write():
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

    with open("todos.csv", "w") as f:
        header = todos[0].keys()
        str_header = ";".join(header)
        print(str_header, file=f)

        for todo in todos:
            # line = "{userId};{id};{title};{completed}".format(**todo)
            c = [str(v) for v in todo.values()]

            line = ";".join(c)
            # Ecriture vers stdout
            # print(line)

            # Ecriture vers fichier
            print(line, file=f)

            # Ecriture avec write
            # f.write(line+"\n")


def main_read():
    with open("todos.csv") as f:
        lines = f.readlines()
        header = lines[0].strip()
        header_names = header.split(';')

        data = lines[1:]

        todos = []
        for d in data:
            d = d.strip().split(';')
            todo = dict(zip(header_names, d))
            todos.append(todo)

        print(todos)

        #   for line in f:
        #       print(line.strip())


def main_writejson():
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

    with open('todos.json','w') as f:
        json.dump(todos,f)

def main():
    with open('todos.json') as f:
        todos = json.load(f)
        print(todos[0]['title'])

        
if __name__ == '__main__':
    main()
