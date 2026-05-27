crop = input("Enter crop name: ")
district = input("Enter district: ")
issue = input("What is your issue? ")

print("\n====== GramSathi AI ======")

print("Crop:", crop)
print("District:", district)
print("Issue:", issue)

crop = crop.lower()
issue = issue.lower()

if crop == "wheat":
    print("Season: Rabi")
    print("Water requirement: Medium")

elif crop == "rice":
    print("Season: Kharif")
    print("Water requirement: High")

else:
    print("Crop data not available yet")

if "water" in issue:
    print("Suggestion: Check irrigation schedule")

elif "disease" in issue:
    print("Suggestion: Crop disease analysis feature coming soon")

else:
    print("General support feature coming soon")

print("Weather integration: Coming soon")
print("Government schemes: Coming soon")
