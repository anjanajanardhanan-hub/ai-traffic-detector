# import matplotlib.pyplot as plt

# traffic_data = [80, 75, 90, 70, 85, 95]

# def create_graph(new_value=None):
#     global traffic_data

#     if new_value is not None:
#         traffic_data.append(new_value)

#     if len(traffic_data) > 10:
#         traffic_data.pop(0)

#     # Use a dark theme base
#     plt.style.use('dark_background')
    
#     # Set the figure size and the facecolor to match your dashboard navy (#0B0F1A)
#     fig, ax = plt.subplots(figsize=(7, 4), facecolor='#0B0F1A')
#     ax.set_facecolor('#1F2937') # Matches your .box background color

#     # Plot the traffic with the professional blue (#3B82F6)
#     ax.plot(traffic_data, marker='o', color='#3B82F6', linewidth=2, label="Traffic")
    
#     # Add a soft blue fill under the line for a modern look
#     ax.fill_between(range(len(traffic_data)), traffic_data, color='#3B82F6', alpha=0.1)

#     # Threshold line - professional red (#EF4444)
#     threshold = 150
#     ax.axhline(y=threshold, color='#EF4444', linestyle='--', linewidth=1.5, label="Threshold")

#     # Highlight anomalies with a larger red dot
#     for i, val in enumerate(traffic_data):
#         if val > threshold:
#             ax.scatter(i, val, color='#EF4444', s=120, edgecolors='white', zorder=5)

#     # Styling the text and grid
#     ax.set_title("Traffic Monitoring", color='#F9FAFB', fontsize=14, pad=15)
#     ax.set_xlabel("Time", color='#94A3B8')
#     ax.set_ylabel("Requests per minute", color='#94A3B8')
    
#     # Grid and spines styling
#     ax.grid(color='#374151', linestyle='-', linewidth=0.5, alpha=0.5)
#     for spine in ax.spines.values():
#         spine.set_color('#374151')

#     # Legend placement and style
#     legend = ax.legend(facecolor='#111827', edgecolor='#374151')
#     plt.setp(legend.get_texts(), color='#F9FAFB')

#     # Save with tight layout to prevent clipping
#     plt.savefig("static/graph.png", bbox_inches='tight', facecolor=fig.get_facecolor())
#     plt.close()

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

traffic_data = [80, 75, 90, 70, 85, 95]

def create_graph(new_value=None):
    global traffic_data

    if new_value is not None:
        traffic_data.append(new_value)

    if len(traffic_data) > 10:
        traffic_data.pop(0)

    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(7, 4), facecolor='#0B0F1A')
    ax.set_facecolor('#1F2937')

    ax.plot(traffic_data, marker='o', color='#3B82F6', linewidth=2, label="Traffic")

    ax.fill_between(range(len(traffic_data)), traffic_data, color='#3B82F6', alpha=0.1)

    threshold = 150
    ax.axhline(y=threshold, color='#EF4444', linestyle='--', linewidth=1.5, label="Threshold")

    for i, val in enumerate(traffic_data):
        if val > threshold:
            ax.scatter(i, val, color='#EF4444', s=120, edgecolors='white', zorder=5)

    ax.set_title("Traffic Monitoring", color='#F9FAFB', fontsize=14, pad=15)
    ax.set_xlabel("Time", color='#94A3B8')
    ax.set_ylabel("Requests per minute", color='#94A3B8')

    ax.grid(color='#374151', linestyle='-', linewidth=0.5, alpha=0.5)

    for spine in ax.spines.values():
        spine.set_color('#374151')

    legend = ax.legend(facecolor='#111827', edgecolor='#374151')
    plt.setp(legend.get_texts(), color='#F9FAFB')

    plt.savefig("static/graph.png", bbox_inches='tight', facecolor=fig.get_facecolor())

    plt.close()