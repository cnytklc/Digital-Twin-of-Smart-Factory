import csv

# Robot kol yon bilgisini iceren liste olusturuldu


data = [

[0, 0, 0, 0, 0, 0, 0, 0, 0],
[-1.5, 0, 0, 0, 0, 0, 0, 0, 0],
[-1.5,0,0,1.2,0,0.81,-0.81,-0.81,0.81],
[-1.5,0.2,0,1.2,0,0.81,-0.81,-0.81,0.81],
[-1.5,0.2,0,1.23,0,0.81,-0.81,-0.81,0.81],
[-1.5,0.2,0,0,0,0.81,-0.81,-0.81,0.81],
[0,0,0,0,0,0.81,-0.81,-0.81,0.81],
[1.5,0.2,0,1.15,0,0.81,-0.81,-0.81,0.81],
[1.5,0.2,0,0.9,0,0.81,-0.81,-0.81,0.81],
[1.5,0.2,0,0.8,0,0.95,-0.95,-0.95,0.95],
[1.5,0.1,0,0.1,0,0.95,-0.95,-0.95,0.95],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# CSV dosyasini olustur
csv_filename = "robot_verileri.csv"
with open(csv_filename, mode="w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print(f"{csv_filename} dosyasi olusturuldu.")

