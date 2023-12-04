import random

# Informasi pekerjaan
jobs = {
    1: {
        "Ukuran": 30,  # dalam KB
        "Eksekusi": 40000  # dalam Hz
    },
    2: {
        "Ukuran": 100,  # dalam KB
        "Eksekusi": 500000  # dalam Hz
    },
    3: {
        "Ukuran": 10000,  # dalam KB
        "Eksekusi": 40000  # dalam Hz
    },
    4: {
        "Ukuran": 50,  # dalam KB
        "Eksekusi": 200000  # dalam Hz
    },
    5: {
        "Ukuran": 500,  # dalam KB
        "Eksekusi": 1000000  # dalam Hz
    },
    6: {
        "Ukuran": 200,  # dalam KB
        "Eksekusi": 600000  # dalam Hz
    },
    7: {
        "Ukuran": 1000,  # dalam KB
        "Eksekusi": 300000  # dalam Hz
    },
    8: {
        "Ukuran": 150,  # dalam KB
        "Eksekusi": 700000  # dalam Hz
    },
    9: {
        "Ukuran": 1000,  # dalam KB
        "Eksekusi": 200000  # dalam Hz
    },
    10: {
        "Ukuran": 2000,  # dalam KB
        "Eksekusi": 900000  # dalam Hz
    }
}

# Informasi perangkat mobile
devices = {
    i: {
        "CPU": random.uniform(1.0, 2.0),  # dalam GHz
        "Battery": random.uniform(3.0, 6.0),  # dalam AH
        "TransferRate": random.uniform(10, 50)  # dalam Mbps
    }
    for i in range(1, 51)
}

# Fungsi untuk menghitung waktu eksekusi
def calculate_execution_time(job, device):
    job_size = jobs[job]["Ukuran"]
    execution_freq = jobs[job]["Eksekusi"]
    cpu_freq = devices[device]["CPU"]

    # Hitung waktu eksekusi
    execution_time = job_size / (execution_freq / cpu_freq)

    return execution_time

# Fungsi untuk menghitung waktu transfer data
def calculate_transfer_time(data_size, transfer_rate):
    # Hitung waktu transfer data
    transfer_time = data_size / transfer_rate

    return transfer_time

# Fungsi untuk menghitung total waktu
def calculate_total_time(combination):
    total_time = 0

    for job, device in combination.items():
        data_size = jobs[job]["Ukuran"]
        execution_time = calculate_execution_time(job, device)
        transfer_time = calculate_transfer_time(data_size, devices[device]["TransferRate"])
        total_time += execution_time + transfer_time

    return total_time

# Fungsi untuk melakukan pencarian tabu
def tabu_search():
    best_solution = {}
    best_time = float("inf")
    tabu_list = []
    tabu_size = 10
    max_iterations = 100

    for _ in range(max_iterations):
        neighbors = []

        for _ in range(10):
            # Generate random neighbor
            neighbor = {job: random.choice(list(devices.keys())) for job in jobs}
            neighbors.append(neighbor)

        neighbors = sorted(neighbors, key=lambda x: calculate_total_time(x))
        best_neighbor = neighbors[0]
        best_neighbor_time = calculate_total_time(best_neighbor)

        if best_neighbor_time < best_time or best_neighbor not in tabu_list:
            best_solution = best_neighbor
            best_time = best_neighbor_time

        tabu_list.append(best_neighbor)

        if len(tabu_list) > tabu_size:
            tabu_list = tabu_list[1:]

    return best_solution, best_time

# Jalankan pencarian tabu
best_solution, best_time = tabu_search()

# Tampilkan hasil
print("Kombinasi tugas dan perangkat mobile dengan waktu minimum:")
print("Solusi:", best_solution)
print("Total waktu:", best_time)