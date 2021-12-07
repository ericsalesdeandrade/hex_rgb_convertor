# Reference - https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
# https://donatbalipapp.medium.com/colours-maths-90346fb5abda

def convert_hex_to_rgb(hex_input: str) -> tuple:
    """
    Function to convert Hex input to RGB
    :param hex_input: Input in Hex format, string
    :return: Output in RGB format, tuple
    """
    hex_input_stripped = hex_input.lstrip('#')
    rgb_value = tuple(int(hex_input_stripped[i:i + 2], 16) for i in (0, 2, 4))
    print(f"Hex Value {hex_input} in RGB is {rgb_value}")
    return rgb_value


def get_avg(input_1: tuple, input_2: tuple) -> tuple:
    """
    Function to get average of 2 tuples
    :param input_1: RGB value 1, tuple
    :param input_2: RGB value 2, tuple
    :return: Average of 2 tuples, tuple
    """
    x = (input_1, input_2)
    avg_val = tuple(int(sum(y) / len(y)) for y in zip(*x))
    print(f"The RGB Average Value is {avg_val}")
    return avg_val


def convert_rgb_to_hex(rgb_input: tuple) -> str:
    """
    Function to convert RGB into Hex
    :param rgb_input: Input in RGB format, tuple
    :return: Output in Hex format, string
    """
    print(f"Converting {rgb_input} back into Hex...")
    return '#%02x%02x%02x' % rgb_input


def get_avg_2_hex(hex_input1: str, hex_input2: str) -> str:
    """
    Wrapper Function to execute all the above functions i.e. get average hex value of 2 input hex values via RGB conversion
    :param hex_input1: Hex input 1, string
    :param hex_input2: Hex input 2, string
    :return: Average hex value of 2 input hex values, string
    """
    rgb_value_1 = convert_hex_to_rgb(hex_input1)
    rgb_value_2 = convert_hex_to_rgb(hex_input2)
    avg_hex_value = get_avg(rgb_value_1, rgb_value_2)
    converted_avg_hex_value = convert_rgb_to_hex(avg_hex_value)
    print(f"The Avg Value in Hex is {converted_avg_hex_value}")
    return converted_avg_hex_value


if __name__ == "__main__":
    hex_input_1 = "#369BE5"
    hex_input_2 = "#FF5733"
    get_avg_2_hex(hex_input_1, hex_input_2)
