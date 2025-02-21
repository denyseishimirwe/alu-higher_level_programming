 #!/usr/bin/python3
def print_comb():
    for i in range(10):
        for j in range(i + 1, 10):
            # Print combinations with a comma and space, but avoid a trailing comma at the last pair
            if i == 8 and j == 9:
                print(f"{i}{j}")
            else:
                print(f"{i}{j}", end=", ")

print_comb()
