def calculate_alarm_time():
    current_time_str = input("Enter the current time (in HH:MM format): ")
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
    time_parts = current_time_str.split(':')
    if len(time_parts) != 2:
        print("Invalid time format. Please use HH:MM format.")
        return
    
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        print("Invalid current time. Please enter a time in HH:MM format, where HH is between 0 and 23 and MM is between 0 and 59.")
        return
    
    if hours_to_wait < 0:
        print("Invalid hours to wait. Please enter a non-negative number.")
        return
    
    total_minutes = (hours * 60 + minutes) + (hours_to_wait * 60)
    alarm_hours = (total_minutes // 60) % 24
    alarm_minutes = total_minutes % 60
    
    print(f"The alarm will go off at: {alarm_hours:02}:{alarm_minutes:02}")

calculate_alarm_time()
