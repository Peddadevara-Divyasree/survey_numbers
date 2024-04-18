# Simulate data structures for illustration
districts = ["Adilabad", "Hyderabad", "Karimnagar"]
mandals = {"Adilabad": ["Adilabad", "Boath"], "Hyderabad": ["Secunderabad", "Rajendranagar"]}
villages = {
    "Adilabad": {"Adilabad": [100, 101, 102]},
    "Hyderabad": {"Secunderabad": [200, 201], "Rajendranagar": [300, 301]},
}

def get_survey_numbers(district, mandal, village):
  """
  Simulates fetching survey numbers based on provided information.

  Args:
      district: Name of the district.
      mandal: Name of the mandal within the district.
      village: Name of the village within the mandal.

  Returns:
      List of survey numbers for the given location, or None if not found.
  """
  if district not in districts:
    return None
  if mandal not in mandals[district]:
    return None
  if village not in villages[district][mandal]:
    return None
  return villages[district][mandal][village]

# Example usage
user_district = "Hyderabad"
user_mandal = "Rajendranagar"
user_village = "Rajendranagar"

survey_numbers = get_survey_numbers(user_district, user_mandal, user_village)

if survey_numbers:
  print(f"Survey numbers for {user_village} in {user_mandal}, {user_district}:")
  for number in survey_numbers:
    print(number)
else:
  print(f"Survey numbers not found for {user_village} in {user_mandal}, {user_district}.")
