import click
from tabulate import tabulate


def get_costs_list_for_user(costs_list: list):
    """Method to format data in costs list to be displayed in a table and calculate user cost


    :param costs_list: list of costs for user
    :type costs_list: list
    :return: formatted list of costs and total cost for user
    :rtype: user_costs_list_to_print: list, total_user_cost: float
    """
    user_costs_list_to_print = []
    total_user_cost = 0
    for cost in costs_list:

        rent_start = cost["rent_start"]
        rent_end = cost["rent_end"]
        rent_time = f"{int(cost['rent_time'])} s"

        rent_cost = f"{float(cost['cost_total']):.2f} pln"
        resources = cost["resources"]
        name = resources["name"]
        rent_type = cost["type"]
        if rent_type == "events_compute":
            entity = resources["entity"]
        elif rent_type == "events_volume":
            entity = "volume"
        total_user_cost += float(cost["cost_total"])
        row_list = [entity, name, rent_start, rent_end, rent_time, rent_cost]
        user_costs_list_to_print.append(row_list)
    user_costs_list_to_print.sort(key=lambda d: f"{d[0]} {d[2]}")
    return user_costs_list_to_print, total_user_cost


def print_billing_status(user_list: list):
    """Prints billing status for all users in a pretty table

    :param user_list: list of users with costs
    :type user_list: list
    """
    for user in user_list:
        user_id = user["user_id"]
        costs_list = user["details"]
        costs_list_to_print, user_cost = get_costs_list_for_user(costs_list)
        list_headers = get_status_list_headers()
        click.echo(f"Billing status for user: {user_id}")
        click.echo(tabulate(costs_list_to_print, headers=list_headers))
        click.echo(f"Summary user cost: {float(user_cost):.2f} pln")
        click.echo()


def get_status_list_headers():
    """Generates headers for billing status command

    :return: list of headers
    :rtype: list
    """
    headers = ["entity", "name", "start", "end", "time", "cost"]
    return headers
