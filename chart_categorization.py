def prompt_chart_type():
    print("Choose a chart type for visualization:")
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
    choice = input("Enter the number corresponding to your choice (1-10): ")
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("Invalid choice. Please select a valid option.")
        choice = input("Enter the number corresponding to your choice (1-10): ")
    return int(choice)

def prompt_color_choice():
    print("Enter the color you want to use for the chart (hex code, e.g., #1f77b4):")
    color = input("Color: ")
    while not (color.startswith("#") and len(color) == 7):
        print("Invalid color code. Please enter a valid hex color code (e.g., #1f77b4).")
        color = input("Color: ")
    return color

def prompt_advanced_settings():
    print("Do you want to enable advanced settings? (yes/no):")
    advanced = input("Advanced settings: ").strip().lower()
    while advanced not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        advanced = input("Advanced settings: ").strip().lower()

    if advanced == "yes":
        print("Enter the desired figure size (width, height) as two numbers separated by a comma (e.g., 12,6):")
        try:
            figsize = tuple(map(int, input("Figure size: ").split(',')))
        except ValueError:
            print("Invalid input. Using default size (12, 6).")
            figsize = (12, 6)

        print("Enter the x-axis label:")
        xlabel = input("x-axis label: ")

        print("Enter the y-axis label:")
        ylabel = input("y-axis label: ")

        return {
            "figsize": figsize,
            "xlabel": xlabel,
            "ylabel": ylabel
        }
    else:
        return {
            "figsize": (12, 6),
            "xlabel": "Image Names",
            "ylabel": "CLIP Scores"
        }
