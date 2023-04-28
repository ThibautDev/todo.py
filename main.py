import os
import json

os.system('clear')

printMessage = True

# The main function
def main(): 
    print("Welcome to todo list program ")
    print("Press c for Create todo list")
    print("Press l for Load todo list")
    print("Press q for Quit the app")

    choixMenu = input("> ")


    if (choixMenu == "c"):
        create()
    elif (choixMenu == "l"):
        chose()
    elif (choixMenu == "q"):
        os.system('clear')
        exit()
    else :
        main()

# The create function
def create():
    # Ask the name of the new todo list
    print("Please, give me the name of the new todo list")
    newName = input("> ")

    #get the numbers of file
    path = './todoLists'
    num_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

    # Create a new todo list
    defaultData = {"name": "test", "tasksId": {}}
    with open('./todoLists/' + str(num_files) + '.json', 'w') as outfile:
        json.dump(defaultData, outfile)

    #Load the new todo list
    load(num_files, "Todo list successfuly created", True)

def chose():
    # TODO: Create a select todo list 

    path = './todoLists'
    num_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

    for i in range(num_files):
        print(str(i + 1) + ". " + json.load(open('todoLists/' + str(i) + '.json'))["name"])
        
    choixLoad = int(input("> ")) - 1

    load(choixLoad, "Todo list successfully loaded", True)

def load(id, message, printMessage):
    os.system('clear')

    if printMessage:
        print(message)
        print("Give the task id for check / uncheck it")
        print("Press a for add a task")
        print("Press c for clear all done tasks")
        print("Press q for back to the start menu")
        print("Press qa for quit the program")
        print("Press h for toggle not see this message again")
        print("")

    data = json.load(open('todoLists/' + str(id) + '.json'))
    
    for i in range(len(data["tasksId"])): 
        if data["tasksId"][str(i)]["status"]:
            taskStatus = " (*)"
        else:
            taskStatus = " ( )"
        
        print(str(i + 1) + ". " +  data["tasksId"][str(i)]["taskName"] + taskStatus)

    inputLoad = input("> ")

    if inputLoad.isdigit():
        inputLoad = int(inputLoad) - 1
        if inputLoad < len(data["tasksId"]) + 1 and inputLoad >= 0:
            data["tasksId"][str(inputLoad)]["status"] = not data["tasksId"][str(inputLoad)]["status"]

            with open('todoLists/' + str(id) + '.json', 'w') as outfile:
                json.dump(data, outfile)

            load(id, "Task status successfuly updated", printMessage)
        else:
            load(id, "Task id doesn't exist", printMessage)
    elif (inputLoad == "a"):
        print("Please, give me the new task name")
        newTask = str(input("> "))

        data["tasksId"][str(len(data["tasksId"]))] = {"taskName": str(newTask), "status": False}

        with open('todoLists/' + str(id) + '.json', 'w') as outfile:
            json.dump(data, outfile)

        load(id, "Task successfuly added", printMessage)
    elif (inputLoad == "c"):
        name = data["name"]
        cleanData = {"name": name, "tasksId":{}}
        j = 0

        for i in range(len(data["tasksId"])): 
            if not data["tasksId"][str(i)]["status"]:
                cleanData["tasksId"][j] = data["tasksId"][str(i)]
                j += 1

        with open('todoLists/' + str(id) + '.json', 'w') as outfile:
            json.dump(cleanData, outfile)
        load(id, "Todo list successfully cleaned", printMessage)

    elif (inputLoad == "qa"):
        os.system('clear')
        exit()
    elif (inputLoad == "q"):
        main()
    elif (inputLoad == "h"):
        load(id, "Print message succesfully toggled", not printMessage)
    else:
        load(id, "Unatribuated input", printMessage)

main()