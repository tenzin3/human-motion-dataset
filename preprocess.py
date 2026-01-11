import re
from collections import defaultdict

def create_motion_dict(text):
    # Using defaultdict(list) so we can append multiple IDs to one motion key
    motion_map = defaultdict(list)
    
    # Regex pattern: 
    # ^(\d+_\d+) matches the ID at the start (e.g., 01_01)
    # \s+ matches the whitespace/tab
    # (.+) matches the rest of the line (the description)
    pattern = re.compile(r'^(\d+_\d+)\s+(.+)')

    for line in text.strip().split('\n'):
        match = pattern.match(line.strip())
        if match:
            motion_id, description = match.groups()
            
            # Clean the description (lowercase for easier searching)
            description = description.strip().lower()
            
            # Add to dictionary
            motion_map[description].append(motion_id)
            
    return dict(motion_map)

if __name__ == "__main__":
    import json

    # Read the raw data from the text file
    with open("cmu-mocap-index-text.txt", "r") as f:
        raw_data = f.read()
    
    # Generate the dictionary
    mocap_dict = create_motion_dict(raw_data)

    # Save the dictionary to a JSON file
    with open("motion_mapping.json", "w") as f:
        json.dump(mocap_dict, f, indent=4)
