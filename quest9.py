# Statistical measures without using NumPy

marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]

sales = [12500, 13800, 14200, 11900, 15100, 16000, 14750]


def mean(data):
    return sum(data) / len(data)


def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2
    else:
        return sorted_data[n // 2]


def standard_deviation(data):
    avg = mean(data)

    squared_differences = []

    for value in data:
        squared_differences.append((value - avg) ** 2)

    variance = sum(squared_differences) / len(data)

    return variance ** 0.5


def calculate_statistics(data, name):
    print("\n", name)
    print("-" * 30)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Standard Deviation:", standard_deviation(data))
    print("Minimum:", min(data))
    print("Maximum:", max(data))


calculate_statistics(marks, "Marks")
calculate_statistics(temperatures, "Temperatures")
calculate_statistics(sales, "Sales")
