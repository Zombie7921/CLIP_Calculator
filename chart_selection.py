def select_chart_type(chart_name):
    """
    Prompt the user to select a chart type with a default option if no input is provided.

    :param chart_name: Name of the chart type prompts (e.g., 'summary chart' or 'single-image chart').
    :return: Selected chart type (integer).
    """
    print(f"Choose a chart type for the {chart_name}:")
    print("1. Line Chart")
    print("2. Histogram")
    print("3. Dot Chart")
    print("4. Scatter Chart")
    print("5. Box Plot")
    print("6. Violin Plot")
    print("7. Area Chart")
    print("8. Pie Chart")
    print("9. Heatmap")
    print("10. 3D Scatter Plot")
    choice = input(f"Enter the number corresponding to your choice for the {chart_name} (1-10, default is 1): ")

    # Default to Line Chart if input is invalid or empty
    if not choice.isdigit() or not (1 <= int(choice) <= 10):
        print(f"Invalid or no input provided. Defaulting to Line Chart for {chart_name}.")
        return 1
    return int(choice)

def select_color(chart_name):
    """
    Prompt the user to select a color with a default option if no input is provided.

    :param chart_name: Name of the chart type prompts (e.g., 'summary chart' or 'single-image chart').
    :return: Selected color (hex string).
    """
    print(f"Enter the color you want to use for the {chart_name} (hex code, e.g., #1f77b4):")
    color = input(f"Color for the {chart_name} (default is #1f77b4): ")

    # Default to blue (#1f77b4) if input is empty or invalid
    if not color or not (color.startswith("#") and len(color) == 7):
        print(f"Invalid or no input provided. Defaulting to color #1f77b4 for {chart_name}.")
        return "#1f77b4"
    return color
