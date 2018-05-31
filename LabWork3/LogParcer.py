import re

if __name__ == "__main__":

    pattern = r"\S+\s-\s-\s\[01/Jul/1995:03:(?:3[5-9]|4\d|5[0-5" \
              r"]):\d{2}\s\S+\]\s\"\S+\s(?:/\S+)+/\S+\s\S+\"\s[4-5]\d{2}\s"

    number_of_matched_requests = 0
    viewed_lines = 0

    with open("access_log_Jul95") as file:
        for line in file:
            viewed_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1

                print(re.findall(pattern, line))

print("\nTotal number of viewed lines: %d" % viewed_lines)
print("\nNumber of found lines: %d" % number_of_matched_requests)
