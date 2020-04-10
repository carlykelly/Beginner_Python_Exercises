import os
import csv

cereal_csv = os.path.join("cereal.csv")

with open(cereal_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
        # Set variable to check if we found the video
    found = False

    # Loop through looking for the video
    for record in csvreader:
        
        cereal_name = record[0]
        fiber = float(record[7])
# below is unnecessary if only printing cereal name and fiber.
        mfr = record [1]
        cereal_type = record [2]
        calories = record [3]
        protien = record [4]
        fat = record[5]
        sodium = record [6]
        carbs = record [8]
        sugars = record [9]
        potassium = record[10]
        vitamins = record[11]
        shelf = record [12]
        weight = record [13]
        cups = record [14]
        rating = record [15]
        

        if fiber >= 5:
# if only need cereal name and amount of fiber un-comment below
            #print(f"{cereal_name} has {fiber} grams of fiber")
            print(f"{cereal_name}, has an mfr of {mfr}, a type of: {cereal_type}, {calories} calories, {protien}g protien,"\
                  f"{fat}g fat, {sodium}mg sodium, {fiber}g fiber, {carbs}g of carbs, {sugars}g sugar,"\
                  f"{potassium}mg potassium, {vitamins} vitamins, shelf: {shelf}, weight: {weight}, {cups}:cups per serving"\
                  f"rating: {rating}")
            print("")
                
            # BONUS: Set variable to confirm we have found the video
            found = True


