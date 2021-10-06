import math
can_list = ["1Picnic", "1Tall", "#2", "#2.5", "3Cylinder", "5","6z", "8Z short", "10", "211" "300", "303"]
radii_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]


def main():

    for i in range(len(can_list)):
        radius = radii_list[i]
        height = height_list[i]
        volume = cylinder_volume(radius, height)
        surface_area =cylinder_surface_area(radius, height)
        storage_efficiency = volume / surface_area
        print(f"The Storage Efficiency for can {can_list[i]} is {storage_efficiency:.1f}")
    
    
    


def cylinder_surface_area (radius, height):
    surface_area = 2 * math.pi * radius *( radius + height)
    return surface_area

def cylinder_volume(radius, height):
    
        volume = math.pi * radius **2 * height

        return volume
    
main()