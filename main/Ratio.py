
def calculate_metrics(assignments, total_casualties):
    total_priority = 0
    camp_sums = []
    
    for camp, allocated in assignments.items():
        camp_sum = sum(c['p_age'] * c['p_emerg'] for c in allocated)
        camp_sums.append(camp_sum)
        total_priority += camp_sum
        
    rescue_ratio = total_priority / total_casualties if total_casualties > 0 else 0
    return camp_sums, rescue_ratio

