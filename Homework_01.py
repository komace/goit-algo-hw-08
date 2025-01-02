import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        # Вибираємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        # Витрачена вартість на з'єднання двох кабелів
        cost = first + second
        total_cost += cost
        # Додаємо новий кабель назад в купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cables)
print(f"Мінімальна вартість з'єднання кабелів: {min_cost}")