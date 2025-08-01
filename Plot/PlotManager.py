import matplotlib.pyplot as plt
import os



class PlotManager:
    """
        Class to Manage Data-Plots and image savings.
    """
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    assets_path = os.path.join(root_path, "Assets")

    def __init__(self):
        pass

    @staticmethod
    def saveMemoryUsagePlot(memory_usage):
        """
            Create and save a bar plot of memory usage for different data structures.

            The plot displays memory usage in kilobytes (KB) with labels and values
            above each bar for clarity.  Saves the plot image as 'memory_usage.jpeg' in the 'Assets' folder.

            Parameters:
                memory_usage (dict): A dictionary where keys are data structure names
                                     and values are memory usage in bytes.

            Returns:
                None
        """
        labels = list(memory_usage.keys())
        values = [memory_usage[label] / 1024 for label in labels]
        plt.figure(figsize=(10, 6))
        bars = plt.bar(labels, values, color=["#66c2a5", "#fc8d62", "#8da0cb"])
        plt.title("Memory Usage of Data Structures (KB)")
        plt.ylabel("Memory (KB)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2, height + 50, f"{height:.0f} KB",
                ha='center', va='bottom', fontsize=10
            )

        plt.tight_layout()
        path = os.path.join(PlotManager.assets_path, "memory_usage.jpeg")
        plt.savefig(path, format="jpeg")

    @staticmethod
    def saveOSSelectTimePlot(times, tries):
        """
            Create and save a bar plot showing OSSelect operation times for different data structures.
            Saves the plot image as 'OSSelect_Time.jpeg' in the 'Assets' folder.

            Parameters:
                times (dict): A dictionary mapping data structure names to elapsed times in seconds.
                tries (int): The number of tries or iterations over which the times were measured.

            Returns:
                None
        """
        labels = list(times.keys())
        values = list(times.values())

        plt.figure(figsize=(8, 5))
        bars = plt.bar(labels, values, color=["#66c2a5", "#fc8d62", "#8da0cb"])
        plt.title(f"OSSelect Time for {tries} Tries")
        plt.ylabel("Time (seconds)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2, height + max(values) * 0.02, f"{height:.4f}s", ha='center',
                va='bottom'
            )

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

    @staticmethod
    def saveOSOperationComplexityPlot(results_by_n, operation_name):
        """
            Create and save a plot showing execution time growth with input size for different data structures,
            compared against theoretical complexity curves.
            Saves the plot image as '{operation_name}_Time_vs_n.jpeg' in the 'Assets' folder.

            Parameters:
                results_by_n (dict): A nested dictionary structured with sizes and times.
                operation_name (str): The name of the operation ("OSSelect" or "OSRank") to include
                in the plot title and filename.

            Returns:
                None

        """
        import numpy as np

        plt.figure(figsize=(10, 6))
        ns = sorted(results_by_n.keys())  # Input sizes
        structures = list(next(iter(results_by_n.values())).keys())  # Data structures

        # Plot empirical timing data for each data structure
        for structure in structures:
            ys = [results_by_n[n][structure] for n in ns]
            plt.plot(ns, ys, marker='o', label=structure)

        # Compute reference complexity curves (normalized for comparison)
        max_n = max(ns)
        normalized_n = np.array(ns) / max_n
        ref_n = normalized_n
        ref_log_n = np.log2(ns) / np.log2(max_n)
        ref_nlogn = ref_n * ref_log_n

        # Scale reference curves to fit the plot visually
        max_y = max([results_by_n[n][s] for n in ns for s in structures])
        plt.plot(ns, ref_log_n * max_y, 'k--', label="O(log n)")
        plt.plot(ns, ref_n * max_y, 'k-.', label="O(n)")
        plt.plot(ns, ref_nlogn * max_y, 'k:', label="O(n log n)")

        plt.title(f"{operation_name} Time vs n")
        plt.xlabel("n (number of elements)")
        plt.ylabel("Time (seconds)")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()

        # Save plot to file
        path = os.path.join(PlotManager.assets_path, f"{operation_name}_Time_vs_n.jpeg")
        plt.savefig(path, format="jpeg")