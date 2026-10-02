from tickets import (
    show_tickets,
    create_ticket, 
    get_my_tickets, 
    change_ticket_status
)

from utils import (
    get_int_input
)
tickets = [
{
    "id": 1,
    "title": "ATM не принимает купюры",
    "status": "В работе",
    "priority": "Высокий",
    "assignee": "Алексей"
},
{
    "id": 2,
    "title": "ATM не на связи",
    "status": "В работе", 
    "priority": "Средний",
    "assignee": "Антон" 
},
{
    "id": 3,
    "title": "Проблемы с чековым принтером",
    "status": "Новая",
    "priority": "Критический",
    "assignee": "Алексей"
}
]

def main_menu(tickets, current_user):
    while True:
        print("=== Service Desk ===")
        print("1. Показать все заявки")
        print("2. Создать заявку")
        print("3. Изменить статус заявки")
        print("4. Мои заявки")
        print("0. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            show_tickets(tickets)
        elif choice == "2":
            new_ticket = create_ticket(tickets) 
            print(f"Заявка #{new_ticket['id']} успешно создана!")   
        elif choice == "3":
            ticket_id = get_int_input("Введите ID заявки: ")
            change_ticket_status(tickets, ticket_id)
        elif choice == "4":
            my_tickets = get_my_tickets(tickets, current_user)
            show_tickets(my_tickets)
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню!")

current_user = "Алексей"
main_menu(tickets, current_user)

while True:
    in_exists = False

    for ticket in tickets:
        if ticket['id'] == new_id:
            in_exists = True

    if in_exists:
        new_id += 1
    else:
        break
