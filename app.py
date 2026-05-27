crop = input("Enter crop name: ")
district = input("Enter district: ")
issue = input("What is your issue? ")

print("\n----- GramSathi AI -----")

print("Crop:", crop)
print("District:", district)
print("Issue:", issue)

if crop.lower() == "wheat":
    print("Suggested season: Rabi")
elif crop.lower() == "rice":
    print("Suggested season: Kharif")
else:
    print("Crop information coming soon")

print("Weather updates coming soon")
print("Government scheme suggestions coming soon")
