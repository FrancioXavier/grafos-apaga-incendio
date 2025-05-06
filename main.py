
import read_data as read_data
import functions as f
if __name__ == "__main__":
    data = read_data.read_data("data.txt")

    num_vertices = data['num_vertices']
    num_edges = data['num_edges']
    fire_start = data['fire_start']

    graph = f.create_graph(num_vertices, data['edges'])
