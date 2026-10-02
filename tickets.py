def show_tickets(tickets):
    for ticket in tickets:
        print(f"Заявка #{ticket['id']}")
        print(f"Проблема: {ticket['title']}")
        print(f"Статус: {ticket['status']}")
        print(f"Приоритет: {ticket['priority']}")
        print(f"Исполнитель: {ticket['assignee']}")
        print()

def choice_priorities():
    print("Выберите приоритет:")
    print("1 — Низкий")
    print("2 — Средний")
    print("3 — Высокий")
    print("4 — Критический")

    priorities = {
        "1": "Низкий",
        "2": "Средний",
        "3": "Высокий",
        "4": "Критический"
    }
    
    while True:
        priority_choice = input("Введите номер: ")
    
        if priority_choice in priorities:
            priority = priorities[priority_choice]
            return priority
        else:
            print("Неверный выбор")

def create_ticket(tickets):
    title = input("Введите описание проблемы: ")
    assignee = input("Введите исполнителя: ")
    priority = choice_priorities()
    status = "Новая"

    new_id = len(tickets) + 1
    while True:
        id_exists = False
    
        for ticket in tickets:
            if ticket["id"] == new_id:
                id_exists = True
    
        if id_exists:
            new_id += 1
        else:
            break
        
    ticket = {
        "id": new_id,
        "title": title,
        "status": status,
        "priority": priority,
        "assignee": assignee
    }
    tickets.append(ticket)
    return ticket

def get_my_tickets(tickets, current_user):
    my_tickets = []
    for ticket in tickets:
        if (
        ticket["assignee"] == current_user 
        and ticket['status'] != "Закрыта"
        and (
            ticket['priority'] == "Высокий"
            or ticket['priority'] == "Критический"
            )
        ):

            my_tickets.append(ticket)
    return my_tickets

def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            return ticket

def choose_status():
    statuses = {
            "1": "Новая",
            "2": "В работе",
            "3": "Закрыта"
        }
    print("1 — Новая")  
    print("2 — В работе")
    print("3 — Закрыта")

    while True:
        status_choice = input("Выберите новый статус:")
    
        if status_choice in statuses:
            status = statuses[status_choice]
            return status
        else:
            print("Неверный выбор")

def change_ticket_status(tickets, ticket_id):
    ticket = find_ticket(tickets, ticket_id)
    if ticket is None:
        print("Заявка не найдена")
        return
    new_status = choose_status()
    ticket['status'] = new_status