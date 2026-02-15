did = []
to_do = []
in_progress = []
all = []

def add(text):
    task_id = len(all) + 1
    all.append({'name':text,'id':task_id, 'status':'todo' })
    print(f'Task added successfully (ID: {task_id})')
    return task_id

def update(id,text):
    if int(id) <= len(all):
        for task in all:
            if task['id'] == int(id):
                task['name'] = text
                print(f'task {id} updated')
                return
    print(f'task {id} not found!')    

def delete(id):
    id = int(id)
    if id <= len(all):
        all.pop(id-1)
        print(f'Task {id} deleted successfully')
    else:
        print(f'Task {id} not found!')

def mark_in_progress(id):
    if int(id) <= len(all) + 1:
        for Id,Index in enumerate(all):
            if int(id)-1 == Id:
                Index['status'] = 'in_progress'
                in_progress.append(Index)
                print(f'task ID {id} added in in_progress list')
    else :
        print(f'there is not {id} task')   

def mark_done(id):
    if int(id) <= len(all) + 1:
        for Id,Index in enumerate(all):
            if int(id)-1 == Id:
                did.append(Index)
                Index['status'] = 'did'
                for Id1,Index1 in enumerate(in_progress):
                    if Index1['name'] == Index['name']:
                        in_progress.pop(Id)
                all.pop(Id)        
                print(f'task ID {id} added in did list') 
    else:
        print(f'Task {id} not found!')        
    

def listing():
    print('your all tasks are:')
    for i in all:
        print(i['name'])

def list_done():
    print('your dided tasks are:')
    for i in did:
        print(i['name'])


def list_todo():
    for i in all:
        if i['status'] == 'todo':
            to_do.append(i)
    print('your doing tasks are:')
    for i in to_do:
        print(i['name'])


def main():
    """Main function that runs the task manager CLI."""
    print("Welcome to Task Manager CLI!")
    print("Available commands: add, update, delete, mark_in_progress, mark_done, list, list_done, list_todo")
    print("Type 'quit' or press Ctrl+C to exit")
    print("-" * 50)
    
    while True:
        try:
            user_input = input().strip().split()
            if user_input[0] == 'add':
                add(user_input[1])    
            elif user_input[0] == 'update':
                update(user_input[1],user_input[2])
            elif user_input[0] == 'delete':
                delete(user_input[1])
            elif user_input[0] == 'mark_in_progress':
                mark_in_progress(user_input[1])
            elif user_input[0] == 'mark_done':
                mark_done(user_input[1])
            elif user_input[0] == 'list':
                listing()
            elif user_input[0] == 'list done' or user_input[0] == 'list_done':
                list_done()
            elif user_input[0] == 'list todo' or user_input[0] == 'list_todo':
                list_todo()
            elif user_input[0] == 'quit':
                print('Have a good day!')
                break
            else : 
                raise Exception("please enter a valid command")    
        except KeyboardInterrupt:
            print('Have a good day!')
            break
        except Exception as e:
            print(f'We have the {e} error')


if __name__ == "__main__":
    main()
    