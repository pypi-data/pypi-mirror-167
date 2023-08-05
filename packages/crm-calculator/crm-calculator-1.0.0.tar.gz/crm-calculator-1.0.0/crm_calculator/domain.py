from dataclasses import dataclass


@dataclass
class CRM:
    total_of_registrations: int
    total_of_essential: int


def get_percentage_of_essential(crm: CRM) -> int:
    return (
        crm.total_of_essential / crm.total_of_registrations * 100
    )


def get_percentage_of_non_essential(crm: CRM) -> int:
    total_of_non_essential = (
        crm.total_of_registrations - crm.total_of_essential
    )
    return (
        total_of_non_essential / crm.total_of_registrations * 100
    )


def get_total_of_essential_to_percentage(crm: CRM, percentage: float) -> int:
    c = 0
    while True:
        if (
            crm.total_of_essential
            / crm.total_of_registrations >= percentage / 100
        ):
            return c
        c += 1
        crm = CRM(
            crm.total_of_registrations + 1,
            crm.total_of_essential + 1
        )
