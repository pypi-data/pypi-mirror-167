from domain import CRM, get_total_of_essential_to_percentage


def show_form() -> None:
    total_of_registrations = int(input('Atendimentos: '))
    total_of_essential = int(input('Essenciais: '))
    percentage = float(input('Porcentagem: '))
    crm = CRM(total_of_registrations, total_of_essential)
    print(
        '\nVocê precisa de mais '
        f'{get_total_of_essential_to_percentage(crm, percentage)} '
        'cadastros completos'
    )


if __name__ == '__main__':
    show_form()
