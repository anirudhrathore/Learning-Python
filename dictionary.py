
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "Zero",
    1: "One"
}

print(monthConversions["Mar"])
print(monthConversions[0])
print(monthConversions.get("Luv", "Not a valid key"))


