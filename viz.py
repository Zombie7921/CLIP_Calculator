import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def select_chart_type(chart_name="chart"):
    """
    Prompt the user to select a chart type with a default option if no input is provided.
    
    :param chart_name: Name of the chart type context (e.g., 'summary chart' or 'single-image chart').
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
    
    choice = input(f"Enter the number corresponding to your choice for the {chart_name} (1-10, default is 1): ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= 10):
        print(f"Invalid or no input provided. Defaulting to Line Chart for {chart_name}.")
        return 1
    return int(choice)

def select_color(chart_name="chart"):
    """
    Prompt the user to select a color with a default option if no input is provided.
    
    :param chart_name: Name of the chart type context.
    :return: Selected color (hex string).
    """
    print(f"Enter the color you want to use for the {chart_name} (hex code, e.g., #1f77b4):")
    color = input(f"Color for the {chart_name} (default is #1f77b4): ").strip()

    if not color or not (color.startswith("#") and len(color) == 7):
        print(f"Invalid or no input provided. Defaulting to color #1f77b4 for {chart_name}.")
        return "#1f77b4"
    return color

def prompt_advanced_settings():
    """
    Prompts the user for advanced chart settings like figure size and labels.
    """
    print("Do you want to enable advanced settings? (yes/no):")
    advanced = input("Advanced settings (default: no): ").strip().lower()

    if advanced == "yes":
        print("Enter the desired figure size (width, height) as two numbers separated by a comma (e.g., 12,6):")
        try:
            figsize = tuple(map(int, input("Figure size: ").split(',')))
        except ValueError:
            print("Invalid input. Using default size (12, 6).")
            figsize = (12, 6)

        xlabel = input("x-axis label (default: Image Names): ").strip() or "Image Names"
        ylabel = input("y-axis label (default: CLIP Scores): ").strip() or "CLIP Scores"

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

def visualize_summary(scores, chart_type, color, settings, output_dir):
    """Generates the summary chart for all images."""
    image_names = [f"Target_{score['image_index']}" for score in scores]
    clip_scores = [score['clip_score'] for score in scores]
    
    plt.figure(figsize=settings['figsize'])
    
    if chart_type == 1:  # Line Chart
        plt.plot(image_names, clip_scores, marker='o', color=color)
        plt.title('Line Chart of CLIP Scores', fontsize=14)
    elif chart_type == 2:  # Histogram
        plt.bar(image_names, clip_scores, color=color, width=0.4)
        plt.title('Histogram of CLIP Scores', fontsize=14)
    elif chart_type == 3:  # Dot Chart
        plt.scatter(image_names, clip_scores, color=color, s=100)
        plt.title('Dot Chart of CLIP Scores', fontsize=14)
    elif chart_type == 4:  # Scatter Chart
        plt.scatter(range(len(image_names)), clip_scores, color=color, s=100)
        plt.xticks(range(len(image_names)), image_names, rotation=45, fontsize=10)
        plt.title('Scatter Chart of CLIP Scores', fontsize=14)
    elif chart_type == 5:  # Box Plot
        plt.boxplot(clip_scores, patch_artist=True, boxprops=dict(facecolor=color))
        plt.xticks([1], ['CLIP Scores'], fontsize=12)
        plt.title('Box Plot of CLIP Scores', fontsize=14)
    elif chart_type == 6:  # Violin Plot
        sns.violinplot(data=clip_scores, color=color)
        plt.xticks([0], ['CLIP Scores'], fontsize=12)
        plt.title('Violin Plot of CLIP Scores', fontsize=14)
    elif chart_type == 7:  # Area Chart
        plt.fill_between(range(len(image_names)), clip_scores, color=color, alpha=0.5)
        plt.plot(range(len(image_names)), clip_scores, color=color)
        plt.xticks(range(len(image_names)), image_names, rotation=45, fontsize=10)
        plt.title('Area Chart of CLIP Scores', fontsize=14)
    elif chart_type == 8:  # Pie Chart
        plt.pie(clip_scores, labels=image_names, colors=[color] * len(image_names), autopct='%1.1f%%', startangle=140)
        plt.title('Pie Chart of CLIP Scores', fontsize=14)
    elif chart_type == 9:  # Heatmap
        data = np.array(clip_scores).reshape(1, -1)
        sns.heatmap(data, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
        plt.yticks([0.5], ['CLIP Scores'], rotation=0)
        plt.xticks(range(len(image_names)), image_names, rotation=45, fontsize=10)
        plt.title('Heatmap of CLIP Scores', fontsize=14)
    elif chart_type == 10:  # 3D Scatter Plot
        fig = plt.figure(figsize=settings['figsize'])
        ax = fig.add_subplot(111, projection='3d')
        z_data = np.random.rand(len(image_names))  # Example Z-axis data
        ax.scatter(range(len(image_names)), clip_scores, z_data, color=color, s=100)
        ax.set_xticks(range(len(image_names)))
        ax.set_xticklabels(image_names, rotation=45, fontsize=10)
        ax.set_xlabel(settings['xlabel'], fontsize=12)
        ax.set_ylabel(settings['ylabel'], fontsize=12)
        ax.set_zlabel('Random Z', fontsize=12)
        ax.set_title('3D Scatter Plot of CLIP Scores', fontsize=14)
        return fig # Returning fig to avoid double plotting if handled outside

    plt.xlabel(settings['xlabel'], fontsize=12)
    plt.ylabel(settings['ylabel'], fontsize=12)
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "clip_scores_summary.png")
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Batch-wide chart saved to {output_path}")
    plt.close()

def visualize_single_images(scores, chart_type, color, settings, output_dir):
    """Generates charts for individual images."""
    os.makedirs(output_dir, exist_ok=True)
    clip_scores = [score['clip_score'] for score in scores]
    global_ymin = min(clip_scores) - 0.01
    global_ymax = max(clip_scores) + 0.01

    for score in scores:
        plt.figure(figsize=settings['figsize'])
        image_label = f"Target_{score['image_index']}"
        score_val = score['clip_score']
        
        if chart_type == 1:  # Line Chart
            plt.plot([image_label], [score_val], marker='o', color=color)
        elif chart_type == 2:  # Histogram
            plt.bar([image_label], [score_val], color=color, width=0.4)
        elif chart_type == 3:  # Dot Chart
            plt.scatter([image_label], [score_val], color=color, s=100)
        elif chart_type == 4:  # Scatter Chart
            plt.scatter([score['image_index']], [score_val], color=color, s=100)
        elif chart_type == 5:  # Box Plot
            plt.boxplot([score_val], patch_artist=True, boxprops=dict(facecolor=color))
        elif chart_type == 6:  # Violin Plot
            sns.violinplot(data=[score_val], color=color)
        elif chart_type == 7:  # Area Chart
            plt.fill_between([image_label], [score_val], color=color, alpha=0.5)
            plt.plot([image_label], [score_val], color=color)

        plt.ylim(global_ymin, global_ymax)
        plt.title(f"CLIP Score for {image_label}", fontsize=14)
        plt.xlabel("Image", fontsize=12)
        plt.ylabel("CLIP Score", fontsize=12)
        
        output_path = os.path.join(output_dir, f"{image_label}_chart.png")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
    
    print(f"Single-image charts saved to {output_dir}")

def visualize(scores, summary_chart_type, summary_color, advanced_settings, charts_dir, images_chart_dir, single_chart_type=1, single_chart_color="#1f77b4"):
    """
    Main visualization entry point.
    """
    visualize_summary(scores, summary_chart_type, summary_color, advanced_settings, charts_dir)
    visualize_single_images(scores, single_chart_type, single_chart_color, advanced_settings, images_chart_dir)
