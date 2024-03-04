import heapq
import sys


def parse_arguments():
    """Парсить аргументи командного рядка"""

    cables = [5.0, 2.0, 3.0, 1.0, 6.0, 7.0]
    iterations = 2

    if len(sys.argv) > 1:
        try:
            cables = [float(x) for x in sys.argv[1].split(",")]
        except Exception as _:
            print(
                "Першим аргументом мають бути цифри, розділені комою, наприклад: 5.0,2.0,3.0,1.0,6.0,7.0"
            )
        if len(sys.argv) > 2:
            try:
                iterations = int(sys.argv[2])
            except Exception as _:
                print("Другим аргументом має бути число об'єднань, наприклад: 2")

    if iterations > len(cables):
        print("[!] Кількість обʼєднань не може перевищувати кількісь кабелів")
        iterations = len(cables)

    return cables, iterations


def connector(cables: list[float], iterations=2):
    cables = cables.copy()
    heapq.heapify(cables)
    result = 0

    while len(cables) > 1:
        connected = 0

        for _ in range(iterations):
            cable = heapq.heappop(cables)
            connected += cable

        heapq.heappush(cables, connected)
        result += connected

    return result, sum(cables)


def main():
    # Масив мережевих кабелів
    cables, iterations = parse_arguments()
    costs_of_connections, total_costs = connector(cables, iterations)

    cables_data = ", ".join([str(x) for x in cables])

    print(f"Масив мережевих кабелів: {cables_data}")
    print(f"Об'єднаємо по {iterations} за раз в один кабель")
    print(
        f"Витрати на з'єднання: {costs_of_connections}, загальні витрати: {total_costs}"
    )


if __name__ == "__main__":
    main()
