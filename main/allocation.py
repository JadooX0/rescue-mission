import math

def allocate_casualties(casualties, rescue_pads):
    
    assignments = {'Pink': [], 'Blue': [], 'Grey': []}
    
    
    casualties.sort(key=lambda x: (x['p_age'] * x['p_emerg'], x['p_emerg']), reverse=True)
    
    for c in casualties:
        best_pad = None
        max_score = -float('inf')
        
        for pad_name, pad_info in rescue_pads.items():
            
            if len(assignments[pad_name]) < pad_info['capacity']:
                
                dist = math.dist(c['pos'], pad_info['pos'])
                
                
                priority = c['p_age'] * c['p_emerg']
                score = priority - math.log10(dist + 1)
                
                if score > max_score:
                    max_score = score
                    best_pad = pad_name
        
        if best_pad:
            assignments[best_pad].append(c)
            
    return assignments




rescue_pads = {
    "Pink": {"pos": (100, 100), "capacity": 3},
    "Blue": {"pos": (500, 500), "capacity": 4},
    "Grey": {"pos": (300, 800), "capacity": 2}
}


detected_casualties_list = [
    {'pos': (120, 150), 'p_age': 3, 'p_emerg': 3}, 
    {'pos': (450, 480), 'p_age': 2, 'p_emerg': 2}, 
    {'pos': (310, 790), 'p_age': 1, 'p_emerg': 1}  
]


final_results = allocate_casualties(detected_casualties_list, rescue_pads)


print("--- RESCUE MISSION COMPLETE ---")
for pad in ["Blue", "Pink", "Grey"]:
    count = len(final_results[pad])
    print(f"{pad} Pad ({count}): {final_results[pad]}")


all_priorities = [(c['p_age'] * c['p_emerg']) for pad in final_results.values() for c in pad]

if all_priorities:
    rescue_ratio = sum(all_priorities) / len(all_priorities)
    print(f"\nRescue Ratio (Pr): {rescue_ratio:.2f}")
else:
    print("\nNo casualties detected to calculate Ratio.")

    
all_priorities = []
for pad_name in final_results:
    for casualty in final_results[pad_name]:
        
        score = casualty['p_age'] * casualty['p_emerg']
        all_priorities.append(score)


if len(all_priorities) > 0:
    rescue_ratio = sum(all_priorities) / len(all_priorities)
    print(f"Rescue Ratio (Pr): {rescue_ratio:.2f}")