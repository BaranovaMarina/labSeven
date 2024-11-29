def analyze_baggage():
    n = 10  # Кількість пасажирів
    baggage_data = []  # Список для збереження даних про багаж

    # Введення даних про багаж
    print("Введіть дані про багаж (кількість речей і загальна вага) для кожного пасажира:")
    for i in range(n):
        try:
            items = int(input(f"Пасажир {i + 1} - кількість речей: "))
            weight = float(input(f"Пасажир {i + 1} - загальна вага (кг): "))
            baggage_data.append((items, weight))
        except ValueError:
            print("Будь ласка, введіть правильні числові дані.")
            return

    # а) Кількість пасажирів з більш ніж двома речами
    more_than_two_items = sum(1 for items, _ in baggage_data if items > 2)
    print(f"Кількість пасажирів, які мають більше двох речей: {more_than_two_items}")

    # б) Чи є хоч один пасажир, у якого одна річ важить менше 25 кг
    has_one_light_item = any(items == 1 and weight < 25 for items, weight in baggage_data)
    print("Чи є пасажир з однією річчю вагою менше 25 кг:", "Так" if has_one_light_item else "Ні")

    # в) Номер багажу, де вага однієї речі відрізняється від середньої ваги на <= 0,5 кг
    average_weights = [weight / items for items, weight in baggage_data if items > 0]  # Середня вага кожної речі
    overall_avg_weight = sum(average_weights) / len(average_weights)  # Загальна середня вага
    close_to_avg = [i + 1 for i, (items, weight) in enumerate(baggage_data)
                    if items > 0 and abs((weight / items) - overall_avg_weight) <= 0.5]

    if close_to_avg:
        print(f"Номери багажу, які відповідають умові (різниця <= 0.5 кг): {', '.join(map(str, close_to_avg))}")
    else:
        print("Немає багажу, який відповідає умові (різниця <= 0.5 кг).")


# Виклик функції
analyze_baggage()
