def is_triangular(n):
    """
    Check if a number is a triangular number.
    """

    triangular_sum = 0
    i = 1
    
    while triangular_sum < n:
        triangular_sum += i
        if triangular_sum == n:
            return True
        i += 1
    
    return False

def decode(message_file):
    with open(message_file, 'r') as message:
        lines = message.readlines()

        lines.sort(key=lambda x: int(x.split()[0]))

        words = []

        position = 0

        for line in lines:
            num, word = line.split()

            num = int(num)

            position += 1

            if is_triangular(position):
                words.append(word)

        decoded_message = ' '.join(words)

        return decoded_message
    
print(decode("coding_qual_input.txt"))




