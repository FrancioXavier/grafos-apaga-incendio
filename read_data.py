def read_data(file_path):
    data = {
        'num_vertices': 0,
        'num_edges': 0,
        'edges': [],
        'water_needed': {},
        'fire_start': None,
        'water_collection_points': [],
        'firefighter_stations': [],
        'truck_capacity': 0
    }
    
    current_section = None
    
    with open(file_path, 'r') as file:
        for line in file:
            # Skip comments and empty lines
            line = line.strip()
            if not line or line.startswith('//') or line.startswith('#'):
                if '#Numero de vertices' in line:
                    current_section = 'vertices_edges'
                elif '#Arestas:' in line:
                    current_section = 'edges'
                elif '#Agua necessaria:' in line:
                    current_section = 'water_needed'
                elif '#Ponto inicial incendio:' in line:
                    current_section = 'fire_start'
                elif '#Pontos de coleta de agua:' in line:
                    current_section = 'water_collection'
                elif '#Postos de brigadistas:' in line:
                    current_section = 'firefighters'
                elif '#Capacidade caminhoes:' in line:
                    current_section = 'truck_capacity'
                continue
            
            if current_section == 'vertices_edges':
                parts = line.split()
                data['num_vertices'] = int(parts[0])
                data['num_edges'] = int(parts[1])
                current_section = None
            
            elif current_section == 'edges':
                parts = line.split()
                if len(parts) == 3:
                    source, target, cost = int(parts[0]), int(parts[1]), int(parts[2])
                    data['edges'].append((source, target, cost))
            
            elif current_section == 'water_needed':
                parts = line.split()
                if len(parts) == 2:
                    vertex, water = int(parts[0]), int(parts[1])
                    data['water_needed'][vertex] = water
            
            elif current_section == 'fire_start':
                data['fire_start'] = int(line.strip())
                current_section = None
            
            elif current_section == 'water_collection':
                parts = line.split()
                data['water_collection_points'] = [int(vertex) for vertex in parts]
                current_section = None
            
            elif current_section == 'firefighters':
                parts = line.split()
                data['firefighter_stations'] = [int(vertex) for vertex in parts]
                current_section = None
            
            elif current_section == 'truck_capacity':
                data['truck_capacity'] = int(line.strip())
                current_section = None
    return data
