def parse_input(
    message: str,
    class_: type,
    min_value: 'class_' = None,
    max_value: 'class_' = None,
    valid_values: list = None,
    allow_exit: bool = False,
    default_value: 'class_' = None,
):
    """Requests an input from the user and validates it.
    
    This function will only raise an exception if the arguments are invalid.
    If the user's input is invalid, a message will be printed and the user will be allowed to try again.

    Args:
        message (str): The message to display to the user to request the input.
        class_ (type): The expected class of the response. For example: int, float, str.
        min_value (class_, optional): The minimum input value. Must be of type class_. Defaults to None.
        max_value (class_, optional): The maximum input value. Must be of type class_. Defaults to None.
        valid_values (list, optional): List of valid values. If the value is only accepted if it is included in this list. If min and max bounds are specified, at least one value in this list must be within those bounds. Defaults to None.
        allow_exit (bool, optional): Whether the input can be empty. If set to true, the function will return None if nothing is entered. Defaults to False.
        default_value (class_, optional): The value to return if no input is provided. Only works if allow_exit is True. Defaults to None.

    Raises:
        ValueError: If min_value is greater than max_value.
        ValueError: If all values in valid_values are out of min/max bounds.
        ValueError: If the default_value parameter cannot be cast to the type specified by class_.

    Returns:
        class_: The value entered by the user, or None if nothing entered and allow_exit is True.
    """
    # Validation of parameters
    if min_value is not None and max_value is not None and max_value < min_value:
        raise ValueError("min_value must be less than or equal to max_value.")
    if valid_values:
        if min_value and max_value:
            valid_values = [
                val for val in valid_values if min_value <= val <= max_value
            ]
        elif min_value:
            valid_values = [val for val in valid_values if min_value <= val]
        elif max_value:
            valid_values = [val for val in valid_values if val <= max_value]

        if not valid_values:
            raise ValueError("Min and max range must include at least one valid value")
    if default_value != None:
        try:
            # Convert to a string first, to prevent float -> int conversion
            default_value = class_(str(default_value))
        except (ValueError, TypeError, OverflowError):
            raise ValueError("The default value {} cannot be cast to type {}".format(default_value, class_.__name__))

    # Validation of input
    while True:
        try:
            data = input(message)
            if allow_exit and data == "":
                return default_value
            breakpoint()
            data = class_(data)
        except ValueError:
            print(
                "Please enter a value of type {}.".format(class_.__name__)
            )
            continue

        if min_value is not None:
            if data < min_value:
                print(
                    "Ensure the value is greater than {}".format(min_value)
                )
                continue
        if max_value is not None:
            if data > max_value:
                print("Ensure the value is less than {}".format(max_value))
                continue
        if valid_values:
            if data not in valid_values:
                print("Value must be one of {}".format(valid_values))
                continue
        # If all goes well, break
        break
    return data

