import pandas as pd
import numpy as np

# DATAFRAME


sumatera = [
    ("Aceh",111.03,4.45),
    ("Sumatera Utara",111.11,5.32),
    ("Sumatera Barat",110.60,4.22),
    ("Riau",111.17,5.08),
    ("Jambi",109.80,3.77),
    ("Sumatera Selatan",109.42,3.44),
    ("Bengkulu",108.19,2.57),
    ("Lampung",108.51,1.17),
    ("Kep. Bangka Belitung",105.65,1.82),
    ("Kep. Riau",109.19,2.70)
]

luar = [
("Bali",109.62,2.51),
("NTB",108.72,2.69),
("NTT",107.48,2.30),
("Kalimantan Barat",108.06,1.94),
("Kalimantan Tengah",108.08,2.35),
("Kalsel",109.03,2.91),
("Kaltim",108.58,1.77),
("Kaltara",107.65,2.32),
("Sulut",108.36,1.57),
("Sulteng",110.96,3.88),
("Sulsel",108.72,3.03),
("Sultra",110.03,3.68),
("Gorontalo",108.23,1.99),
("Sulbar",109.26,3.04),
("Maluku",109.68,3.01),
("Maluku Utara",108.48,-0.17),
("Papua Barat",108.51,1.02),
("Papua Barat Daya",107.04,1.30),
("Papua",104.94,0.99),
("Papua Selatan",109.93,3.42),
("Papua Tengah",111.94,2.28),
("Papua Pegunungan",114.03,3.55)
]

df = pd.DataFrame(sumatera + luar, columns=["Provinsi","IHK","Inflasi_YoY"])
df["Region"] = ["Sumatera"]*10 + ["Luar"]*22


# SIMPLE RANDOM SAMPLING


print("=== SIMPLE RANDOM SAMPLING (n=10) ===")
print(df.sample(n=10, random_state=1))


# STRATIFIED SAMPLING (30% per region)


print("\n=== STRATIFIED SAMPLING (30% tiap Region) ===")
strat_sample = df.groupby("Region").apply(
    lambda x: x.sample(frac=0.3, random_state=1)
)
print(strat_sample)


# SYSTEMATIC SAMPLING (interval 3)


print("\n=== SYSTEMATIC SAMPLING (tiap baris ke-3) ===")
print(df.iloc[::3])


# CLUSTER SAMPLING (pilih 1 cluster Region)


print("\n=== CLUSTER SAMPLING (cluster = Region) ===")
cluster = np.random.choice(df["Region"].unique())
cluster_sample = df[df["Region"] == cluster]
print("Cluster terpilih:", cluster)
print(cluster_sample)
