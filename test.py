with open("similarity.pkl", "rb") as f:
    data = f.read(500)  # Read the first 500 bytes
    print(data[:100])  # Print the first 100 bytes for inspection
