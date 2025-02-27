while True:
    start = input('Enter για συνέχεια ή "q" to quit: ')

    if start == 'q':
        break # Exit the loop if user enters 'q'

    # Read input values
    start_temperature = int(input('Start temperature = '))
    end_temperature = int(input('End temperature = '))
    step = int(input('Increment step for temperature = '))

    # Loop through the temperature range and convert to Fahrenheit
    for c in range(start_temperature,end_temperature+1,step):
        f = c*9/5 + 32
        print(c, f)
        
print('End of program')