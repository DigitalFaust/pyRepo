import pygal
from dice import Dice

# Creation dice
dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()

# Modeling sequence of rolling with saving results in list
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

# Analyzing results
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of data
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
