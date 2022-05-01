with open("README.md", "r", encoding='utf-8') as f_in:
    buf = f_in.readlines()
    count = 0
    sec_count = 0
    sec_title = None
    dummy_counter = 0
    for line in buf:
        # if "**" in line:
        if line.startswith("#"):
            if sec_title is None:
                sec_title = line.strip()
                continue
            print(sec_title, "\nsec paper number", sec_count)
            print("total paper number", count)
            sec_count = 0
            sec_title = line.strip()
        if line.startswith("1. **"):
            count += 1
            sec_count += 1