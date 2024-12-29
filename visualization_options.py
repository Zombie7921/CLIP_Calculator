import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def visualize(scores, summary_chart_type, summary_color, advanced_settings, charts_dir, images_chart_dir, single_chart_type=1, single_chart_color="#1f77b4"):
    """
    Visualizes CLIP scores for multiple and single images.

    :param scores: List of dictionaries containing 'image_index' and 'clip_score'.
    :param summary_chart_type: The type of chart for the summary (batch-wide) chart.
    :param summary_color: The color for the summary chart (hex value).
    :param advanced_settings: Dictionary with 'figsize', 'xlabel', and 'ylabel'.
    :param charts_dir: Directory to save batch-wide charts.
    :param images_chart_dir: Directory to save single-image charts.
    :param single_chart_type: The type of chart for single-image charts.
    :param single_chart_color: The color for single-image charts (hex value).
    """
    if not os.path.exists(charts_dir):
        os.makedirs(charts_dir)

    if not os.path.exists(images_chart_dir):
        os.makedirs(images_chart_dir)

    # Prepare data
    image_names = [f"Target_{score['image_index']}" for score in scores]
    clip_scores = [score['clip_score'] for score in scores]

    # Determine the global y-axis range for single-image charts
    global_ymin = min(clip_scores) - 0.01  # Add some padding
    global_ymax = max(clip_scores) + 0.01

    # Batch-wide chart
    plt.figure(figsize=advanced_settings['figsize'])
    if summary_chart_type == 1:  # Line Chart
        plt.plot(image_names, clip_scores, marker='o', color=summary_color)
        plt.title('Line Chart of CLIP Scores', fontsize=14)
    elif summary_chart_type == 2:  # Histogram
        plt.bar(image_names, clip_scores, color=summary_color, width=0.4)
        plt.title('Histogram of CLIP Scores', fontsize=14)
    elif summary_chart_type == 3:  # Dot Chart
        plt.scatter(image_names, clip_scores, color=summary_color, s=100)
        plt.title('Dot Chart of CLIP Scores', fontsize=14)
    elif summary_chart_type == 4:  # Scatter Chart
        plt.scatter(range(len(image_names)), clip_scores, color=summary_color, s=100)
        plt.xticks(range(len(image_names)), image_names, rotation=45, fontsize=10)
        plt.title('Scatter Chart of CLIP Scores', fontsize=14)
    elif summary_chart_type == 5:  # Box Plot
        plt.boxplot(clip_scores, patch_artist=True, boxprops=dict(facecolor=summary_color))
        plt.xticks([1], ['CLIP Scores'], fontsize=12)
        plt.title('Box Plot of CLIP Scores', fontsize=14)
    elif summary_chart_type == 6:  # Violin Plot
        sns.violinplot(data=clip_scores, color=summary_color)
        plt.xticks([0], ['CLIP Scores'], fontsize=12)
        plt.title('Violin Plot of CLIP Scores', fontsize=14)
    elif summary_chart_type == 7:  # Area Chart
        plt.fill_between(range(len(image_names)), clip_scores, color=summary_color, alpha=0.5)
        plt.plot(range(len(image_names)), clip_scores, color=summary_color)
        plt.xticks(range(len(image_names)), image_names, rotation=45, fontsize=10)
        plt.title('Area Chart of CLIP Scores', fontsize=14)
    elif summary_chart_type == 8:  # Pie Chart
        plt.pie(clip_scores, labels=image_names, colors=[summary_color] * len(image_names), autopct='%1.1f%%', startangle=140)
        plt.title('Pie Chart of CLIP Scores', fontsize=14)
    elif summary_chart_type == 9:  # Heatmap
        data = np.array(clip_scores).reshape(1, -1)
        sns.heatmap(data, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
        plt.yticks([0.5], ['CLIP Scores'], rotation=0)
        plt.xticks(range(len(image_names)), image_names, rotation=45, fontsize=10)
        plt.title('Heatmap of CLIP Scores', fontsize=14)
    elif summary_chart_type == 10:  # 3D Scatter Plot
        fig = plt.figure(figsize=advanced_settings['figsize'])
        ax = fig.add_subplot(111, projection='3d')
        z_data = np.random.rand(len(image_names))  # Example Z-axis data
        ax.scatter(range(len(image_names)), clip_scores, z_data, color=summary_color, s=100)
        ax.set_xticks(range(len(image_names)))
        ax.set_xticklabels(image_names, rotation=45, fontsize=10)
        ax.set_xlabel(advanced_settings['xlabel'], fontsize=12)
        ax.set_ylabel(advanced_settings['ylabel'], fontsize=12)
        ax.set_zlabel('Random Z', fontsize=12)
        ax.set_title('3D Scatter Plot of CLIP Scores', fontsize=14)

    plt.xlabel(advanced_settings['xlabel'], fontsize=12)
    plt.ylabel(advanced_settings['ylabel'], fontsize=12)

    # Save batch-wide chart
    batch_chart_path = os.path.join(charts_dir, "clip_scores_summary.png")
    plt.tight_layout()
    plt.savefig(batch_chart_path)
    print(f"Batch-wide chart saved to {batch_chart_path}")
    plt.close()

    # Single-image charts
    for score in scores:
        plt.figure(figsize=advanced_settings['figsize'])
        if single_chart_type == 1:  # Line Chart
            plt.plot([f"Target_{score['image_index']}"], [score['clip_score']], marker='o', color=single_chart_color)
        elif single_chart_type == 2:  # Histogram
            plt.bar([f"Target_{score['image_index']}"], [score['clip_score']], color=single_chart_color, width=0.4)
        elif single_chart_type == 3:  # Dot Chart
            plt.scatter([f"Target_{score['image_index']}"], [score['clip_score']], color=single_chart_color, s=100)
        elif single_chart_type == 4:  # Scatter Chart
            plt.scatter([score['image_index']], [score['clip_score']], color=single_chart_color, s=100)
        elif single_chart_type == 5:  # Box Plot
            plt.boxplot([score['clip_score']], patch_artist=True, boxprops=dict(facecolor=single_chart_color))
        elif single_chart_type == 6:  # Violin Plot
            sns.violinplot(data=[score['clip_score']], color=single_chart_color)
        elif single_chart_type == 7:  # Area Chart
            plt.fill_between([f"Target_{score['image_index']}"], [score['clip_score']], color=single_chart_color, alpha=0.5)
            plt.plot([f"Target_{score['image_index']}"], [score['clip_score']], color=single_chart_color)

        plt.ylim(global_ymin, global_ymax)  # Ensure consistent y-axis range across all single-image charts
        plt.title(f"CLIP Score for Target_{score['image_index']}", fontsize=14)
        plt.xlabel("Image", fontsize=12)
        plt.ylabel("CLIP Score", fontsize=12)
        single_chart_path = os.path.join(images_chart_dir, f"Target_{score['image_index']}_chart.png")
        plt.tight_layout()
        plt.savefig(single_chart_path)
        print(f"Single-image chart saved to {single_chart_path}")
        plt.close()
