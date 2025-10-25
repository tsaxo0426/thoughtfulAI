def sort(width, height, length, mass):
    volume = width * height * length

    if width > 150 or height > 150 or length > 150:
        if mass >= 20:
            return "REJECTED"
        return "SPECIAL"
    
    if volume >= 1000000:
        return "SPECIAL"
    
    if mass >= 20:
        return "SPECIAL"
    
    return "STANDARD"


if __name__ == "__main__":
    # Example usage
    package_type = sort(160, 100, 50, 25)
    print(package_type)  # Output: REJECTED