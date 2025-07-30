import matplotlib.pyplot as plt
import os


class PlotManager:
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    assets_path = os.path.join(root_path, "Assets")

    def __init__(self):
        pass

    @staticmethod
    def saveMemoryUsagePlot(memory_usage):
        labels = list(memory_usage.keys())
        values = [memory_usage[label] / 1024 for label in labels]
        plt.figure(figsize=(10, 6))
        bars = plt.bar(labels, values, color=["#66c2a5", "#fc8d62", "#8da0cb"])
        plt.title("Memory Usage of Data Structures (KB)")
        plt.ylabel("Memory (KB)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 50, f"{height:.0f} KB",
                     ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        path = os.path.join(PlotManager.assets_path, "memory_usage.jpeg")
        plt.savefig(path, format="jpeg")

    @staticmethod
    def saveOSSelectTimePlot(times, tries):
        labels = list(times.keys())
        values = list(times.values())

        plt.figure(figsize=(8, 5))
        bars = plt.bar(labels, values, color=["#66c2a5", "#fc8d62", "#8da0cb"])
        plt.title(f"OSSelect Time for {tries} Tries")
        plt.ylabel("Time (seconds)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + max(values) * 0.02, f"{height:.4f}s", ha='center',
                     va='bottom')

        plt.tight_layout()
        path = os.path.join(PlotManager.assets_path, "OSSelect_Time.jpeg")
        plt.savefig(path, format="jpeg")

    @staticmethod
    def saveOSRankTimePlot(times, tries):
        labels = list(times.keys())
        values = list(times.values())

        plt.figure(figsize=(8, 5))
        bars = plt.bar(labels, values, color=["#66c2a5", "#fc8d62", "#8da0cb"])
        plt.title(f"OSRank Time for {tries} Tries")
        plt.ylabel("Time (seconds)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + max(values) * 0.02, f"{height:.4f}s", ha='center',
                     va='bottom')

        plt.tight_layout()
        path = os.path.join(PlotManager.assets_path, "OSRank_Time.jpeg")
        plt.savefig(path, format="jpeg")