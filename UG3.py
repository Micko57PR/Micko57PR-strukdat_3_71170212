kalimat_input = input("Masukkan kalimat: ")

a_list = kalimat_input.split()

output = {}

for kalimat_input in a_list:
    if kalimat_input in output:
        output[kalimat_input] += 1
    else:
        output[kalimat_input] = 1


print("Output:")

for kalimat_input, total in output.items():
    print(f"{kalimat_input} = {total}")

print(f"Total kata = {len(a_list)}")
print(f"Kata unik = {len(output)}")