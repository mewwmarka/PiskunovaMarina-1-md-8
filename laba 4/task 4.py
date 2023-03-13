def is_lucky_ticket(ticket_number: str) -> bool:
    if not len(ticket_number) % 2 == 0:
        raise ValueError('Количество цифр нечетно')

    formatted_numbers = [int(number) for number in ticket_number]
    half = len(formatted_numbers) // 2
    return sum(formatted_numbers[:half]) == sum(formatted_numbers[half:])

print(is_lucky_ticket("385916"))