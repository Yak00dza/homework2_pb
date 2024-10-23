def get_user_input(expected_type, message):
    while True:
        inp = input(message)
        try:
            inp = expected_type(inp)
            return inp
        except ValueError as e:
            print(e)
            
